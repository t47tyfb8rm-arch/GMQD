from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-sticky-header-tabs"


CSS_PATCH = """
        /* github patch: sticky header and tabs */
        :root {
            --sticky-header-height: 76px;
        }
        .header-info {
            position: sticky !important;
            top: 0 !important;
            z-index: 90 !important;
            background: rgba(255, 247, 250, .96) !important;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            box-shadow: 0 1px 0 rgba(240, 224, 224, .9);
        }
        body.dark .header-info {
            background: rgba(22, 19, 22, .96) !important;
            box-shadow: 0 1px 0 rgba(51, 42, 49, .9);
        }
        .tab-bar {
            position: sticky !important;
            top: var(--sticky-header-height) !important;
            z-index: 89 !important;
            padding: 4px 18px 10px !important;
            background: rgba(255, 247, 250, .96) !important;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            box-shadow: 0 1px 0 rgba(240, 224, 224, .9);
        }
        body.dark .tab-bar {
            background: rgba(22, 19, 22, .96) !important;
            box-shadow: 0 1px 0 rgba(51, 42, 49, .9);
        }
        .product-grid {
            padding-top: 22px !important;
        }
        @media (max-width: 400px) {
            .tab-bar {
                padding: 4px 16px 9px !important;
            }
        }
"""


NO_COMPRESS_PATCH = """
        /* github patch: sticky header no-compress override */
        .header-info {
            padding: 18px 20px 10px !important;
        }
        .header-info .title {
            font-size: 26px !important;
            margin-bottom: 6px !important;
        }
        .header-info .subtitle {
            font-size: 14.5px !important;
        }
        .header-sort-btn,
        .header-theme-btn {
            height: 34px !important;
        }
        .tab-bar .tab-item {
            height: 38px !important;
            font-size: 14px !important;
        }
        @media (max-width: 400px) {
            .header-info {
                padding: 16px 20px 9px !important;
            }
            .header-info .title {
                font-size: 25px !important;
            }
            .header-info .subtitle {
                font-size: 13.5px !important;
            }
            .header-sort-btn,
            .header-theme-btn {
                height: 32px !important;
            }
            .tab-bar .tab-item {
                height: 36px !important;
                font-size: 13px !important;
            }
        }
"""


JS_PATCH = """

    // github patch: sticky header and tabs
    function updateStickyHeaderOffset() {
        const header = document.querySelector('.header-info');
        if (!header) return;
        document.documentElement.style.setProperty('--sticky-header-height', `${Math.ceil(header.getBoundingClientRect().height)}px`);
    }
    updateStickyHeaderOffset();
    window.addEventListener('resize', updateStickyHeaderOffset);
    window.addEventListener('orientationchange', () => window.setTimeout(updateStickyHeaderOffset, 180));
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: sticky header and tabs" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "github patch: sticky header no-compress override" not in html:
        html = html.replace("    </style>", NO_COMPRESS_PATCH + "\n    </style>", 1)

    if "function updateStickyHeaderOffset" not in html:
        markers = (
            "    // ===== 初始化 =====",
            "    // ===== 鍒濆鍖?=====",
            "    window.addEventListener('load',",
        )
        for marker in markers:
            if marker in html:
                html = html.replace(marker, JS_PATCH + "\n" + marker, 1)
                break
        else:
            html = html.replace("</script>", JS_PATCH + "\n</script>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
