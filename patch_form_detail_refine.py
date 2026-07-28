from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-form-detail-refine"


CSS_PATCH = '''
        /* github patch: refine form size and detail style */
        .modal-content.form-modal-content {
            width: min(92vw, 520px) !important;
            max-width: 520px !important;
            padding: 18px 18px 16px !important;
            border-radius: 24px !important;
        }
        .form-modal-content .modal-header h3 {
            font-size: 22px !important;
        }
        .form-modal-content .modal-header .close-btn {
            width: 31px !important;
            height: 31px !important;
        }
        .form-modal-content > form > .form-group:first-of-type {
            padding: 10px !important;
            margin-bottom: 11px !important;
            border-radius: 16px !important;
        }
        .form-modal-content .image-uploader {
            grid-template-columns: 66px 1fr !important;
            gap: 12px !important;
        }
        .form-modal-content .image-preview {
            width: 66px !important;
            height: 66px !important;
            border-radius: 14px !important;
            font-size: 24px !important;
        }
        .form-modal-content .form-row > .form-group {
            min-height: 46px !important;
            padding: 7px 10px !important;
            margin-bottom: 7px !important;
            border-radius: 14px !important;
        }
        .form-modal-content .single-row > .form-group {
            min-height: 49px !important;
        }
        .form-modal-content .form-row > .form-group input,
        .form-modal-content .form-row > .form-group select {
            height: 27px !important;
            min-height: 27px !important;
            font-size: 14px !important;
        }
        .form-modal-content .name-row > .form-group input {
            font-size: 15px !important;
        }
        .form-modal-content .payment-summary-box {
            min-height: 46px !important;
            padding: 8px 10px !important;
            border-radius: 14px !important;
        }
        .form-modal-content textarea#formNote {
            min-height: 48px !important;
            height: 48px !important;
            border-radius: 14px !important;
        }
        .form-modal-content .modal-footer button {
            min-height: 42px !important;
            border-radius: 14px !important;
            font-size: 15px !important;
        }

        .modal-content.detail-modal {
            width: min(92vw, 510px) !important;
            max-width: 510px !important;
            padding: 17px !important;
            border-radius: 24px !important;
            background: linear-gradient(180deg, #ffffff, #fff8fb) !important;
            box-shadow: 0 20px 48px rgba(40, 26, 34, 0.15) !important;
        }
        body.dark .modal-content.detail-modal {
            background: linear-gradient(180deg, #231c22, #191417) !important;
        }
        .detail-modal .detail-img-area {
            width: min(68%, 220px) !important;
            height: 202px !important;
            flex: 0 0 202px !important;
            border-radius: 20px !important;
            background: linear-gradient(145deg, #fff6fa, #f8f6f8) !important;
            box-shadow: 0 10px 24px rgba(255, 105, 180, 0.10) !important;
        }
        .detail-modal .detail-title {
            font-size: 18px !important;
            font-weight: 850 !important;
            color: #211a1f !important;
            text-align: left !important;
        }
        .detail-modal .detail-list {
            gap: 8px !important;
        }
        .detail-modal .detail-list li {
            min-height: 38px !important;
            padding: 8px 9px !important;
            border: 1px solid rgba(255, 188, 218, 0.42) !important;
            border-radius: 14px !important;
            background: rgba(255, 250, 252, 0.86) !important;
            box-shadow: none !important;
        }
        body.dark .detail-modal .detail-list li {
            background: rgba(23, 18, 22, 0.92) !important;
            border-color: #332a31 !important;
        }
        .detail-modal .detail-list li .icon {
            background: transparent !important;
            color: #ef6fa8 !important;
            font-size: 12px !important;
        }
        .detail-modal .detail-list li .label {
            color: #a2969d !important;
            font-size: 11px !important;
        }
        .detail-modal .detail-list li .value {
            color: #2b2428 !important;
            font-size: 12.5px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 40px !important;
            border-radius: 14px !important;
            font-size: 14px !important;
        }
        .detail-modal .detail-actions .btn-edit {
            background: linear-gradient(135deg, #ff62ad, #ff88bf) !important;
        }
        .detail-modal .detail-actions .btn-delete {
            background: #fff1f5 !important;
            color: #e85b74 !important;
        }
        @media (max-width: 400px) {
            .modal-content.form-modal-content {
                width: min(100%, 378px) !important;
                padding: 16px 14px 14px !important;
            }
            .form-modal-content .image-uploader {
                grid-template-columns: 60px 1fr !important;
            }
            .form-modal-content .image-preview {
                width: 60px !important;
                height: 60px !important;
            }
            .modal-content.detail-modal {
                width: min(100%, 376px) !important;
                padding: 15px !important;
            }
            .detail-modal .detail-img-area {
                width: min(68%, 205px) !important;
                height: 188px !important;
                flex-basis: 188px !important;
            }
        }
'''


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    for old in (
        "20260728-v1-form-detail-polish",
        "20260728-v1-detail-compact",
        "20260728-v1-form-modal-polish",
    ):
        html = html.replace(old, VERSION_TO)
    if "github patch: refine form size and detail style" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>")
    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
