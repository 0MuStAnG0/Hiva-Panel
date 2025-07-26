# bot_reseller.py
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os

reseller_users = {
    "123456789": {  # Telegram user_id as key
        "username": "reseller1",
        "users": [
            {"username": "user1", "traffic": 10, "active": True},
            {"username": "user2", "traffic": 5, "active": False}
        ]
    }
}

TOKEN = os.getenv("RESELLER_BOT_TOKEN", "YOUR_TOKEN_HERE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if uid not in reseller_users:
        await update.message.reply_text("⛔️ شما فروشنده نیستید. لطفاً با مدیر تماس بگیرید.")
        return
    await update.message.reply_text("🎉 خوش آمدید به پنل فروشنده هیوا!

دستور /panel را بزنید.")

async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    reseller = reseller_users.get(uid)
    if not reseller:
        await update.message.reply_text("⛔️ دسترسی ندارید.")
        return
    count = len(reseller["users"])
    active_count = sum(1 for u in reseller["users"] if u["active"])
    await update.message.reply_text(
        f"📊 کاربران شما: {count} نفر
✅ فعال: {active_count}
❌ غیرفعال: {count - active_count}"
    )

async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    reseller = reseller_users.get(uid)
    if not reseller:
        await update.message.reply_text("⛔️ دسترسی ندارید.")
        return
    msg = "👥 کاربران:
"
    for u in reseller["users"]:
        status = "✅" if u["active"] else "❌"
        msg += f"- {u['username']} | ترافیک: {u['traffic']} GB | {status}\n"
    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(CommandHandler("list", list_users))
    app.run_polling()

if __name__ == "__main__":
    main()
