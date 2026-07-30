from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260730-v1-dark-top-safe-area"


CSS_PATCH = """
        /* github patch: dark top safe area */
        html {
            background: #fff7fa;
            min-height: 100%;
        }
        html.dark-root {
            background: #161316;
        }
        body.dark {
            background-color: #161316 !important;
        }
        body.dark::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: env(safe-area-inset-top, 0px);
            background: #161316;
            z-index: 9999;
            pointer-events: none;
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
        const themeMeta = document.querySelector('meta[name=\"theme-color\"]');
        if (themeMeta) {
            themeMeta.setAttribute('content', isDark ? '#161316' : '#fff7fa');
        }
        const btn = document.getElementById('themeToggle');
        if (btn) {
            btn.textContent = isDark ? '☀' : '☾';
            btn.title = isDark ? '浅色模式' : '深色模式';
        }
    }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if 'name="theme-color"' not in html:
        html = html.replace(
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">',
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">\n'
            '    <meta name="theme-color" content="#fff7fa">',
            1,
        )
    elif 'viewport-fit=cover' not in html:
        html = html.replace(
            'content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"',
            'content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"',
            1,
        )

    if "github patch: dark top safe area" not in html:
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
