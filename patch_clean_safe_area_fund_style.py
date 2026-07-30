from pathlib import Path
import re


TARGET = Path("index.html")
VERSION_TO = "20260730-v1-clean-safe-area-fund-style"


CSS_PATCH = """
        /* github patch: clean safe area fund style */
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
        .header-info {
            top: env(safe-area-inset-top, 0px) !important;
        }
        .tab-bar {
            top: calc(env(safe-area-inset-top, 0px) + var(--sticky-header-height, 76px)) !important;
        }
        body.dark .header-info,
        body.dark .tab-bar {
            background: rgba(22, 19, 22, .98) !important;
        }
"""


PATCH_MARKERS = (
    "github patch: dark top safe area",
    "github patch: ios safe area like fund",
    "github patch: safe area header extend",
    "github patch: clean safe area fund style",
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


def remove_old_safe_area_patches(html: str) -> str:
    for marker in PATCH_MARKERS:
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
        html = html.replace(
            "user-scalable=no\"",
            "user-scalable=no, viewport-fit=cover\"",
            1,
        )
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


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    html = remove_old_safe_area_patches(html)
    html = ensure_meta(html)
    html = ensure_apply_theme(html)

    version_pattern = re.compile(r"const APP_VERSION = ['\"][^'\"]+['\"];")
    if version_pattern.search(html):
        html = version_pattern.sub(f"const APP_VERSION = '{VERSION_TO}';", html, count=1)
    else:
        html = html.replace("<script>", f"<script>\n    const APP_VERSION = '{VERSION_TO}';", 1)

    html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
