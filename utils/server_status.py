# utils/server_status.py
import random

def get_all_server_status():
    return [
        {"name": "Server 1", "status": "🟢 Online", "ping": random.randint(20, 80)},
        {"name": "Server 2", "status": "🟠 Slow", "ping": random.randint(100, 200)},
        {"name": "Server 3", "status": "🔴 Offline", "ping": "---"},
    ]
