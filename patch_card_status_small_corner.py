from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-card-status-small-corner"


CSS_PATCH = """
        /* github patch: card status small corner */
        .product-card .img-wrap .tag {
            top: 6px !important;
            left: 6px !important;
            right: auto !important;
            transform: none !important;
            min-width: 0 !important;
            max-width: calc(100% - 12px) !important;
            padding: 3px 8px !important;
            border-radius: 999px !important;
            font-size: 10.5px !important;
            line-height: 1.2 !important;
            font-weight: 500 !important;
            background: rgba(255, 105, 180, 0.76) !important;
            color: rgba(255, 255, 255, 0.96) !important;
            box-shadow: 0 2px 8px rgba(255, 105, 180, 0.16) !important;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
        }
        body.dark .product-card .img-wrap .tag {
            background: rgba(255, 139, 200, 0.70) !important;
            color: rgba(255, 255, 255, 0.96) !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.20) !important;
        }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: card status small corner" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
