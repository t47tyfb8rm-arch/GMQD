from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-hide-home-quick-edit"


CSS_PATCH = """
        /* github patch: hide home quick edit */
        .product-card .quick-edit {
            display: none !important;
        }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: hide home quick edit" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
