from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-swipe-tabs-drawer-animation"


CSS_PATCH = """
        /* github patch: swipe tabs drawer animation */
        .product-grid.swipe-anim-left {
            animation: swipeDrawerLeft 0.24s ease-out both !important;
        }
        .product-grid.swipe-anim-right {
            animation: swipeDrawerRight 0.24s ease-out both !important;
        }
        .tab-bar.swipe-tab-flash {
            animation: none !important;
        }
        @keyframes swipeDrawerLeft {
            0% { opacity: .62; transform: translateX(34px); }
            100% { opacity: 1; transform: translateX(0); }
        }
        @keyframes swipeDrawerRight {
            0% { opacity: .62; transform: translateX(-34px); }
            100% { opacity: 1; transform: translateX(0); }
        }
"""


OLD_TIMEOUTS = (
    "window.setTimeout(() => grid.classList.remove(directionClass), 440);",
    "window.setTimeout(() => grid.classList.remove(directionClass), 360);",
    "window.setTimeout(() => grid.classList.remove(directionClass), 280);",
)
NEW_TIMEOUT = "window.setTimeout(() => grid.classList.remove(directionClass), 260);"


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-swipe-tabs-animation-bolder",
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

    if "github patch: swipe tabs drawer animation" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    for old_timeout in OLD_TIMEOUTS:
        html = html.replace(old_timeout, NEW_TIMEOUT)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
