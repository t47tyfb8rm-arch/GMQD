from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-keep-image-clean"


CSS_PATCH = """
        /* github patch: detail keep image clean */
        .modal-content.detail-modal {
            padding: 18px 18px 16px !important;
        }
        .detail-modal .detail-img-area {
            width: min(62vw, 260px) !important;
            height: min(44vh, 340px) !important;
            aspect-ratio: 3 / 4 !important;
            margin: 4px auto 12px !important;
            border-radius: 22px !important;
            background: linear-gradient(180deg, #fff7fb 0%, #fff 100%) !important;
            box-shadow: 0 12px 30px rgba(225, 92, 150, .15) !important;
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
            margin: 2px 0 10px !important;
            font-size: 20px !important;
            line-height: 1.25 !important;
            text-align: center !important;
        }
        .detail-modal .detail-list {
            grid-template-columns: 1fr 1fr !important;
            gap: 8px !important;
            margin-top: 8px !important;
        }
        .detail-modal .detail-list li {
            min-height: 42px !important;
            padding: 8px 10px !important;
            border-radius: 12px !important;
            background: #fff !important;
            border: 1px solid #f1e7ed !important;
            box-shadow: none !important;
            display: grid !important;
            grid-template-columns: auto minmax(0, 1fr) !important;
            gap: 8px !important;
            align-items: center !important;
        }
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            grid-column: 1 / -1 !important;
        }
        .detail-modal .detail-list li .icon {
            display: none !important;
        }
        .detail-modal .detail-list li .label {
            color: #a9a0a6 !important;
            font-size: 13px !important;
            letter-spacing: 0 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list li .value {
            min-width: 0 !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            text-align: right !important;
            color: #262126 !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list li .value.price {
            color: #f25aa8 !important;
            font-size: 16px !important;
            font-weight: 800 !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            gap: 6px !important;
            overflow: hidden !important;
        }
        .detail-modal .payment-chip {
            padding: 3px 7px !important;
            border-radius: 999px !important;
            font-size: 12px !important;
        }
        .detail-modal .detail-actions {
            margin-top: 12px !important;
            padding-top: 12px !important;
        }
        body.dark .detail-modal .detail-list li {
            background: #251f24 !important;
            border-color: rgba(255,255,255,.08) !important;
        }
        body.dark .detail-modal .detail-list li .value {
            color: #fff7fb !important;
        }
        @media (max-width: 400px) {
            .detail-modal .detail-img-area {
                width: min(60vw, 230px) !important;
                height: min(38vh, 300px) !important;
                border-radius: 19px !important;
            }
            .detail-modal .detail-title {
                font-size: 19px !important;
            }
            .detail-modal .detail-list {
                gap: 7px !important;
            }
            .detail-modal .detail-list li {
                min-height: 39px !important;
                padding: 7px 9px !important;
            }
        }
"""


OLD_DETAIL_LIST = """        list.innerHTML = `
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
"""


NEW_DETAIL_LIST = """        list.innerHTML = `
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
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-swipe-tabs",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-platform-custom-default",
        "20260728-v1-form-detail-smaller",
        "20260728-v1-form-detail-refine",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: detail keep image clean" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if NEW_DETAIL_LIST not in html:
        if OLD_DETAIL_LIST not in html:
            raise SystemExit("未找到详情字段渲染代码，未修改。")
        html = html.replace(OLD_DETAIL_LIST, NEW_DETAIL_LIST, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
