# pg_multi_sync.py
import psycopg2
from psycopg2.extras import RealDictCursor
import json

# لیست سرورهای هدف برای همگام‌سازی
SERVERS = [
    {"host": "10.0.0.1", "port": 5432, "dbname": "hiva", "user": "hiva", "password": "pass1"},
    {"host": "10.0.0.2", "port": 5432, "dbname": "hiva", "user": "hiva", "password": "pass2"},
]

# سرور مرجع (اصلی)
MASTER = {
    "host": "localhost", "port": 5432,
    "dbname": "hiva", "user": "hiva", "password": "localpass"
}

TABLES = ["core_user", "core_reseller"]

def get_rows(conn, table):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(f"SELECT * FROM {table}")
        return cur.fetchall()

def sync_table(master_conn, target_conn, table):
    print(f"🔁 Syncing table: {table}")
    master_data = get_rows(master_conn, table)

    with target_conn.cursor() as cur:
        cur.execute(f"DELETE FROM {table}")
        for row in master_data:
            cols = ', '.join(row.keys())
            placeholders = ', '.join(['%s'] * len(row))
            values = list(row.values())
            cur.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", values)
        target_conn.commit()

def main():
    print("🚀 Connecting to master DB...")
    master_conn = psycopg2.connect(**MASTER)
    for srv in SERVERS:
        print(f"🌐 Connecting to {srv['host']}")
        target_conn = psycopg2.connect(**srv)
        for table in TABLES:
            sync_table(master_conn, target_conn, table)
        target_conn.close()
        print(f"✅ Synced {srv['host']}")
    master_conn.close()
    print("🎯 Done.")

if __name__ == "__main__":
    main()
