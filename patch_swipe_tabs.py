from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-swipe-tabs"


CSS_PATCH = """
        /* github patch: swipe status tabs */
        #productGrid {
            touch-action: pan-y;
        }
        .tab-bar {
            touch-action: pan-y;
        }
"""


OLD_TAB_HANDLER = """    // ===== 标签切换 =====
    document.getElementById('tabBar').addEventListener('click', (e) => {
        const tab = e.target.closest('.tab-item');
        if (!tab) return;
        document.querySelectorAll('.tab-item').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        currentFilter = tab.dataset.status || '';
        renderGrid();
    });
"""


NEW_TAB_HANDLER = """    // ===== 标签切换 =====
    const STATUS_FILTERS = ['', '已购买', '待发货', '已收货'];

    function selectStatusFilter(status) {
        currentFilter = status || '';
        document.querySelectorAll('.tab-item').forEach(t => {
            t.classList.toggle('active', (t.dataset.status || '') === currentFilter);
        });
        renderGrid();
    }

    document.getElementById('tabBar').addEventListener('click', (e) => {
        const tab = e.target.closest('.tab-item');
        if (!tab) return;
        selectStatusFilter(tab.dataset.status || '');
    });

    function setupSwipeTabs() {
        const swipeArea = document.getElementById('productGrid');
        if (!swipeArea || swipeArea.dataset.swipeTabsReady === '1') return;
        swipeArea.dataset.swipeTabsReady = '1';

        let startX = 0;
        let startY = 0;
        let startTime = 0;

        swipeArea.addEventListener('touchstart', (event) => {
            if (event.touches.length !== 1) return;
            const target = event.target;
            if (target.closest('button, input, textarea, select, .modal-overlay')) return;
            startX = event.touches[0].clientX;
            startY = event.touches[0].clientY;
            startTime = Date.now();
        }, { passive: true });

        swipeArea.addEventListener('touchend', (event) => {
            if (!startTime || !event.changedTouches.length) return;
            const dx = event.changedTouches[0].clientX - startX;
            const dy = event.changedTouches[0].clientY - startY;
            const elapsed = Date.now() - startTime;
            startTime = 0;

            if (elapsed > 650 || Math.abs(dx) < 55 || Math.abs(dx) < Math.abs(dy) * 1.25) return;

            const currentIndex = Math.max(0, STATUS_FILTERS.indexOf(currentFilter));
            const nextIndex = dx < 0
                ? Math.min(STATUS_FILTERS.length - 1, currentIndex + 1)
                : Math.max(0, currentIndex - 1);
            if (nextIndex !== currentIndex) {
                selectStatusFilter(STATUS_FILTERS[nextIndex]);
            }
        }, { passive: true });
    }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-platform-custom-default",
        "20260728-v1-form-detail-smaller",
        "20260728-v1-form-detail-refine",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: swipe status tabs" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "function setupSwipeTabs()" not in html:
        if OLD_TAB_HANDLER not in html:
            raise SystemExit("未找到分类切换代码，未修改。")
        html = html.replace(OLD_TAB_HANDLER, NEW_TAB_HANDLER, 1)

    if "setupSwipeTabs();" not in html:
        marker = "    loadRecordsFromApi();\n"
        if marker not in html:
            raise SystemExit("未找到初始化位置，未修改。")
        html = html.replace(marker, "    setupSwipeTabs();\n" + marker, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
