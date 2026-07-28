from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-vertical-photo-light-text"


CSS_PATCH = """
        /* github patch: detail vertical photo light text */
        .detail-modal .detail-img-area {
            width: min(46vw, 168px) !important;
            height: min(34vh, 230px) !important;
            aspect-ratio: 3 / 4 !important;
            margin: 0 auto 9px !important;
            border-radius: 18px !important;
        }
        .detail-modal .detail-img-area img {
            object-fit: cover !important;
        }
        .detail-modal .detail-title {
            text-align: center !important;
            font-weight: 650 !important;
        }
        .detail-modal .detail-label {
            font-weight: 400 !important;
        }
        .detail-modal .detail-value {
            font-weight: 500 !important;
        }
        .detail-modal .detail-value.price {
            font-weight: 650 !important;
            font-size: 14px !important;
        }
        .detail-modal .detail-row-2 {
            display: grid !important;
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
            gap: 7px !important;
            width: 100% !important;
        }
        .detail-modal .detail-row-2 .detail-wide-card {
            min-height: 42px !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            justify-content: center !important;
            gap: 4px !important;
        }
        .detail-modal .detail-row-2 .detail-wide-card .detail-value {
            width: 100% !important;
            text-align: left !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-start !important;
        }
        @media (max-width: 400px) {
            .detail-modal .detail-img-area {
                width: min(44vw, 150px) !important;
                height: min(31vh, 204px) !important;
            }
        }
"""


OLD_BLOCK = """            <li>
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


NEW_BLOCK = """            <li>
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


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail vertical photo light text" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if NEW_BLOCK not in html:
        if OLD_BLOCK not in html:
            raise SystemExit("未找到付款/合计详情结构，未修改。请先执行 exact three row 补丁。")
        html = html.replace(OLD_BLOCK, NEW_BLOCK, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
