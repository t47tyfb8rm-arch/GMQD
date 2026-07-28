from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-swipe-tabs-animation-bolder"


CSS_PATCH = """
        /* github patch: swipe tabs animation bolder */
        .product-grid.swipe-anim-left {
            animation: swipePageLeftBolder 0.42s cubic-bezier(.16,.9,.18,1) both !important;
        }
        .product-grid.swipe-anim-right {
            animation: swipePageRightBolder 0.42s cubic-bezier(.16,.9,.18,1) both !important;
        }
        .tab-bar.swipe-tab-flash {
            animation: swipeTabFlashBolder 0.42s ease both !important;
        }
        .product-grid.swipe-anim-left::before,
        .product-grid.swipe-anim-right::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background: rgba(255, 105, 180, .08);
            animation: swipeTintBolder 0.42s ease both;
            z-index: 1;
        }
        @keyframes swipePageLeftBolder {
            0% { opacity: .08; transform: translateX(86px) scale(.965); filter: blur(.6px); }
            46% { opacity: 1; transform: translateX(-12px) scale(1.01); filter: blur(0); }
            100% { opacity: 1; transform: translateX(0) scale(1); filter: blur(0); }
        }
        @keyframes swipePageRightBolder {
            0% { opacity: .08; transform: translateX(-86px) scale(.965); filter: blur(.6px); }
            46% { opacity: 1; transform: translateX(12px) scale(1.01); filter: blur(0); }
            100% { opacity: 1; transform: translateX(0) scale(1); filter: blur(0); }
        }
        @keyframes swipeTabFlashBolder {
            0% { filter: brightness(1.16); transform: translateY(-2px) scale(1.01); }
            100% { filter: brightness(1); transform: translateY(0) scale(1); }
        }
        @keyframes swipeTintBolder {
            0% { opacity: 1; }
            100% { opacity: 0; }
        }
"""


OLD_TIMEOUT = "window.setTimeout(() => grid.classList.remove(directionClass), 360);"
NEW_TIMEOUT = "window.setTimeout(() => grid.classList.remove(directionClass), 440);"
OLD_TAB_TIMEOUT = "window.setTimeout(() => tabBar.classList.remove('swipe-tab-flash'), 360);"
NEW_TAB_TIMEOUT = "window.setTimeout(() => tabBar.classList.remove('swipe-tab-flash'), 440);"


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-swipe-tabs-animation-stronger",
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

    if "github patch: swipe tabs animation bolder" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    html = html.replace(OLD_TIMEOUT, NEW_TIMEOUT)
    html = html.replace(OLD_TAB_TIMEOUT, NEW_TAB_TIMEOUT)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
