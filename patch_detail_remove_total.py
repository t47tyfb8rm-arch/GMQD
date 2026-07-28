from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-remove-total"


CSS_PATCH = """
        /* github patch: detail remove total */
        .detail-modal .detail-payment-only {
            display: grid !important;
            grid-template-columns: 46px minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 10px !important;
        }
        .detail-modal .detail-payment-only .detail-value {
            text-align: right !important;
        }
"""


OLD_TWO_COL = """            <li>
                <div class="detail-row-2">
                    <div class="detail-wide-card payment-detail-row">
                        <span class="detail-label">付款</span>
                        <span class="detail-value">${paymentDetailHtml(r)}</span>
                    </div>
                    <div class="detail-wide-card">
                        <span class="detail-label">合计</span>
                        <span class="detail-value price">¥${totalAmount(r).toFixed(2)}</span>
                    </div>
                </div>
            </li>
"""


OLD_SEPARATE = """            <li>
                <div class="detail-wide-card payment-detail-row">
                    <span class="detail-label">付款</span>
                    <span class="detail-value">${paymentDetailHtml(r)}</span>
                </div>
            </li>
            <li>
                <div class="detail-wide-card">
                    <span class="detail-label">合计</span>
                    <span class="detail-value price">¥${totalAmount(r).toFixed(2)}</span>
                </div>
            </li>
"""


NEW_PAYMENT_ONLY = """            <li>
                <div class="detail-wide-card payment-detail-row detail-payment-only">
                    <span class="detail-label">付款</span>
                    <span class="detail-value">${paymentDetailHtml(r)}</span>
                </div>
            </li>
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail remove total" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if NEW_PAYMENT_ONLY not in html:
        if OLD_TWO_COL in html:
            html = html.replace(OLD_TWO_COL, NEW_PAYMENT_ONLY, 1)
        elif OLD_SEPARATE in html:
            html = html.replace(OLD_SEPARATE, NEW_PAYMENT_ONLY, 1)
        else:
            raise SystemExit("未找到详情付款/合计结构，未修改。")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
