from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-detail-compact"


CSS_PATCH = '''
        /* github patch: compact detail modal */
        .modal-content.detail-modal {
            width: min(92vw, 520px) !important;
            max-width: 520px !important;
            padding: 18px !important;
            border-radius: 24px !important;
        }
        .detail-modal .modal-header h3 {
            font-size: 21px !important;
        }
        .detail-modal .modal-header .close-btn {
            width: 30px !important;
            height: 30px !important;
            font-size: 15px !important;
        }
        .detail-modal .detail-img-area {
            width: min(72%, 240px) !important;
            height: 220px !important;
            flex: 0 0 220px !important;
            align-self: center !important;
            border-radius: 18px !important;
            margin-bottom: 10px !important;
        }
        .detail-modal .detail-title {
            font-size: 18px !important;
            font-weight: 800 !important;
            line-height: 1.22 !important;
            margin-bottom: 10px !important;
            -webkit-line-clamp: 1 !important;
        }
        .detail-modal .detail-list {
            gap: 7px !important;
        }
        .detail-modal .detail-list li {
            min-height: 38px !important;
            padding: 7px 8px !important;
            border-radius: 12px !important;
            font-size: 12px !important;
        }
        .detail-modal .detail-list li .icon {
            width: 18px !important;
            height: 18px !important;
            font-size: 11px !important;
        }
        .detail-modal .detail-list li .label {
            font-size: 11px !important;
        }
        .detail-modal .detail-list li .value {
            font-size: 12.5px !important;
            font-weight: 700 !important;
        }
        .detail-modal .payment-chip {
            padding: 3px 6px !important;
            font-size: 10px !important;
        }
        .detail-modal .detail-actions {
            margin-top: 9px !important;
            padding-top: 6px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 40px !important;
            padding: 9px !important;
            border-radius: 13px !important;
            font-size: 14px !important;
            font-weight: 700 !important;
        }
        @media (max-width: 400px) {
            .modal-content.detail-modal {
                width: min(100%, 384px) !important;
                padding: 16px !important;
            }
            .detail-modal .detail-img-area {
                width: min(72%, 220px) !important;
                height: 200px !important;
                flex-basis: 200px !important;
            }
            .detail-modal .detail-title {
                font-size: 17px !important;
            }
            .detail-modal .detail-list li {
                min-height: 36px !important;
                padding: 6px 7px !important;
                font-size: 11px !important;
            }
        }
'''


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    html = html.replace("20260728-v1-form-detail-polish", VERSION_TO)
    if "github patch: compact detail modal" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>")
    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
