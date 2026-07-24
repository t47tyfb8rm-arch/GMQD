from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field


ROOT_DIR = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT_DIR / "index.html"
DATA_DIR = ROOT_DIR / "data"
DB_FILE = DATA_DIR / "purchase_records.sqlite3"


class RecordIn(BaseModel):
    name: str = Field(default="", max_length=300)
    brand: str = Field(default="", max_length=120)
    platform: str = Field(default="", max_length=120)
    orderNo: str = Field(default="", max_length=180)
    paymentType: str = Field(default="正常", max_length=40)
    hasShipping: bool = False
    price: float = 0
    depositAmount: float = 0
    balanceAmount: float = 0
    shippingAmount: float = 0
    quantity: int = 1
    status: str = Field(default="待付款", max_length=40)
    date: str = Field(default="", max_length=40)
    note: str = Field(default="", max_length=1000)
    imageData: str = ""


app = FastAPI(title="GMQD 购物清单")


def now_text() -> str:
    return datetime.now().isoformat(timespec="seconds")


def connect() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def row_to_record(row: sqlite3.Row) -> dict[str, Any]:
    deposit_amount = row["deposit_amount"] or 0
    balance_amount = row["balance_amount"] or 0
    shipping_amount = row["shipping_amount"] or 0
    price = row["price"] or 0
    total_amount = price or (deposit_amount + balance_amount + shipping_amount)
    return {
        "id": row["id"],
        "name": row["name"],
        "brand": row["brand"] or "",
        "platform": row["platform"] or "",
        "orderNo": row["order_no"] or "",
        "paymentType": row["payment_type"] or "正常",
        "hasShipping": bool(row["has_shipping"] or 0),
        "price": price,
        "depositAmount": deposit_amount,
        "balanceAmount": balance_amount,
        "shippingAmount": shipping_amount,
        "totalAmount": total_amount,
        "quantity": row["quantity"] or 1,
        "status": row["status"] or "待付款",
        "date": row["purchase_date"] or "",
        "note": row["note"] or "",
        "imageData": row["image_data"] or "",
        "createdAt": row["created_at"],
        "updatedAt": row["updated_at"],
    }


def execute_write(sql: str, params: tuple[Any, ...]) -> int:
    with connect() as conn:
        cur = conn.execute(sql, params)
        conn.commit()
        return int(cur.lastrowid)


def init_db() -> None:
    with connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                brand TEXT DEFAULT '',
                platform TEXT DEFAULT '',
                order_no TEXT DEFAULT '',
                payment_type TEXT DEFAULT '正常',
                has_shipping INTEGER DEFAULT 0,
                price REAL DEFAULT 0,
                deposit_amount REAL DEFAULT 0,
                balance_amount REAL DEFAULT 0,
                shipping_amount REAL DEFAULT 0,
                quantity INTEGER DEFAULT 1,
                status TEXT DEFAULT '待付款',
                purchase_date TEXT DEFAULT '',
                note TEXT DEFAULT '',
                image_data TEXT DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        columns = {row["name"] for row in conn.execute("PRAGMA table_info(records)").fetchall()}
        if "payment_type" not in columns:
            conn.execute("ALTER TABLE records ADD COLUMN payment_type TEXT DEFAULT '正常'")
        if "has_shipping" not in columns:
            conn.execute("ALTER TABLE records ADD COLUMN has_shipping INTEGER DEFAULT 0")
        if "deposit_amount" not in columns:
            conn.execute("ALTER TABLE records ADD COLUMN deposit_amount REAL DEFAULT 0")
        if "balance_amount" not in columns:
            conn.execute("ALTER TABLE records ADD COLUMN balance_amount REAL DEFAULT 0")
        if "shipping_amount" not in columns:
            conn.execute("ALTER TABLE records ADD COLUMN shipping_amount REAL DEFAULT 0")
        count = conn.execute("SELECT COUNT(*) AS count FROM records").fetchone()["count"]
        if count == 0:
            defaults = [
                ("白套装 蓝毛衣三件套", "娃衣", "淘宝", "TA20250101001", 200.00, 1, "待发货", "2025-01-01", "娃衣"),
                ("米白翻边打底裤", "娃衣", "淘宝", "", 53.64, 1, "已发货", "2025-01-02", ""),
                ("牛仔背带裤", "娃衣", "京东", "", 101.84, 1, "已收货", "2025-01-03", ""),
                ("花边打底", "娃衣", "淘宝", "", 51.44, 1, "待付款", "2025-01-04", ""),
                ("低领蓝色打底", "娃衣", "淘宝", "", 44.24, 1, "已购买", "2025-01-05", ""),
                ("低领杏色打底", "娃衣", "淘宝", "", 44.24, 1, "已购买", "2025-01-05", ""),
                ("黄色家居服", "娃衣", "拼多多", "", 73.04, 1, "待发货", "2025-01-06", ""),
                ("杏色背带裤", "娃衣", "淘宝", "", 104.00, 1, "已收货", "2025-01-07", ""),
            ]
            ts = now_text()
            conn.executemany(
                """
                INSERT INTO records
                    (name, brand, platform, order_no, payment_type, has_shipping, price, deposit_amount, balance_amount, shipping_amount, quantity, status, purchase_date, note, image_data, created_at, updated_at)
                VALUES (?, ?, ?, ?, '正常', 0, ?, 0, 0, 0, ?, ?, ?, ?, '', ?, ?)
                """,
                [(*item, ts, ts) for item in defaults],
            )
        conn.commit()


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return INDEX_FILE.read_text(encoding="utf-8")


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"ok": True, "db": str(DB_FILE), "time": now_text()}


