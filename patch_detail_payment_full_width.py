from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-payment-full-width"


CSS_PATCH = """
        /* github patch: detail payment full width */
        .detail-modal .detail-list > li:has(.detail-payment-only),
        .detail-modal .detail-list > li:has(.payment-detail-row) {
            width: 100% !important;
            grid-column: 1 / -1 !important;
            display: block !important;
        }
        .detail-modal .detail-wide-card.payment-detail-row,
        .detail-modal .detail-payment-only {
            width: 100% !important;
            max-width: none !important;
            box-sizing: border-box !important;
            display: grid !important;
            grid-template-columns: 46px minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 10px !important;
        }
        .detail-modal .detail-wide-card.payment-detail-row .detail-value,
        .detail-modal .detail-payment-only .detail-value {
            min-width: 0 !important;
            text-align: right !important;
        }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-detail-payment-spacing",
        "20260728-v1-detail-remove-total",
        "20260728-v1-detail-vertical-photo-light-text",
        "20260728-v1-detail-exact-three-row",
        "20260728-v1-detail-three-equal-cards",
        "20260728-v1-detail-stop-overlap",
        "20260728-v1-detail-compact-rows",
        "20260728-v1-detail-hard-restore",
        "20260728-v1-detail-restore-full-grid",
        "20260728-v1-detail-calm-sheet",
        "20260728-v1-detail-receipt-layout",
        "20260728-v1-detail-summary-grid",
        "20260728-v1-detail-summary-layout",
        "20260728-v1-detail-elegant-compact",
        "20260728-v1-detail-single-line-compact",
        "20260728-v1-detail-keep-image-clean",
        "20260728-v1-swipe-tabs",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-platform-custom-default",
        "20260728-v1-form-detail-smaller",
        "20260728-v1-form-detail-refine",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: detail payment full width" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
