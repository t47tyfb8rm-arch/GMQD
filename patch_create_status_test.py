from pathlib import Path


TARGET = Path("status-test.html")


HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#111827">
    <title>状态栏测试</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        html {
            min-height: 100%;
            background: #111827;
        }
        body {
            min-height: 100vh;
            min-height: 100dvh;
            padding-top: env(safe-area-inset-top);
            padding-bottom: env(safe-area-inset-bottom);
            background:
                radial-gradient(circle at 14% -8%, rgba(255, 105, 180, .22), transparent 34%),
                linear-gradient(180deg, #111827 0%, #151827 48%, #0f1118 100%);
            color: #fff;
            font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", Arial, sans-serif;
        }
        .app-top {
            position: sticky;
            top: env(safe-area-inset-top);
            padding: 18px 18px 14px;
            background: #111827;
            border-bottom: 1px solid rgba(255,255,255,.08);
        }
        .title {
            font-size: 26px;
            font-weight: 800;
            line-height: 1.2;
        }
        .sub {
            margin-top: 8px;
            color: rgba(255,255,255,.62);
            font-size: 14px;
            line-height: 1.5;
        }
        .card {
            margin: 18px;
            padding: 18px;
            border-radius: 18px;
            background: rgba(255,255,255,.08);
            border: 1px solid rgba(255,255,255,.08);
        }
        button {
            width: 100%;
            height: 46px;
            margin-top: 16px;
            border: 0;
            border-radius: 23px;
            background: #ff69b4;
            color: #fff;
            font-size: 16px;
            font-weight: 700;
        }
        body.light,
        body.light html {
            background: #fff7fa;
        }
        body.light {
            background: linear-gradient(180deg, #fff7fa 0%, #fff 100%);
            color: #111;
        }
        body.light .app-top {
            background: #fff7fa;
            border-bottom-color: rgba(222,186,199,.32);
        }
        body.light .sub { color: #7f747b; }
        body.light .card {
            background: #fff;
            border-color: rgba(222,186,199,.28);
            color: #111;
        }
    </style>
</head>
<body>
    <div class="app-top">
        <div class="title">状态栏测试</div>
        <div class="sub">这个页面不加载业务代码，只测试 iPhone 顶部颜色。</div>
    </div>
    <div class="card">
        <p>如果顶部状态栏能变深，说明环境支持，问题在柜子页面。</p>
        <p style="margin-top:10px;">如果这里也不变，说明当前浏览器/主屏幕环境不吃这类网页控制。</p>
        <button onclick="toggleMode()">切换深浅</button>
    </div>
    <script>
        function setMode(isLight) {
            document.body.classList.toggle('light', isLight);
            const color = isLight ? '#fff7fa' : '#111827';
            document.documentElement.style.backgroundColor = color;
            document.body.style.backgroundColor = color;
            document.querySelector('meta[name="theme-color"]').setAttribute('content', color);
        }
        function toggleMode() {
            setMode(!document.body.classList.contains('light'));
        }
        setMode(false);
    </script>
</body>
</html>
"""


def main() -> None:
    TARGET.write_text(HTML, encoding="utf-8")
    print(f"OK: wrote {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
