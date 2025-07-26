# utils/sales_report.py
from datetime import datetime, timedelta
import random

def get_sales_data():
    today = datetime.today()
    return [
        {
            "date": (today - timedelta(days=i)).strftime("%Y-%m-%d"),
            "count": random.randint(5, 20),
            "total": random.randint(200000, 800000)
        }
        for i in range(7)
    ]
