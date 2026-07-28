from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-swipe-tabs-strong"


CSS_PATCH = """
        /* github patch: swipe status tabs strong */
        body, #productGrid, .product-grid {
            overscroll-behavior-x: contain;
        }
"""


JS_PATCH = """

    // github patch: swipe status tabs strong
    function setupSwipeTabsStrong() {
        if (window.__gmqdSwipeTabsStrongReady) return;
        window.__gmqdSwipeTabsStrongReady = true;

        const filters = ['', '已购买', '待发货', '已收货'];
        let sx = 0;
        let sy = 0;
        let st = 0;
        let validStart = false;

        function isModalOpen() {
            return !!document.querySelector('.modal-overlay.active');
        }

        function switchBySwipe(dx) {
            const current = typeof currentFilter === 'string' ? currentFilter : '';
            const index = Math.max(0, filters.indexOf(current));
            const next = dx < 0 ? Math.min(filters.length - 1, index + 1) : Math.max(0, index - 1);
            if (next === index) return;
            if (typeof selectStatusFilter === 'function') {
                selectStatusFilter(filters[next]);
            } else {
                currentFilter = filters[next];
                document.querySelectorAll('.tab-item').forEach(t => {
                    t.classList.toggle('active', (t.dataset.status || '') === currentFilter);
                });
                renderGrid();
            }
        }

        document.addEventListener('touchstart', (event) => {
            if (isModalOpen() || event.touches.length !== 1) {
                validStart = false;
                return;
            }
            const target = event.target;
            if (target.closest('button, input, textarea, select, .quick-edit, .add-btn')) {
                validStart = false;
                return;
            }
            sx = event.touches[0].clientX;
            sy = event.touches[0].clientY;
            st = Date.now();
            validStart = true;
        }, { passive: true, capture: true });

        document.addEventListener('touchend', (event) => {
            if (!validStart || isModalOpen() || !event.changedTouches.length) return;
            validStart = false;
            const dx = event.changedTouches[0].clientX - sx;
            const dy = event.changedTouches[0].clientY - sy;
            const dt = Date.now() - st;
            if (dt > 900) return;
            if (Math.abs(dx) < 38) return;
            if (Math.abs(dx) < Math.abs(dy) * 1.05) return;
            switchBySwipe(dx);
        }, { passive: true, capture: true });
    }

    setupSwipeTabsStrong();
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-swipe-tabs",
        "20260728-v1-detail-payment-value-right",
        "20260728-v1-detail-note-full-width",
        "20260728-v1-detail-payment-full-width",
        "20260728-v1-detail-payment-spacing",
        "20260728-v1-detail-remove-total",
        "20260728-v1-detail-vertical-photo-light-text",
        "20260728-v1-detail-exact-three-row",
        "20260728-v1-detail-three-equal-cards",
        "20260728-v1-detail-stop-overlap",
        "20260728-v1-detail-compact-rows",
        "20260728-v1-detail-hard-restore",
        "20260728-v1-detail-restore-full-grid",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: swipe status tabs strong" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "setupSwipeTabsStrong" not in html:
        html = html.replace("</script>", JS_PATCH + "\n</script>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
