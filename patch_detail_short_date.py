from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-detail-short-date"


HELPER = """

    // github patch: detail short date
    function detailShortDate(value) {
        const text = String(value || '').trim();
        const match = text.match(/^(\\d{4})-(\\d{1,2})-(\\d{1,2})$/);
        if (!match) return text || '—';
        return `${match[2].padStart(2, '0')}-${match[3].padStart(2, '0')}`;
    }
"""


DATE_REPLACEMENTS = (
    (
        """<div class="detail-mini-card"><span class="detail-label">日期</span><span class="detail-value">${escapeHtml(r.date || '—')}</span></div>""",
        """<div class="detail-mini-card"><span class="detail-label">日期</span><span class="detail-value">${escapeHtml(detailShortDate(r.date))}</span></div>""",
    ),
    (
        """<li><span class="icon">日</span><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>""",
        """<li><span class="icon">日</span><span class="label">日期</span><span class="value">${escapeHtml(detailShortDate(r.date))}</span></li>""",
    ),
    (
        """<li><span class="label">日期</span><span class="value">${escapeHtml(r.date || '—')}</span></li>""",
        """<li><span class="label">日期</span><span class="value">${escapeHtml(detailShortDate(r.date))}</span></li>""",
    ),
)


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260729-v1-sort-images-detail-fields",
        "20260729-v1-sort-scroll-guard",
        "20260729-v1-dark-sort-theme-button",
        "20260728-v1-swipe-tabs-page-slide",
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

    if "function detailShortDate" not in html:
        marker = "    function quickEdit(event, id) {"
        if marker not in html:
            raise SystemExit("未找到详情函数插入位置，未修改。")
        html = html.replace(marker, HELPER + "\n" + marker, 1)

    if "detailShortDate(r.date)" not in html:
        for old, new in DATE_REPLACEMENTS:
            if old in html:
                html = html.replace(old, new, 1)
                break
        else:
            raise SystemExit("未找到详情日期字段，未修改。")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
