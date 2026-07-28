from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-swipe-tabs-animation-stronger"


CSS_PATCH = """
        /* github patch: swipe tabs animation stronger */
        .product-grid.swipe-anim-left {
            animation: swipePageLeftStrong 0.34s cubic-bezier(.2,.8,.2,1) both !important;
        }
        .product-grid.swipe-anim-right {
            animation: swipePageRightStrong 0.34s cubic-bezier(.2,.8,.2,1) both !important;
        }
        .tab-bar.swipe-tab-flash {
            animation: swipeTabFlash 0.34s ease both !important;
        }
        @keyframes swipePageLeftStrong {
            0% { opacity: .25; transform: translateX(46px) scale(.985); }
            58% { opacity: 1; transform: translateX(-5px) scale(1); }
            100% { opacity: 1; transform: translateX(0) scale(1); }
        }
        @keyframes swipePageRightStrong {
            0% { opacity: .25; transform: translateX(-46px) scale(.985); }
            58% { opacity: 1; transform: translateX(5px) scale(1); }
            100% { opacity: 1; transform: translateX(0) scale(1); }
        }
        @keyframes swipeTabFlash {
            0% { filter: brightness(1.08); transform: translateY(-1px); }
            100% { filter: brightness(1); transform: translateY(0); }
        }
"""


OLD_SNIPPET = """            if (grid) {
                grid.classList.remove('swipe-anim-left', 'swipe-anim-right');
                void grid.offsetWidth;
                grid.classList.add(directionClass);
                window.setTimeout(() => grid.classList.remove(directionClass), 280);
            }
"""


NEW_SNIPPET = """            if (grid) {
                grid.classList.remove('swipe-anim-left', 'swipe-anim-right');
                void grid.offsetWidth;
                grid.classList.add(directionClass);
                window.setTimeout(() => grid.classList.remove(directionClass), 360);
            }
            const tabBar = document.getElementById('tabBar');
            if (tabBar) {
                tabBar.classList.remove('swipe-tab-flash');
                void tabBar.offsetWidth;
                tabBar.classList.add('swipe-tab-flash');
                window.setTimeout(() => tabBar.classList.remove('swipe-tab-flash'), 360);
            }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-swipe-tabs-animation",
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

    if "github patch: swipe tabs animation stronger" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "swipe-tab-flash" not in html.split("</style>", 1)[-1]:
        if OLD_SNIPPET not in html:
            raise SystemExit("未找到滑动动画代码，未修改。请先执行 animation 补丁。")
        html = html.replace(OLD_SNIPPET, NEW_SNIPPET, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
