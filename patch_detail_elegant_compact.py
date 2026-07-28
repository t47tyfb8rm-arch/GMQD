from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-elegant-compact"


CSS_PATCH = """
        /* github patch: detail elegant compact */
        .modal-content.detail-modal {
            width: min(88vw, 380px) !important;
            max-height: 80vh !important;
            padding: 15px 16px 14px !important;
            border-radius: 24px !important;
            overflow-y: auto !important;
        }
        .detail-modal .modal-header {
            margin-bottom: 8px !important;
        }
        .detail-modal .modal-header h3 {
            font-size: 20px !important;
            font-weight: 800 !important;
            letter-spacing: 0 !important;
        }
        .detail-modal .modal-header .close-btn {
            width: 34px !important;
            height: 34px !important;
            font-size: 20px !important;
        }
        .detail-modal .detail-img-area {
            width: 148px !important;
            height: 148px !important;
            aspect-ratio: 1 / 1 !important;
            margin: 2px auto 9px !important;
            border-radius: 19px !important;
            background: #fff7fb !important;
            box-shadow: 0 8px 22px rgba(235, 88, 158, .10) !important;
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
            margin: 0 0 10px !important;
            font-size: 18px !important;
            line-height: 1.25 !important;
            font-weight: 800 !important;
            text-align: center !important;
            color: #241f23 !important;
            text-shadow: none !important;
        }
        .detail-modal .detail-list {
            display: block !important;
            margin: 0 !important;
            padding: 4px 12px !important;
            border-radius: 16px !important;
            background: #fffafc !important;
            border: 1px solid #f1e4eb !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,.8) !important;
        }
        .detail-modal .detail-list li,
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            min-height: 32px !important;
            padding: 7px 0 !important;
            border: 0 !important;
            border-bottom: 1px solid #f1e6ec !important;
            border-radius: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            gap: 14px !important;
        }
        .detail-modal .detail-list li:last-child {
            border-bottom: 0 !important;
        }
        .detail-modal .detail-list li .icon {
            display: none !important;
        }
        .detail-modal .detail-list li .label {
            flex: 0 0 auto !important;
            font-size: 12px !important;
            font-weight: 500 !important;
            color: #aaa0a7 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list li .value {
            flex: 1 1 auto !important;
            min-width: 0 !important;
            text-align: right !important;
            font-size: 14px !important;
            line-height: 1.25 !important;
            font-weight: 650 !important;
            color: #282228 !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list li .value.price {
            color: #f052a3 !important;
            font-size: 17px !important;
            font-weight: 850 !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            flex-wrap: nowrap !important;
            gap: 5px !important;
            overflow: hidden !important;
        }
        .detail-modal .payment-chip {
            padding: 2px 7px !important;
            border-radius: 999px !important;
            font-size: 12px !important;
            line-height: 1.35 !important;
            background: #fff0f7 !important;
            white-space: nowrap !important;
        }
        .detail-modal .payment-chip .amount {
            font-weight: 800 !important;
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
        .detail-modal .detail-actions .btn-delete {
            background: #fff4f7 !important;
        }
        body.dark .detail-modal .detail-title {
            color: #fff7fb !important;
        }
        body.dark .detail-modal .detail-list {
            background: #231e23 !important;
            border-color: rgba(255,255,255,.08) !important;
        }
        body.dark .detail-modal .detail-list li {
            border-bottom-color: rgba(255,255,255,.08) !important;
        }
        body.dark .detail-modal .detail-list li .value {
            color: #fff7fb !important;
        }
        @media (max-width: 400px) {
            .modal-content.detail-modal {
                width: calc(100vw - 36px) !important;
                padding: 14px 15px 13px !important;
            }
            .detail-modal .detail-img-area {
                width: 136px !important;
                height: 136px !important;
            }
            .detail-modal .detail-title {
                font-size: 17px !important;
            }
            .detail-modal .detail-list li,
            .detail-modal .detail-list li.wide,
            .detail-modal .detail-list li.payment-detail-row {
                min-height: 30px !important;
                padding: 6px 0 !important;
            }
        }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail elegant compact" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
