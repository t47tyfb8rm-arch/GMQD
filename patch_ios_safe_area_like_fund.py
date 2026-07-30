from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260730-v1-ios-safe-area-like-fund"


CSS_PATCH = """
        /* github patch: ios safe area like fund */
        html {
            background: #fff7fa;
            min-height: 100%;
        }
        html.dark-root {
            background: #161316;
        }
        body {
            min-height: 100vh;
            min-height: 100dvh;
            padding-top: env(safe-area-inset-top, 0px);
            padding-bottom: env(safe-area-inset-bottom, 0px);
            background-color: #fff7fa;
        }
        body.dark {
            background-color: #161316 !important;
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
        document.documentElement.style.backgroundColor = isDark ? '#161316' : '#fff7fa';
        document.body.style.backgroundColor = isDark ? '#161316' : '#fff7fa';
        document.querySelectorAll('meta[name=\"theme-color\"]').forEach(meta => {
            meta.setAttribute('content', isDark ? '#161316' : '#fff7fa');
        });
        const btn = document.getElementById('themeToggle');
        if (btn) {
            btn.textContent = isDark ? '☀' : '☾';
            btn.title = isDark ? '浅色模式' : '深色模式';
        }
    }
"""


def ensure_meta(html: str) -> str:
    if "viewport-fit=cover" not in html:
        html = html.replace(
            'content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"',
            'content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"',
            1,
        )
    if 'name="theme-color"' not in html:
        html = html.replace(
            "    <title>",
            '    <meta name="theme-color" content="#fff7fa">\n    <title>',
            1,
        )
    if 'name="apple-mobile-web-app-status-bar-style"' not in html:
        html = html.replace(
            "    <title>",
            '    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
            '    <meta name="apple-mobile-web-app-capable" content="yes">\n'
            '    <title>',
            1,
        )
    return html


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260730-v1-dark-top-safe-area",
        "20260729-v1-card-status-top-center-small",
        "20260729-v1-card-status-top-right",
        "20260729-v1-card-status-small-corner",
        "20260729-v1-sticky-divider-subtle",
        "20260729-v1-sticky-divider-soften",
        "20260729-v1-sticky-divider-shadow",
        "20260729-v1-hide-home-quick-edit",
        "20260729-v1-sticky-header-tabs",
        "20260729-v1-detail-short-date",
        "20260729-v1-sort-images-detail-fields",
        "20260729-v1-sort-scroll-guard",
        "20260729-v1-dark-sort-theme-button",
        "20260728-v1-swipe-tabs-page-slide",
        "20260728-v1-detail-payment-value-right",
        "20260728-v1-detail-note-full-width",
        "20260728-v1-detail-payment-full-width",
        "20260728-v1-detail-remove-total",
        "20260728-v1-detail-exact-three-row",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    html = ensure_meta(html)

    if "github patch: ios safe area like fund" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "document.documentElement.classList.toggle('dark-root', isDark)" not in html:
        if JS_FIND in html:
            html = html.replace(JS_FIND, JS_REPLACE, 1)
        else:
            raise SystemExit("未找到 applyTheme 函数，未修改。")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
