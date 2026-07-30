from pathlib import Path
import re


TARGET = Path("index.html")
VERSION_TO = "20260730-v1-app-top-fund-structure"


CSS_PATCH = """
        /* github patch: app top fund structure */
        html {
            background: #fff7fa !important;
            min-height: 100%;
        }
        html.dark-root {
            background: #161316 !important;
        }
        body {
            min-height: 100vh;
            min-height: 100dvh;
            padding-top: env(safe-area-inset-top, 0px) !important;
            padding-bottom: env(safe-area-inset-bottom, 0px);
            background: #fff7fa !important;
        }
        body.dark {
            background: #161316 !important;
        }
        .app-top {
            position: sticky;
            top: env(safe-area-inset-top, 0px);
            z-index: 90;
            background: #fff7fa;
            box-shadow: 0 8px 20px rgba(92, 52, 70, 0.035);
        }
        body.dark .app-top {
            background: #161316;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.16);
        }
        .app-top .header-info,
        .app-top .tab-bar {
            position: static !important;
            top: auto !important;
            z-index: auto !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        .app-top .tab-bar {
            border-bottom-color: rgba(234, 211, 220, 0.12) !important;
        }
        body.dark .app-top .tab-bar {
            border-bottom-color: rgba(82, 66, 77, 0.20) !important;
        }
        .product-grid {
            padding-top: 20px !important;
        }
"""


SAFE_AREA_MARKERS = (
    "github patch: dark top safe area",
    "github patch: ios safe area like fund",
    "github patch: safe area header extend",
    "github patch: clean safe area fund style",
    "github patch: app top fund structure",
)


JS_FIND = """    function applyTheme(theme) {
        const isDark = theme === 'dark';
        document.body.classList.toggle('dark', isDark);
        const btn = document.getElementById('themeToggle');
        if (btn) {
            btn.textContent = isDark ? '☀' : '☾';
            btn.title = isDark ? '浅色模式' : '深色模式';
        }
    }
"""


JS_REPLACE = """    function applyTheme(theme) {
        const isDark = theme === 'dark';
        document.body.classList.toggle('dark', isDark);
        document.documentElement.classList.toggle('dark-root', isDark);
        const bg = isDark ? '#161316' : '#fff7fa';
        document.documentElement.style.backgroundColor = bg;
        document.body.style.backgroundColor = bg;
        document.querySelectorAll('meta[name=\"theme-color\"]').forEach(meta => {
            meta.setAttribute('content', bg);
        });
        const btn = document.getElementById('themeToggle');
        if (btn) {
            btn.textContent = isDark ? '☀' : '☾';
            btn.title = isDark ? '浅色模式' : '深色模式';
        }
    }
"""


def remove_patch_blocks(html: str) -> str:
    for marker in SAFE_AREA_MARKERS:
        pattern = re.compile(
            r"\n\s*/\* " + re.escape(marker) + r" \*/.*?(?=\n\s*/\* github patch:|\n\s*</style>)",
            re.S,
        )
        html = pattern.sub("", html)
    return html


def ensure_meta(html: str) -> str:
    html = html.replace("\\n    <meta name=\"theme-color\"", "\n    <meta name=\"theme-color\"")
    html = html.replace(
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\">",
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover\">",
        1,
    )
    if "viewport-fit=cover" not in html:
        html = html.replace("user-scalable=no\"", "user-scalable=no, viewport-fit=cover\"", 1)
    if 'name="theme-color"' not in html:
        html = html.replace("    <title>", '    <meta name="theme-color" content="#fff7fa">\n    <title>', 1)
    if 'name="apple-mobile-web-app-status-bar-style"' not in html:
        html = html.replace(
            "    <title>",
            '    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
            '    <meta name="apple-mobile-web-app-capable" content="yes">\n'
            '    <title>',
            1,
        )
    return html


def ensure_apply_theme(html: str) -> str:
    if "document.documentElement.classList.toggle('dark-root', isDark)" in html:
        return html
    if JS_FIND not in html:
        raise SystemExit("未找到 applyTheme 函数，未修改。")
    return html.replace(JS_FIND, JS_REPLACE, 1)


def wrap_app_top(html: str) -> str:
    if 'class="app-top"' in html:
        return html

    header_start = html.find('<div class="header-info">')
    tab_start = html.find('<div class="tab-bar"', header_start)
    grid_start = html.find('<div class="product-grid"', tab_start)
    if header_start < 0 or tab_start < 0 or grid_start < 0:
        raise SystemExit("未找到顶部/分类/商品网格结构，未修改。")

    block = html[header_start:grid_start].rstrip()
    wrapped = '<div class="app-top">\n' + block + '\n</div>\n\n'
    return html[:header_start] + wrapped + html[grid_start:]


def update_version(html: str) -> str:
    pattern = re.compile(r"const APP_VERSION = ['\"][^'\"]+['\"];")
    if pattern.search(html):
        return pattern.sub(f"const APP_VERSION = '{VERSION_TO}';", html, count=1)
    return html.replace("<script>", f"<script>\n    const APP_VERSION = '{VERSION_TO}';", 1)


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    html = remove_patch_blocks(html)
    html = ensure_meta(html)
    html = ensure_apply_theme(html)
    html = wrap_app_top(html)
    html = update_version(html)
    html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
