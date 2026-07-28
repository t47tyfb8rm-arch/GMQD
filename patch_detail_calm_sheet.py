from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-calm-sheet"


CSS_PATCH = """
        /* github patch: detail calm sheet */
        .modal-content.detail-modal {
            width: min(88vw, 368px) !important;
            max-height: 78vh !important;
            padding: 16px 16px 14px !important;
            border-radius: 24px !important;
            overflow-y: auto !important;
        }
        .detail-modal .modal-header {
            margin-bottom: 8px !important;
        }
        .detail-modal .modal-header h3 {
            font-size: 20px !important;
            font-weight: 850 !important;
        }
        .detail-modal .modal-header .close-btn {
            width: 34px !important;
            height: 34px !important;
            font-size: 20px !important;
        }
        .detail-modal .detail-img-area {
            width: 150px !important;
            height: 178px !important;
            margin: 0 auto 9px !important;
            border-radius: 18px !important;
            background: #fff7fb !important;
            box-shadow: none !important;
            overflow: hidden !important;
        }
        .detail-modal .detail-img-area.has-image {
            background: #fff !important;
        }
        .detail-modal .detail-img-area img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
        }
        .detail-modal .detail-title {
            max-width: 92% !important;
            margin: 0 auto 8px !important;
            color: #231f23 !important;
            font-size: 17px !important;
            font-weight: 850 !important;
            line-height: 1.25 !important;
            text-align: center !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            text-shadow: none !important;
        }
        .detail-modal .detail-list {
            display: block !important;
            margin: 0 !important;
            padding: 0 !important;
            border: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        .detail-modal .detail-list li,
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            border: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
            border-radius: 0 !important;
        }
        .detail-modal .detail-calm-head {
            padding: 0 0 9px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 10px !important;
        }
        .detail-modal .detail-calm-price {
            color: #f052a3 !important;
            font-size: 22px !important;
            font-weight: 900 !important;
            line-height: 1 !important;
        }
        .detail-modal .detail-calm-status {
            padding: 4px 10px !important;
            border-radius: 999px !important;
            background: #fff0f7 !important;
            color: #e74799 !important;
            font-size: 12px !important;
            font-weight: 800 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-calm-meta {
            margin: 0 0 10px !important;
            color: #746a72 !important;
            font-size: 13px !important;
            font-weight: 650 !important;
            line-height: 1.35 !important;
            text-align: center !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-calm-panel {
            margin: 0 !important;
            padding: 4px 12px !important;
            border-radius: 15px !important;
            background: #fffafc !important;
            border: 1px solid #f1e4eb !important;
        }
        .detail-modal .detail-calm-row {
            min-height: 31px !important;
            padding: 7px 0 !important;
            border-bottom: 1px solid #f1e6ec !important;
            display: grid !important;
            grid-template-columns: 42px minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 10px !important;
        }
        .detail-modal .detail-calm-row:last-child {
            border-bottom: 0 !important;
        }
        .detail-modal .detail-calm-row .label {
            color: #aaa0a7 !important;
            font-size: 12px !important;
            font-weight: 500 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-calm-row .value {
            min-width: 0 !important;
            color: #292429 !important;
            font-size: 13px !important;
            font-weight: 700 !important;
            text-align: right !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            flex-wrap: nowrap !important;
            gap: 5px !important;
            overflow: hidden !important;
        }
        .detail-modal .payment-chip {
            max-width: 100% !important;
            padding: 2px 7px !important;
            border-radius: 999px !important;
            background: #fff0f7 !important;
            font-size: 12px !important;
            line-height: 1.35 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-actions {
            margin-top: 11px !important;
            padding-top: 0 !important;
            border-top: 0 !important;
            gap: 9px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 42px !important;
            border-radius: 13px !important;
            font-size: 15px !important;
            font-weight: 750 !important;
        }
        .detail-modal .detail-actions .btn-delete {
            background: #fff4f7 !important;
        }
        body.dark .detail-modal .detail-title,
        body.dark .detail-modal .detail-calm-row .value {
            color: #fff7fb !important;
        }
        body.dark .detail-modal .detail-calm-meta {
            color: #cfc3ca !important;
        }
        body.dark .detail-modal .detail-calm-panel {
            background: #231e23 !important;
            border-color: rgba(255,255,255,.08) !important;
        }
        body.dark .detail-modal .detail-calm-row {
            border-bottom-color: rgba(255,255,255,.08) !important;
        }
        @media (max-width: 400px) {
            .detail-modal .detail-img-area {
                width: 138px !important;
                height: 164px !important;
            }
            .detail-modal .detail-calm-price {
                font-size: 21px !important;
            }
            .detail-modal .detail-title {
                font-size: 16px !important;
            }
        }
"""


