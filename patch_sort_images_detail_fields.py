from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-sort-images-detail-fields"


CSS_PATCH = """
        /* github patch: sort images and detail fields */
        .detail-modal .detail-row-3 .detail-mini-card {
            min-height: 38px !important;
            display: flex !important;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: space-between !important;
            gap: 7px !important;
        }
        .detail-modal .detail-row-3 .detail-label {
            flex: 0 0 auto !important;
            font-size: 11px !important;
            font-weight: 400 !important;
            color: #aaa0a7 !important;
        }
        .detail-modal .detail-row-3 .detail-value {
            flex: 1 1 auto !important;
            width: auto !important;
            min-width: 0 !important;
            text-align: right !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;
        }
        .sort-thumb {
            object-fit: cover !important;
        }
"""


OLD_SORT_FN_HEAD = """    function renderSortList() {
        const list = document.getElementById('sortList');
        if (!sortDraftRecords.length) {
            list.innerHTML = '<div class="sort-empty">暂无订单可以排序</div>';
            return;
        }
        list.innerHTML = sortDraftRecords.map((r, index) => `
"""


NEW_SORT_FN_HEAD = """    function renderSortList() {
        const list = document.getElementById('sortList');
        if (!sortDraftRecords.length) {
            list.innerHTML = '<div class="sort-empty">暂无订单可以排序</div>';
            return;
        }
        const sortImageSrc = (r) => r.imageData || r.imageUrl || (r.hasImage ? `/api/records/${r.id}/image` : '');
        list.innerHTML = sortDraftRecords.map((r, index) => `
"""


OLD_SORT_IMAGE = """                ${r.imageData
                    ? `<img class="sort-thumb" src="${r.imageData}" alt="${escapeHtml(r.name)}">`
                    : '<div class="sort-thumb sort-placeholder">🛍</div>'}
"""


NEW_SORT_IMAGE = """                ${sortImageSrc(r)
                    ? `<img class="sort-thumb" src="${sortImageSrc(r)}" alt="${escapeHtml(r.name)}" loading="lazy" onerror="this.outerHTML='<div class=&quot;sort-thumb sort-placeholder&quot;>🛍</div>'">`
                    : '<div class="sort-thumb sort-placeholder">🛍</div>'}
"""


def replace_once(html: str, old: str, new: str, label: str) -> str:
    if new in html:
        return html
    if old not in html:
        raise SystemExit(f"未找到{label}，未修改。")
    return html.replace(old, new, 1)


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260729-v1-sort-scroll-guard",
        "20260729-v1-dark-sort-theme-button",
        "20260728-v1-swipe-tabs-page-slide",
        "20260728-v1-swipe-tabs-drawer-animation",
        "20260728-v1-swipe-tabs-animation-bolder",
        "20260728-v1-swipe-tabs-animation-stronger",
        "20260728-v1-swipe-tabs-animation",
        "20260728-v1-swipe-tabs-strong",
        "20260728-v1-detail-payment-value-right",
        "20260728-v1-detail-note-full-width",
        "20260728-v1-detail-payment-full-width",
        "20260728-v1-detail-payment-spacing",
        "20260728-v1-detail-remove-total",
        "20260728-v1-detail-vertical-photo-light-text",
        "20260728-v1-detail-exact-three-row",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: sort images and detail fields" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    html = replace_once(html, OLD_SORT_FN_HEAD, NEW_SORT_FN_HEAD, "排序列表图片函数")
    html = replace_once(html, OLD_SORT_IMAGE, NEW_SORT_IMAGE, "排序缩略图渲染")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
