from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-form-detail-smaller"


CSS_PATCH = '''
        /* github patch: slightly smaller form/detail modal */
        .modal-content.form-modal-content {
            width: min(90vw, 500px) !important;
            max-width: 500px !important;
            padding: 16px 16px 14px !important;
            border-radius: 22px !important;
        }
        .form-modal-content .modal-header {
            margin-bottom: 10px !important;
        }
        .form-modal-content .modal-header h3 {
            font-size: 21px !important;
        }
        .form-modal-content > form > .form-group:first-of-type {
            padding: 9px !important;
            margin-bottom: 9px !important;
        }
        .form-modal-content .image-uploader {
            grid-template-columns: 58px 1fr !important;
            gap: 10px !important;
        }
        .form-modal-content .image-preview {
            width: 58px !important;
            height: 58px !important;
            border-radius: 13px !important;
            font-size: 22px !important;
        }
        .form-modal-content .image-actions label,
        .form-modal-content .image-actions button {
            min-height: 30px !important;
            padding: 7px 11px !important;
            font-size: 12px !important;
        }
        .form-modal-content .form-row {
            gap: 7px !important;
        }
        .form-modal-content .form-row > .form-group {
            min-height: 42px !important;
            padding: 6px 9px !important;
            margin-bottom: 6px !important;
            border-radius: 13px !important;
        }
        .form-modal-content .single-row > .form-group {
            min-height: 45px !important;
        }
        .form-modal-content .form-row > .form-group label {
            font-size: 11px !important;
        }
        .form-modal-content .form-row > .form-group input,
        .form-modal-content .form-row > .form-group select {
            height: 25px !important;
            min-height: 25px !important;
            font-size: 13.5px !important;
        }
        .form-modal-content .name-row > .form-group input {
            font-size: 14.5px !important;
        }
        .form-modal-content .payment-summary-box {
            min-height: 42px !important;
            padding: 7px 9px !important;
            border-radius: 13px !important;
        }
        .form-modal-content .payment-summary-text {
            font-size: 13px !important;
        }
        .form-modal-content .payment-summary-box button {
            min-height: 30px !important;
            padding: 7px 11px !important;
            font-size: 12px !important;
        }
        .form-modal-content .form-group .radio-group label {
            padding: 6px 11px !important;
            font-size: 12px !important;
        }
        .form-modal-content textarea#formNote {
            min-height: 44px !important;
            height: 44px !important;
            border-radius: 13px !important;
        }
        .form-modal-content .modal-footer {
            margin-top: 8px !important;
        }
        .form-modal-content .modal-footer button {
            min-height: 40px !important;
            padding: 10px !important;
            border-radius: 13px !important;
            font-size: 14px !important;
        }

        .modal-content.detail-modal {
            width: min(90vw, 490px) !important;
            max-width: 490px !important;
            padding: 15px !important;
            border-radius: 22px !important;
        }
        .detail-modal .detail-img-area {
            width: min(64%, 205px) !important;
            height: 186px !important;
            flex: 0 0 186px !important;
            border-radius: 18px !important;
            margin-bottom: 9px !important;
        }
        .detail-modal .detail-title {
            font-size: 17px !important;
            margin-bottom: 8px !important;
        }
        .detail-modal .detail-list {
            gap: 6px !important;
        }
        .detail-modal .detail-list li {
            min-height: 34px !important;
            padding: 6px 7px !important;
            border-radius: 12px !important;
        }
        .detail-modal .detail-actions button {
            min-height: 38px !important;
            font-size: 13px !important;
        }
        @media (max-width: 400px) {
            .modal-content.form-modal-content,
            .modal-content.detail-modal {
                width: min(100%, 366px) !important;
            }
        }
'''


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    for old in (
        "20260728-v1-form-detail-refine",
        "20260728-v1-form-detail-polish",
        "20260728-v1-detail-compact",
        "20260728-v1-form-modal-polish",
    ):
        html = html.replace(old, VERSION_TO)
    if "github patch: slightly smaller form/detail modal" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>")
    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
