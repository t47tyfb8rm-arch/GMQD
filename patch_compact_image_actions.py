from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-compact-image-actions"


CSS_PATCH = '''
        /* github patch: compact image upload actions */
        .form-modal-content > form > .form-group:first-of-type {
            padding: 7px 9px !important;
            margin-bottom: 7px !important;
        }
        .form-modal-content > form > .form-group:first-of-type > label {
            display: none !important;
        }
        .form-modal-content .image-uploader {
            grid-template-columns: 46px minmax(0, 1fr) !important;
            gap: 9px !important;
        }
        .form-modal-content .image-preview {
            width: 46px !important;
            height: 46px !important;
            border-radius: 12px !important;
            font-size: 19px !important;
        }
        .form-modal-content .image-actions {
            display: flex !important;
            align-items: center !important;
            gap: 7px !important;
            min-width: 0 !important;
        }
        .form-modal-content .image-actions label,
        .form-modal-content .image-actions button {
            min-height: 28px !important;
            padding: 6px 10px !important;
            border-radius: 999px !important;
            font-size: 12px !important;
            line-height: 1 !important;
            white-space: nowrap !important;
        }
        .form-modal-content .image-actions .btn-remove-image {
            color: #9b8f96 !important;
            background: #f7f4f6 !important;
        }
        @media (max-width: 400px) {
            .form-modal-content .image-uploader {
                grid-template-columns: 42px minmax(0, 1fr) !important;
                gap: 8px !important;
            }
            .form-modal-content .image-preview {
                width: 42px !important;
                height: 42px !important;
                font-size: 18px !important;
            }
            .form-modal-content .image-actions label,
            .form-modal-content .image-actions button {
                padding: 6px 9px !important;
                font-size: 11px !important;
            }
        }
'''


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    for old in (
        "20260728-v1-platform-custom-default",
        "20260728-v1-form-detail-smaller",
        "20260728-v1-form-detail-refine",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old, VERSION_TO)
    if "github patch: compact image upload actions" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>")
    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
