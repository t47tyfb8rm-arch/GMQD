from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260728-v1-platform-custom-default"


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")
    html = html.replace("20260728-v1-form-detail-smaller", VERSION_TO)
    html = html.replace("20260728-v1-form-detail-refine", VERSION_TO)
    html = html.replace("20260728-v1-form-detail-polish", VERSION_TO)

    old = "        setPlatformValue('');"
    new = "        setPlatformValue('__custom__');"
    if new not in html:
        if old not in html:
            raise SystemExit("未找到新增弹框平台默认值位置，未修改。")
        html = html.replace(old, new, 1)

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
