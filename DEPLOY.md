# 部署说明

## 静态部署

本项目只有一个 `index.html`，可以部署到任意静态 Web 服务。

推荐生产环境使用 Nginx 或 Caddy，不建议长期使用 `python -m http.server`。

## Nginx 示例

```nginx
server {
    listen 8080;
    server_name _;

    root /opt/gmqd;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
        charset utf-8;
    }

    add_header X-Content-Type-Options nosniff;
}
```

部署文件：

```bash
mkdir -p /opt/gmqd
cp index.html /opt/gmqd/index.html
```

重载 Nginx：

```bash
nginx -t
systemctl reload nginx
```

## Caddy 示例

```caddyfile
:8080 {
    root * /opt/gmqd
    file_server
    header Content-Type "text/html; charset=utf-8"
}
```

## 检查项

- 页面能正常打开
- 中文不乱码
- 新增记录后刷新页面仍保留
- 删除记录后刷新页面不恢复
- 不要把密钥、token、服务器账号密码放进仓库