@app.get("/api/records")
def list_records() -> list[dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM records ORDER BY id DESC").fetchall()
    return [row_to_record(row) for row in rows]


@app.post("/api/records")
def create_record(record: RecordIn) -> dict[str, Any]:
    ts = now_text()
    total_amount = record.price or (record.depositAmount + record.balanceAmount + record.shippingAmount)
    record_id = execute_write(
        """
        INSERT INTO records
            (name, brand, platform, order_no, payment_type, has_shipping, price, deposit_amount, balance_amount, shipping_amount, quantity, status, purchase_date, note, image_data, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            record.name.strip(),
            record.brand.strip(),
            record.platform.strip(),
            record.orderNo.strip(),
            record.paymentType.strip() or "正常",
            1 if (record.hasShipping or record.shippingAmount > 0) else 0,
            total_amount,
            record.depositAmount,
            record.balanceAmount,
            record.shippingAmount,
            record.quantity,
            record.status,
            record.date,
            record.note.strip(),
            record.imageData,
            ts,
            ts,
        ),
    )
    return get_record(record_id)


@app.get("/api/records/{record_id}")
def get_record(record_id: int) -> dict[str, Any]:
    with connect() as conn:
        row = conn.execute("SELECT * FROM records WHERE id = ?", (record_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Record not found")
    return row_to_record(row)


@app.put("/api/records/{record_id}")
def update_record(record_id: int, record: RecordIn) -> dict[str, Any]:
    total_amount = record.price or (record.depositAmount + record.balanceAmount + record.shippingAmount)
    with connect() as conn:
        exists = conn.execute("SELECT id FROM records WHERE id = ?", (record_id,)).fetchone()
        if not exists:
            raise HTTPException(status_code=404, detail="Record not found")
        conn.execute(
            """
            UPDATE records
            SET name = ?, brand = ?, platform = ?, order_no = ?, payment_type = ?, has_shipping = ?,
                price = ?, deposit_amount = ?, balance_amount = ?, shipping_amount = ?, quantity = ?,
                status = ?, purchase_date = ?, note = ?, image_data = ?, updated_at = ?
            WHERE id = ?
            """,
            (
                record.name.strip(),
                record.brand.strip(),
                record.platform.strip(),
                record.orderNo.strip(),
                record.paymentType.strip() or "正常",
                1 if (record.hasShipping or record.shippingAmount > 0) else 0,
                total_amount,
                record.depositAmount,
                record.balanceAmount,
                record.shippingAmount,
                record.quantity,
                record.status,
                record.date,
                record.note.strip(),
                record.imageData,
                now_text(),
                record_id,
            ),
        )
        conn.commit()
    return get_record(record_id)


@app.delete("/api/records/{record_id}")
def delete_record(record_id: int) -> dict[str, Any]:
    with connect() as conn:
        cur = conn.execute("DELETE FROM records WHERE id = ?", (record_id,))
        conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"ok": True}


@app.post("/api/import")
def import_records(records_to_import: list[RecordIn]) -> dict[str, Any]:
    if not records_to_import:
        return {"ok": True, "imported": 0}
    ts = now_text()
    with connect() as conn:
        conn.executemany(
            """
            INSERT INTO records
                (name, brand, platform, order_no, payment_type, has_shipping, price, deposit_amount, balance_amount, shipping_amount, quantity, status, purchase_date, note, image_data, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    item.name.strip(),
                    item.brand.strip(),
                    item.platform.strip(),
                    item.orderNo.strip(),
                    item.paymentType.strip() or "正常",
                    1 if (item.hasShipping or item.shippingAmount > 0) else 0,
                    item.depositAmount + item.balanceAmount + item.shippingAmount or item.price,
                    item.depositAmount,
                    item.balanceAmount,
                    item.shippingAmount,
                    item.quantity,
                    item.status,
                    item.date,
                    item.note.strip(),
                    item.imageData,
                    ts,
                    ts,
                )
                for item in records_to_import
            ],
        )
        conn.commit()
    return {"ok": True, "imported": len(records_to_import)}
