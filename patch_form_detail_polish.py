from pathlib import Path


TARGET = Path("index.html")
VERSION_FROM = "20260728-v1-form-modal-polish"
VERSION_TO = "20260728-v1-form-detail-polish"


FORM_BLOCK = '''            <div class="form-row single-row name-row">
                <div class="form-group">
                    <label>商品名称 *</label>
                    <input type="text" id="formName" required placeholder="输入商品名称">
                </div>
            </div>
            <div class="form-row single-row platform-row">
                <div class="form-group">
                    <label>购买平台</label>
                    <input type="hidden" id="formPlatform" value="">
                    <select id="formPlatformSelect" onchange="handlePlatformSelectChange()">
                        <option value="">选择</option>
                        <option value="淘宝">淘宝</option>
                        <option value="京东">京东</option>
                        <option value="微信群">微信群</option>
                        <option value="__custom__">自定义</option>
                    </select>
                    <input class="platform-custom-input" type="text" id="formPlatformCustom" placeholder="输入平台" oninput="syncPlatformValue()">
                </div>
            </div>
            <div class="form-row two-col">
                <div class="form-group">
                    <label>品牌</label>
                    <input type="hidden" id="formBrand" value="">
                    <select id="formBrandSelect" onchange="handleBrandSelectChange()">
                        <option value="">选择</option>
                        <option value="梨涡">梨涡</option>
                        <option value="小满">小满</option>
                        <option value="圆点">圆点</option>
                        <option value="娃丽比">娃丽比</option>
                        <option value="澳泷哩">澳泷哩</option>
                        <option value="balabala">balabala</option>
                        <option value="__custom__">自定义</option>
                    </select>
                    <input class="brand-custom-input" type="text" id="formBrandCustom" placeholder="输入品牌" oninput="syncBrandValue()">
                </div>
                <div class="form-group">
                    <label>购买日期</label>
                    <input type="date" id="formDate">
                </div>
            </div>
'''


CSS_PATCH = '''
        /* github patch: form/detail polish */
        .form-modal-content .form-row.single-row {
            grid-template-columns: 1fr !important;
        }
        .form-modal-content .single-row > .form-group {
            min-height: 54px !important;
        }
        .form-modal-content .single-row input,
        .form-modal-content .single-row select {
            text-align: left !important;
            font-size: 15px !important;
            font-weight: 700 !important;
        }
        .modal-content.detail-modal {
            width: min(94vw, 560px) !important;
            max-width: 560px !important;
            padding: 20px !important;
            border-radius: 28px !important;
        }
        .detail-modal .detail-img-area {
            width: 100% !important;
            height: min(44vh, 300px) !important;
            flex: 0 0 min(44vh, 300px) !important;
            border-radius: 22px !important;
            margin-bottom: 14px !important;
        }
        .detail-modal .detail-title {
            font-size: 22px !important;
            font-weight: 900 !important;
            white-space: normal !important;
            margin-bottom: 12px !important;
        }
        .detail-modal .detail-list li {
            min-height: 48px !important;
            padding: 10px 11px !important;
            border-radius: 16px !important;
            font-size: 13px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 46px !important;
            border-radius: 16px !important;
            font-size: 16px !important;
            font-weight: 800 !important;
        }
'''


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    html = html.replace(VERSION_FROM, VERSION_TO)

    if "single-row name-row" not in html:
        start = html.find(
            '            <div class="form-row two-col">\\n'
            '                <div class="form-group">\\n'
            '                    <label>商品名称 *'
        )
        end = html.find('            <div class="form-row item-row">', start)
        if start == -1 or end == -1:
            raise SystemExit("未找到表单字段位置，未修改。")
        html = html[:start] + FORM_BLOCK + html[end:]

    if "github patch: form/detail polish" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
