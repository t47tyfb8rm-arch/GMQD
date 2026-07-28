from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-single-line-compact"


CSS_PATCH = """
        /* github patch: detail single line compact */
        .modal-content.detail-modal {
            width: min(88vw, 390px) !important;
            max-height: 82vh !important;
            padding: 16px 16px 14px !important;
        }
        .detail-modal .modal-header {
            margin-bottom: 8px !important;
        }
        .detail-modal .modal-header h3 {
            font-size: 21px !important;
        }
        .detail-modal .detail-img-area {
            width: min(52vw, 210px) !important;
            height: min(31vh, 260px) !important;
            aspect-ratio: 3 / 4 !important;
            margin: 2px auto 10px !important;
            border-radius: 18px !important;
        }
        .detail-modal .detail-title {
            margin: 0 0 8px !important;
            font-size: 18px !important;
            line-height: 1.22 !important;
            text-align: center !important;
        }
        .detail-modal .detail-list {
            display: grid !important;
            grid-template-columns: 1fr !important;
            gap: 6px !important;
            margin-top: 6px !important;
        }
        .detail-modal .detail-list li,
        .detail-modal .detail-list li.wide,
        .detail-modal .detail-list li.payment-detail-row {
            grid-column: 1 / -1 !important;
            min-height: 34px !important;
            padding: 6px 9px !important;
            border-radius: 10px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            gap: 12px !important;
        }
        .detail-modal .detail-list li .icon {
            display: none !important;
        }
        .detail-modal .detail-list li .label {
            flex: 0 0 auto !important;
            font-size: 12px !important;
            color: #aaa1a7 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-list li .value {
            flex: 1 1 auto !important;
            min-width: 0 !important;
            text-align: right !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        .detail-modal .detail-list li .value.price {
            font-size: 15px !important;
            font-weight: 800 !important;
        }
        .detail-modal .payment-breakdown {
            justify-content: flex-end !important;
            flex-wrap: nowrap !important;
            gap: 5px !important;
            overflow: hidden !important;
        }
        .detail-modal .payment-chip {
            padding: 2px 6px !important;
            font-size: 11px !important;
            line-height: 1.35 !important;
            white-space: nowrap !important;
        }
        .detail-modal .detail-actions {
            margin-top: 10px !important;
            padding-top: 10px !important;
            gap: 8px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 40px !important;
            font-size: 15px !important;
            border-radius: 11px !important;
        }
        @media (max-width: 400px) {
            .modal-content.detail-modal {
                width: calc(100vw - 36px) !important;
                padding: 15px 15px 13px !important;
            }
            .detail-modal .detail-img-area {
                width: min(50vw, 190px) !important;
                height: min(28vh, 230px) !important;
            }
            .detail-modal .modal-header h3 {
                font-size: 20px !important;
            }
            .detail-modal .detail-title {
                font-size: 17px !important;
            }
        }
"""


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
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

    if "github patch: detail single line compact" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
