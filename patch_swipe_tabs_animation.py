from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-swipe-tabs-animation"


CSS_PATCH = """
        /* github patch: swipe tabs animation */
        .product-grid {
            transition: transform 0.22s ease, opacity 0.22s ease !important;
            will-change: transform, opacity;
        }
        .product-grid.swipe-anim-left {
            animation: swipePageLeft 0.26s ease both;
        }
        .product-grid.swipe-anim-right {
            animation: swipePageRight 0.26s ease both;
        }
        .tab-bar .tab-item {
            transition: background 0.2s ease, color 0.2s ease, transform 0.18s ease, box-shadow 0.2s ease !important;
        }
        .tab-bar .tab-item.active {
            transform: scale(1.03);
        }
        @keyframes swipePageLeft {
            0% { opacity: .55; transform: translateX(22px); }
            100% { opacity: 1; transform: translateX(0); }
        }
        @keyframes swipePageRight {
            0% { opacity: .55; transform: translateX(-22px); }
            100% { opacity: 1; transform: translateX(0); }
        }
"""


OLD_SWITCH = """            if (next === index) return;
            if (typeof selectStatusFilter === 'function') {
                selectStatusFilter(filters[next]);
            } else {
                currentFilter = filters[next];
                document.querySelectorAll('.tab-item').forEach(t => {
                    t.classList.toggle('active', (t.dataset.status || '') === currentFilter);
                });
                renderGrid();
            }
"""


NEW_SWITCH = """            if (next === index) return;
            const directionClass = dx < 0 ? 'swipe-anim-left' : 'swipe-anim-right';
            if (typeof selectStatusFilter === 'function') {
                selectStatusFilter(filters[next]);
            } else {
                currentFilter = filters[next];
                document.querySelectorAll('.tab-item').forEach(t => {
                    t.classList.toggle('active', (t.dataset.status || '') === currentFilter);
                });
                renderGrid();
            }
            const grid = document.getElementById('productGrid');
            if (grid) {
                grid.classList.remove('swipe-anim-left', 'swipe-anim-right');
                void grid.offsetWidth;
                grid.classList.add(directionClass);
                window.setTimeout(() => grid.classList.remove(directionClass), 280);
            }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-swipe-tabs-strong",
        "20260728-v1-detail-payment-value-right",
        "20260728-v1-detail-note-full-width",
        "20260728-v1-detail-payment-full-width",
        "20260728-v1-detail-payment-spacing",
        "20260728-v1-detail-remove-total",
        "20260728-v1-detail-vertical-photo-light-text",
        "20260728-v1-detail-exact-three-row",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: swipe tabs animation" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "swipe-anim-left" not in html.split("</style>", 1)[-1]:
        if OLD_SWITCH not in html:
            raise SystemExit("未找到增强滑动切换代码，未修改。请先执行 strong swipe 补丁。")
        html = html.replace(OLD_SWITCH, NEW_SWITCH, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
