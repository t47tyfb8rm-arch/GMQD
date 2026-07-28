from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-hard-restore"


CSS_PATCH = """
        /* github patch: detail hard restore */
        .modal-content.detail-modal {
            width: min(92vw, 430px) !important;
            max-height: 86vh !important;
            padding: 18px !important;
            border-radius: 24px !important;
            overflow-y: auto !important;
        }
        .detail-modal .detail-img-area {
            width: 100% !important;
            height: 180px !important;
            margin: 0 0 12px !important;
            border-radius: 16px !important;
            background: #fff7fb !important;
            overflow: hidden !important;
            box-shadow: none !important;
        }
        .detail-modal .detail-img-area img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
        }
        .detail-modal .detail-title {
            margin: 0 0 12px !important;
            font-size: 20px !important;
            font-weight: 850 !important;
            line-height: 1.25 !important;
            text-align: left !important;
            white-space: normal !important;
        }
        .detail-modal .detail-list {
            display: grid !important;
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
            gap: 8px !important;
            margin: 0 0 12px !important;
            padding: 0 !important;
            background: transparent !important;
            border: 0 !important;
        }
        .detail-modal .detail-list li {
            min-width: 0 !important;
            min-height: 42px !important;
            padding: 8px 10px !important;
            border-radius: 12px !important;
            background: #fff !important;
            border: 1px solid #f1e5ec !important;
            box-shadow: none !important;
            display: grid !important;
            grid-template-columns: auto minmax(0, 1fr) !important;
            align-items: center !important;
            gap: 8px !important;
        }
        .detail-modal .detail-list li.wide {
            grid-column: 1 / -1 !important;
        }
        .detail-modal .detail-list .icon {
            display: none !important;
        }
        .detail-modal .detail-list .label {
            color: #aaa0a7 !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list .value {
            min-width: 0 !important;
            color: #292429 !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            text-align: right !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list .value.price {
            color: #f052a3 !important;
            font-size: 16px !important;
            font-weight: 850 !important;
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
            margin-top: 0 !important;
            padding-top: 0 !important;
            border-top: 0 !important;
            display: grid !important;
            grid-template-columns: 1fr 1fr !important;
            gap: 9px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 42px !important;
            border-radius: 13px !important;
            font-size: 15px !important;
            font-weight: 750 !important;
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
        const note = r.note ? escapeHtml(r.note) : '—';
        list.innerHTML = `
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
        document.getElementById('detailModal').classList.add('active');
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

    if "github patch: detail hard restore" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "20260728 hard restore marker" not in html:
        html = replace_open_detail(html)
        html = html.replace(
            "        document.getElementById('detailModal').classList.add('active');",
            "        document.getElementById('detailModal').classList.add('active');\n        // 20260728 hard restore marker",
            1,
        )

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
