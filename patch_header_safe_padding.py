from pathlib import Path
import re


TARGET = Path("index.html")
VERSION_TO = "20260730-v1-header-safe-padding"


CSS_PATCH = """
        /* github patch: header safe padding */
        html {
            background: #fff7fa !important;
        }
        html.dark-root {
            background: #161316 !important;
        }
        body {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        .header-info {
            position: sticky !important;
            top: 0 !important;
            z-index: 90 !important;
            padding-top: calc(env(safe-area-inset-top, 0px) + 18px) !important;
            background: #fff7fa !important;
        }
        body.dark .header-info {
            background: #161316 !important;
        }
        .tab-bar {
            position: sticky !important;
            top: var(--sticky-header-height, 96px) !important;
            z-index: 89 !important;
            background: #fff7fa !important;
        }
        body.dark .tab-bar {
            background: #161316 !important;
        }
        .product-grid {
            padding-top: 20px !important;
        }
"""


PATCH_MARKERS = (
    "github patch: app top fund structure",
    "github patch: clean safe area fund style",
    "github patch: dark top safe area",
    "github patch: ios safe area like fund",
    "github patch: safe area header extend",
    "github patch: revert safe scroll",
    "github patch: header safe padding",
)


def remove_patch_blocks(html: str) -> str:
    for marker in PATCH_MARKERS:
        pattern = re.compile(
            r"\n\s*/\* " + re.escape(marker) + r" \*/.*?(?=\n\s*/\* github patch:|\n\s*</style>)",
            re.S,
        )
        html = pattern.sub("", html)
    return html


def unwrap_app_top(html: str) -> str:
    if 'class="app-top"' not in html:
        return html
    html = html.replace('<div class="app-top">\n', '', 1)
    close_before_product = '\n</div>\n\n<!-- ===== 商品网格 ===== -->'
    product_marker = '\n\n<!-- ===== 商品网格 ===== -->'
    if close_before_product in html:
        html = html.replace(close_before_product, product_marker, 1)
    return html


def update_version(html: str) -> str:
    pattern = re.compile(r"const APP_VERSION = ['\"][^'\"]+['\"];")
    if pattern.search(html):
        return pattern.sub(f"const APP_VERSION = '{VERSION_TO}';", html, count=1)
    return html.replace("<script>", f"<script>\n    const APP_VERSION = '{VERSION_TO}';", 1)


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    html = remove_patch_blocks(html)
    html = unwrap_app_top(html)
    html = update_version(html)
    html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)
    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
