from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-platform-custom-fallback"


def replace_once(html: str, old: str, new: str, label: str) -> str:
    if new in html:
        return html
    if old not in html:
        raise SystemExit(f"未找到{label}，未修改。")
    return html.replace(old, new, 1)


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260728-v1-compact-image-actions",
        "20260728-v1-platform-custom-default",
        "20260728-v1-form-detail-smaller",
        "20260728-v1-form-detail-refine",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    html = html.replace(
        'id="formPlatformCustom" placeholder="输入平台"',
        'id="formPlatformCustom" placeholder="可输入其他平台"',
    )

    html = html.replace(
        "        setPlatformValue('');",
        "        setPlatformValue('__custom__');",
        1,
    )

    old_set_platform = """    function setPlatformValue(value) {
        const platform = (value || '').trim();
        const select = document.getElementById('formPlatformSelect');
        const custom = document.getElementById('formPlatformCustom');
        if (!platform) {
            select.value = '';
            custom.value = '';
            custom.classList.remove('active');
        } else if (PLATFORM_OPTIONS.includes(platform)) {
            select.value = platform;
            custom.value = '';
            custom.classList.remove('active');
        } else {
            select.value = '__custom__';
            custom.value = platform;
            custom.classList.add('active');
        }
        syncPlatformValue();
    }
"""
    new_set_platform = """    function setPlatformValue(value) {
        const platform = (value || '').trim();
        const select = document.getElementById('formPlatformSelect');
        const custom = document.getElementById('formPlatformCustom');
        if (!platform || platform === '__custom__') {
            select.value = '__custom__';
            custom.value = '';
            custom.classList.add('active');
        } else if (PLATFORM_OPTIONS.includes(platform)) {
            select.value = platform;
            custom.value = '';
            custom.classList.remove('active');
        } else {
            select.value = '__custom__';
            custom.value = platform === '自定义' ? '' : platform;
            custom.classList.add('active');
        }
        syncPlatformValue();
    }
"""
    html = replace_once(html, old_set_platform, new_set_platform, "购买平台赋值逻辑")

    old_sync = """    function syncPlatformValue() {
        const selected = document.getElementById('formPlatformSelect').value;
        const custom = document.getElementById('formPlatformCustom').value.trim();
        document.getElementById('formPlatform').value = selected === '__custom__' ? custom : selected;
    }
"""
    new_sync = """    function syncPlatformValue() {
        const selected = document.getElementById('formPlatformSelect').value;
        const custom = document.getElementById('formPlatformCustom').value.trim();
        document.getElementById('formPlatform').value = selected === '__custom__' ? (custom || '自定义') : selected;
    }
"""
    html = replace_once(html, old_sync, new_sync, "购买平台同步逻辑")

    if "github patch: platform custom fallback" not in html:
        html = html.replace(
            "    </style>",
            "        /* github patch: platform custom fallback */\n"
            "        .form-modal-content .platform-custom-input.active:placeholder-shown {\n"
            "            color: #b8adb3;\n"
            "        }\n"
            "    </style>",
            1,
        )

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