OLD_LISTS = [
"""        list.innerHTML = `
            <li class="detail-receipt-head">
                <span class="detail-receipt-price">¥${totalAmount(r).toFixed(2)}</span>
                <span class="detail-receipt-status">${escapeHtml(r.status || '—')}</span>
            </li>
            <li class="detail-receipt-tags">
                <span class="detail-receipt-tag">${escapeHtml(r.brand || '未填品牌')}</span>
                <span class="detail-receipt-tag">${escapeHtml(r.orderNo || '未填尺码')}</span>
                <span class="detail-receipt-tag">${r.quantity || 1}件</span>
            </li>
            <li class="detail-receipt-panel">
                <div class="detail-receipt-row"><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></div>
                <div class="detail-receipt-row payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></div>
                ${r.date ? `<div class="detail-receipt-row"><span class="label">日期</span><span class="value">${escapeHtml(r.date)}</span></div>` : ''}
                <div class="detail-receipt-row"><span class="label">备注</span><span class="value">${note}</span></div>
            </li>
        `;
""",
"""        list.innerHTML = `
            <li class="detail-summary-row">
                <span class="detail-summary-price">¥${totalAmount(r).toFixed(2)}</span>
                <span class="detail-status-pill">${escapeHtml(r.status || '—')}</span>
            </li>
            <li class="detail-chip-row">
                <span class="detail-chip">${escapeHtml(r.brand || '未填品牌')}</span>
                <span class="detail-chip">${escapeHtml(r.orderNo || '未填尺码')}</span>
                <span class="detail-chip">${r.quantity || 1}件</span>
            </li>
            <li class="detail-info-panel">
                <div class="detail-info-row"><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></div>
                <div class="detail-info-row payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></div>
                ${r.date ? `<div class="detail-info-row"><span class="label">日期</span><span class="value">${escapeHtml(r.date)}</span></div>` : ''}
                <div class="detail-info-row"><span class="label">备注</span><span class="value">${note}</span></div>
            </li>
        `;
""",
"""        list.innerHTML = `
            <li><span class="label">品牌</span><span class="value">${escapeHtml(r.brand || '—')}</span></li>
            <li><span class="label">尺码</span><span class="value">${escapeHtml(r.orderNo || '—')}</span></li>
            <li><span class="label">数量</span><span class="value">${r.quantity}</span></li>
            <li><span class="label">状态</span><span class="value">${r.status}</span></li>
            <li class="wide"><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></li>
            <li class="wide payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></li>
            <li><span class="label">合计</span><span class="value price">¥${totalAmount(r).toFixed(2)}</span></li>
            <li><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>
            <li class="wide"><span class="label">备注</span><span class="value">${note}</span></li>
        `;
""",
"""        list.innerHTML = `
            <li><span class="icon">🏷</span><span class="label">品牌</span><span class="value">${escapeHtml(r.brand || '—')}</span></li>
            <li><span class="icon">📏</span><span class="label">尺码</span><span class="value">${escapeHtml(r.orderNo || '—')}</span></li>
            <li><span class="icon">渠</span><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></li>
            <li><span class="icon">♥</span><span class="label">状态</span><span class="value">${r.status}</span></li>
            <li class="wide payment-detail-row"><span class="icon">票</span><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></li>
            <li><span class="icon">¥</span><span class="label">合计</span><span class="value price">¥${totalAmount(r).toFixed(2)}</span></li>
            <li><span class="icon">日</span><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>
            <li><span class="icon">N</span><span class="label">数量</span><span class="value">${r.quantity}</span></li>
            <li><span class="icon">记</span><span class="label">备注</span><span class="value">${note}</span></li>
        `;
""",
]


NEW_LIST = """        list.innerHTML = `
            <li class="detail-calm-head">
                <span class="detail-calm-price">¥${totalAmount(r).toFixed(2)}</span>
                <span class="detail-calm-status">${escapeHtml(r.status || '—')}</span>
            </li>
            <li class="detail-calm-meta">${escapeHtml(r.brand || '未填品牌')} · ${escapeHtml(r.orderNo || '未填尺码')} · ${r.quantity || 1}件</li>
            <li class="detail-calm-panel">
                <div class="detail-calm-row"><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></div>
                <div class="detail-calm-row payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></div>
                ${r.date ? `<div class="detail-calm-row"><span class="label">日期</span><span class="value">${escapeHtml(r.date)}</span></div>` : ''}
                <div class="detail-calm-row"><span class="label">备注</span><span class="value">${note}</span></div>
            </li>
        `;
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail calm sheet" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if NEW_LIST not in html:
        for old in OLD_LISTS:
            if old in html:
                html = html.replace(old, NEW_LIST, 1)
                break
        else:
            raise SystemExit("未找到详情字段渲染代码，未修改。")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
