from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-dark-sort-theme-button"


CSS_PATCH = """
        /* github patch: dark payment, sort height, theme button */
        .header-actions {
            flex: 0 0 auto;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 2px;
        }
        .header-theme-btn {
            width: 34px;
            height: 34px;
            border: none;
            border-radius: 999px;
            background: #fff;
            color: #ff4fa8;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 6px 14px rgba(255, 105, 180, 0.16);
        }
        body.dark .header-theme-btn {
            background: #2a2028;
            color: #ff8bc8;
            box-shadow: none;
        }
        body.dark .detail-modal .payment-chip .amount,
        body.dark .detail-modal .payment-detail-row .detail-value,
        body.dark .detail-modal .detail-payment-only .detail-value {
            color: #ff8bc8 !important;
        }
        body.dark .detail-modal .payment-chip {
            background: #3a2433 !important;
            color: #ffc3df !important;
        }
        .sort-modal-content {
            max-height: min(90vh, 760px) !important;
        }
        .sort-list {
            flex: 1 1 auto !important;
            min-height: 0 !important;
            max-height: none !important;
            padding-bottom: 12px !important;
            overscroll-behavior: contain;
        }
        .sort-modal-content .modal-footer {
            flex: 0 0 auto !important;
        }
"""


OLD_HEADER_BUTTON = """        <button class="header-sort-btn" type="button" onclick="openSortModal()">排序</button>
"""


NEW_HEADER_BUTTONS = """        <div class="header-actions">
            <button class="header-theme-btn" id="themeToggle" type="button" onclick="toggleTheme()" title="切换模式">☾</button>
            <button class="header-sort-btn" type="button" onclick="openSortModal()">排序</button>
        </div>
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: dark payment, sort height, theme button" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    if "class=\"header-actions\"" not in html:
        if OLD_HEADER_BUTTON not in html:
            raise SystemExit("未找到头部排序按钮，未修改。")
        html = html.replace(OLD_HEADER_BUTTON, NEW_HEADER_BUTTONS, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
