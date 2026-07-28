from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-compact-rows"


CSS_PATCH = """
        /* github patch: detail compact rows */
        .detail-modal .detail-list {
            display: grid !important;
            grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
            gap: 7px !important;
            margin: 0 0 12px !important;
        }
        .detail-modal .detail-list li {
            min-height: 40px !important;
            padding: 7px 8px !important;
            border-radius: 12px !important;
            background: #fff !important;
            border: 1px solid #f1e5ec !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            justify-content: center !important;
            gap: 3px !important;
        }
        .detail-modal .detail-list li.col-2 {
            grid-column: span 2 !important;
        }
        .detail-modal .detail-list li.wide {
            grid-column: 1 / -1 !important;
        }
        .detail-modal .detail-list .label {
            color: #aaa0a7 !important;
            font-size: 11px !important;
            line-height: 1 !important;
            font-weight: 500 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list .value {
            width: 100% !important;
            min-width: 0 !important;
            color: #292429 !important;
            font-size: 13px !important;
            font-weight: 750 !important;
            line-height: 1.2 !important;
            text-align: left !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list .value.price {
            color: #f052a3 !important;
            font-size: 15px !important;
            font-weight: 900 !important;
        }
        .detail-modal .detail-list li.wide {
            min-height: 38px !important;
            display: grid !important;
            grid-template-columns: 42px minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 10px !important;
        }
        .detail-modal .detail-list li.wide .label {
            font-size: 12px !important;
        }
        .detail-modal .detail-list li.wide .value {
            text-align: right !important;
            font-size: 13px !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            flex-wrap: wrap !important;
            gap: 5px !important;
        }
        @media (max-width: 400px) {
            .detail-modal .detail-list {
                gap: 6px !important;
            }
            .detail-modal .detail-list li {
                padding: 6px 7px !important;
            }
            .detail-modal .detail-list .value {
                font-size: 12px !important;
            }
        }
"""


OLD_LIST = """        list.innerHTML = `
            <li><span class="label">品牌</span><span class="value">${escapeHtml(r.brand || '—')}</span></li>
            <li><span class="label">尺码</span><span class="value">${escapeHtml(r.orderNo || '—')}</span></li>
            <li><span class="label">数量</span><span class="value">${r.quantity || 1}</span></li>
            <li><span class="label">状态</span><span class="value">${escapeHtml(r.status || '—')}</span></li>
            <li class="wide"><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></li>
            <li class="wide payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></li>
            <li><span class="label">合计</span><span class="value price">¥${totalAmount(r).toFixed(2)}</span></li>
            <li><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>
            <li class="wide"><span class="label">备注</span><span class="value">${note}</span></li>
        `;
"""


NEW_LIST = """        list.innerHTML = `
            <li><span class="label">品牌</span><span class="value">${escapeHtml(r.brand || '—')}</span></li>
            <li><span class="label">尺码</span><span class="value">${escapeHtml(r.orderNo || '—')}</span></li>
            <li><span class="label">数量</span><span class="value">${r.quantity || 1}</span></li>
            <li><span class="label">状态</span><span class="value">${escapeHtml(r.status || '—')}</span></li>
            <li class="col-2"><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></li>
            <li class="col-2"><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>
            <li class="wide payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></li>
            <li class="wide"><span class="label">合计</span><span class="value price">¥${totalAmount(r).toFixed(2)}</span></li>
            <li class="wide"><span class="label">备注</span><span class="value">${note}</span></li>
        `;
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail compact rows" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if NEW_LIST not in html:
        if OLD_LIST not in html:
            raise SystemExit("未找到详情字段渲染代码，未修改。请先执行 hard restore 补丁。")
        html = html.replace(OLD_LIST, NEW_LIST, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
