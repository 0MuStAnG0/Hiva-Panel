import requests
import os

BOT_TOKEN = os.getenv("HIVA_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

def notify_sync(success=True, message=""):
    if not BOT_TOKEN or not ADMIN_CHAT_ID:
        return
    status = "✅ همگام‌سازی با موفقیت انجام شد." if success else f"❌ خطا در همگام‌سازی:\n{message}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": ADMIN_CHAT_ID,
        "text": status
    }
    requests.post(url, data=data)
