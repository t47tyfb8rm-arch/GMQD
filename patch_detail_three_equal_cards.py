from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-three-equal-cards"


CSS_PATCH = """
        /* github patch: detail three equal cards */
        .modal-content.detail-modal {
            width: min(90vw, 400px) !important;
            max-height: 84vh !important;
            padding: 14px 16px 14px !important;
            border-radius: 24px !important;
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important;
        }
        .detail-modal .modal-header {
            flex: 0 0 auto !important;
            margin-bottom: 8px !important;
        }
        .detail-modal .detail-img-area {
            flex: 0 0 auto !important;
            width: 100% !important;
            height: min(22vh, 142px) !important;
            margin: 0 0 9px !important;
            border-radius: 16px !important;
            overflow: hidden !important;
            box-shadow: none !important;
        }
        .detail-modal .detail-img-area img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
        }
        .detail-modal .detail-title {
            flex: 0 0 auto !important;
            margin: 0 0 9px !important;
            font-size: 18px !important;
            line-height: 1.25 !important;
            font-weight: 850 !important;
            text-align: left !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list {
            flex: 1 1 auto !important;
            min-height: 0 !important;
            overflow-y: auto !important;
            display: grid !important;
            grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
            align-content: start !important;
            gap: 7px !important;
            margin: 0 0 10px !important;
            padding: 0 1px 0 0 !important;
            background: transparent !important;
            border: 0 !important;
            box-shadow: none !important;
        }
        .detail-modal .detail-list::-webkit-scrollbar {
            width: 0 !important;
            height: 0 !important;
        }
        .detail-modal .detail-list li {
            min-width: 0 !important;
            min-height: 42px !important;
            padding: 7px 8px !important;
            border-radius: 12px !important;
            background: #fff !important;
            border: 1px solid #f1e5ec !important;
            box-shadow: none !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            justify-content: center !important;
            gap: 4px !important;
        }
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            grid-column: 1 / -1 !important;
            min-height: 40px !important;
            display: grid !important;
            grid-template-columns: 46px minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 10px !important;
        }
        .detail-modal .detail-list .icon {
            display: none !important;
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
            line-height: 1.2 !important;
            font-weight: 750 !important;
            text-align: left !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list li.wide .label,
        .detail-modal .detail-list li.payment-detail-row .label {
            font-size: 12px !important;
        }
        .detail-modal .detail-list li.wide .value,
        .detail-modal .detail-list li.payment-detail-row .value {
            text-align: right !important;
            font-size: 13px !important;
        }
        .detail-modal .detail-list .value.price {
            color: #f052a3 !important;
            font-size: 15px !important;
            font-weight: 900 !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            flex-wrap: wrap !important;
            gap: 5px !important;
        }
        .detail-modal .payment-chip {
            padding: 2px 7px !important;
            border-radius: 999px !important;
            background: #fff0f7 !important;
            font-size: 12px !important;
            line-height: 1.35 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-actions {
            position: static !important;
            inset: auto !important;
            transform: none !important;
            z-index: auto !important;
            flex: 0 0 auto !important;
            margin: 0 !important;
            padding: 0 !important;
            border: 0 !important;
            background: transparent !important;
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: 9px !important;
        }
        .detail-modal .detail-actions button {
            position: static !important;
            min-height: 42px !important;
            border-radius: 13px !important;
            font-size: 15px !important;
            font-weight: 750 !important;
        }
        body.dark .detail-modal .detail-list .value {
            color: #fff7fb !important;
        }
        body.dark .detail-modal .detail-list li {
            background: #231e23 !important;
            border-color: rgba(255,255,255,.08) !important;
        }
        @media (max-width: 400px) {
            .modal-content.detail-modal {
                width: calc(100vw - 34px) !important;
                padding: 13px 14px !important;
            }
            .detail-modal .detail-img-area {
                height: min(20vh, 124px) !important;
            }
            .detail-modal .detail-title {
                font-size: 17px !important;
            }
            .detail-modal .detail-list {
                gap: 6px !important;
            }
            .detail-modal .detail-list li {
                min-height: 40px !important;
                padding: 6px 7px !important;
            }
        }
"""


NEW_OPEN_DETAIL = r"""    function openDetail(id) {
        const r = records.find(x => x.id == id);
        if (!r) return;
        if (r.hasImage && !r.imageData) {
            loadFullRecordForDetail(id);
        }
        currentDetailId = r.id;
        document.getElementById('detailTitle').textContent = r.name;
        const detailImage = document.querySelector('.detail-img-area');
        detailImage.classList.toggle('has-image', !!r.imageData);
        detailImage.innerHTML = r.imageData ? `<img src="${r.imageData}" alt="${escapeHtml(r.name)}">` : '🛍';
        detailImage.onclick = r.imageData ? () => openImageViewer(r.imageData, r.name) : null;

        const list = document.getElementById('detailList');
        const noteHtml = r.note ? `<li class="wide"><span class="label">备注</span><span class="value">${escapeHtml(r.note)}</span></li>` : '';
        list.innerHTML = `
            <li><span class="label">品牌</span><span class="value">${escapeHtml(r.brand || '—')}</span></li>
            <li><span class="label">尺码</span><span class="value">${escapeHtml(r.orderNo || '—')}</span></li>
            <li><span class="label">数量</span><span class="value">${r.quantity || 1}</span></li>
            <li><span class="label">状态</span><span class="value">${escapeHtml(r.status || '—')}</span></li>
            <li><span class="label">渠道</span><span class="value">${escapeHtml(r.platform || '—')}</span></li>
            <li><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>
            <li class="wide payment-detail-row"><span class="label">付款</span><span class="value">${paymentDetailHtml(r)}</span></li>
            <li class="wide"><span class="label">合计</span><span class="value price">¥${totalAmount(r).toFixed(2)}</span></li>
            ${noteHtml}
        `;
        document.getElementById('detailModal').classList.add('active');
        // 20260728 three equal cards marker
    }
"""


def replace_open_detail(html: str) -> str:
    start = html.find("    function openDetail(id) {")
    if start < 0:
        raise SystemExit("未找到 openDetail 开始位置，未修改。")
    end = html.find("    async function loadFullRecordForDetail", start)
    if end < 0:
        raise SystemExit("未找到 openDetail 结束位置，未修改。")
    return html[:start] + NEW_OPEN_DETAIL + "\n\n" + html[end:]


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail three equal cards" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "20260728 three equal cards marker" not in html:
        html = replace_open_detail(html)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
