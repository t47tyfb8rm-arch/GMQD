# 部署说明

## FastAPI + SQLite 部署

本项目需要运行 FastAPI 后端，数据保存在 SQLite 数据库中。

## 安装依赖

```bash
cd /opt/purchase-system
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

## 启动

```bash
cd /opt/purchase-system
source venv/bin/activate
HOST=0.0.0.0 PORT=8080 ./start.sh
```

后台启动：

```bash
cd /opt/purchase-system
source venv/bin/activate
nohup ./start.sh > server.log 2>&1 &
```

健康检查：

```bash
curl http://127.0.0.1:8080/api/health
```

## 更新代码

覆盖新版文件后，重启后端：

```bash
ps -ef | grep uvicorn
kill <PID>
cd /opt/purchase-system
source venv/bin/activate
nohup ./start.sh > server.log 2>&1 &
```

## 数据库

数据库位置：

```text
data/purchase_records.sqlite3
```

升级前建议备份：

```bash
cp data/purchase_records.sqlite3 data/purchase_records.sqlite3.bak-$(date +%Y%m%d-%H%M%S)
```

## 检查项

- 页面能正常打开
- 中文不乱码
- 新增记录后刷新页面仍保留
- 删除记录后刷新页面不恢复
- `data/purchase_records.sqlite3` 文件存在且时间会更新
- 不要把密钥、token、服务器账号密码放进仓库
