from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-sticky-divider-soften"


CSS_PATCH = """
        /* github patch: sticky divider soften */
        .tab-bar {
            border-bottom: 1px solid rgba(234, 211, 220, 0.46) !important;
            box-shadow: 0 7px 14px rgba(92, 52, 70, 0.045) !important;
        }
        body.dark .tab-bar {
            border-bottom-color: rgba(82, 66, 77, 0.52) !important;
            box-shadow: 0 7px 14px rgba(0, 0, 0, 0.14) !important;
        }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: sticky divider soften" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
