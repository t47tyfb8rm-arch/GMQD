from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-restore-full-grid"


CSS_PATCH = """
        /* github patch: detail restore full grid */
        .modal-content.detail-modal {
            width: min(92vw, 430px) !important;
            max-height: 86vh !important;
            padding: 18px 18px 16px !important;
            border-radius: 24px !important;
            overflow-y: auto !important;
        }
        .detail-modal .modal-header {
            margin-bottom: 12px !important;
        }
        .detail-modal .modal-header h3 {
            font-size: 22px !important;
            font-weight: 850 !important;
        }
        .detail-modal .modal-header .close-btn {
            width: 36px !important;
            height: 36px !important;
            font-size: 20px !important;
        }
        .detail-modal .detail-img-area {
            width: 100% !important;
            height: 170px !important;
            margin: 0 0 12px !important;
            border-radius: 16px !important;
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
            max-width: 100% !important;
            margin: 0 0 12px !important;
            color: #231f23 !important;
            font-size: 20px !important;
            font-weight: 850 !important;
            line-height: 1.25 !important;
            text-align: left !important;
            white-space: normal !important;
            overflow: visible !important;
            text-overflow: clip !important;
            text-shadow: none !important;
        }
        .detail-modal .detail-list {
            display: grid !important;
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
            gap: 8px !important;
            margin: 0 !important;
            padding: 0 !important;
            border: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        .detail-modal .detail-list li,
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            min-width: 0 !important;
            min-height: 42px !important;
            padding: 8px 10px !important;
            border-radius: 12px !important;
            background: #fff !important;
            border: 1px solid #f1e5ec !important;
            box-shadow: none !important;
            display: grid !important;
            grid-template-columns: auto auto minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 7px !important;
        }
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            grid-column: 1 / -1 !important;
        }
        .detail-modal .detail-list li .icon {
            display: inline-flex !important;
            width: 20px !important;
            min-width: 20px !important;
            height: 20px !important;
            align-items: center !important;
            justify-content: center !important;
            color: #b7aeb4 !important;
            background: transparent !important;
            font-size: 13px !important;
            font-weight: 700 !important;
        }
        .detail-modal .detail-list li .label {
            color: #aaa0a7 !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list li .value {
            min-width: 0 !important;
            color: #292429 !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            line-height: 1.25 !important;
            text-align: right !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list li .value.price {
            color: #f052a3 !important;
            font-size: 16px !important;
            font-weight: 850 !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            flex-wrap: wrap !important;
            gap: 5px !important;
            overflow: visible !important;
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
            margin-top: 12px !important;
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
        body.dark .detail-modal .detail-title,
        body.dark .detail-modal .detail-list li .value {
            color: #fff7fb !important;
        }
        body.dark .detail-modal .detail-list li {
            background: #231e23 !important;
            border-color: rgba(255,255,255,.08) !important;
        }
        @media (max-width: 400px) {
            .modal-content.detail-modal {
                width: calc(100vw - 36px) !important;
                padding: 16px 16px 14px !important;
            }
            .detail-modal .detail-img-area {
                height: 160px !important;
            }
            .detail-modal .detail-title {
                font-size: 19px !important;
            }
            .detail-modal .detail-list {
                gap: 7px !important;
            }
            .detail-modal .detail-list li,
            .detail-modal .detail-list li.wide,
            .detail-modal .detail-list li.payment-detail-row {
                min-height: 40px !important;
                padding: 7px 9px !important;
            }
            .detail-modal .detail-list li .label,
            .detail-modal .detail-list li .icon {
                font-size: 12px !important;
            }
            .detail-modal .detail-list li .value {
                font-size: 13px !important;
            }
        }
"""


OLD_START = "        list.innerHTML = `"
OLD_END = "        `;"


FULL_GRID_LIST = """        list.innerHTML = `
            <li><span class="icon">品</span><span class="label">品牌</span><span class="value">${escapeHtml(r.brand || '—')}</span></li>
            <li><span class="icon">码</span><span class="label">尺码</span><span class="value">${escapeHtml(r.orderNo || '—')}</span></li>
            <li><span class="icon">N</span><span class="label">数量</span><span class="value">${r.quantity || 1}</span></li>
            <li><span class="icon">态</span><span class="label">状态</span><span class="value">${escapeHtml(r.status || '—')}</span></li>
            <li class="wide"><span class="icon">渠</span><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></li>
            <li class="wide payment-detail-row"><span class="icon">付</span><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></li>
            <li><span class="icon">¥</span><span class="label">合计</span><span class="value price">¥${totalAmount(r).toFixed(2)}</span></li>
            <li><span class="icon">日</span><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>
            <li class="wide"><span class="icon">记</span><span class="label">备注</span><span class="value">${note}</span></li>
        `;
"""


def replace_detail_list(html: str) -> str:
    marker = "        const note = r.note ? escapeHtml(r.note) : '—';\n"
    start = html.find(marker)
    if start < 0:
        raise SystemExit("未找到详情备注位置，未修改。")
    list_start = html.find(OLD_START, start)
    if list_start < 0:
        raise SystemExit("未找到详情字段开始位置，未修改。")
    list_end = html.find(OLD_END, list_start)
    if list_end < 0:
        raise SystemExit("未找到详情字段结束位置，未修改。")
    list_end += len(OLD_END)
    return html[:list_start] + FULL_GRID_LIST + html[list_end:]


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail restore full grid" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if FULL_GRID_LIST not in html:
        html = replace_detail_list(html)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
