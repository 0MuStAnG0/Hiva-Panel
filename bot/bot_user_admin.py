# bot_user_admin.py
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# دیتابیس ساختگی برای نمونه
ADMINS = {"111111111"}  # user_id تلگرام
USERS = {"222222222"}  # کاربران نهایی
RESELLERS = {"123456789"}

TOKEN = os.getenv("HIVA_BOT_TOKEN", "YOUR_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if uid in ADMINS:
        await update.message.reply_text("👑 سلام ادمین عزیز! دستور /admin برای دسترسی استفاده کنید.")
    elif uid in RESELLERS:
        await update.message.reply_text("👤 سلام فروشنده عزیز! دستور /reseller را امتحان کنید.")
    elif uid in USERS:
        await update.message.reply_text("🌐 به پنل کاربری خوش آمدید. دستور /account را بزنید.")
    else:
        await update.message.reply_text("❌ شما ثبت نشده‌اید. لطفاً با پشتیبانی تماس بگیرید.")

# دستورات ادمین
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if uid not in ADMINS:
        return
    await update.message.reply_text("🧩 پنل ادمین:
/list_users
/list_resellers")

# دستورات فروشنده
async def reseller(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if uid not in RESELLERS:
        return
    await update.message.reply_text("📦 پنل فروشنده:
/panel
/list")

# دستورات کاربر
async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    if uid not in USERS:
        return
    await update.message.reply_text("🧾 اطلاعات شما:
ترافیک: 15 GB
اعتبار: تا 1403/12/29")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CommandHandler("reseller", reseller))
    app.add_handler(CommandHandler("account", account))
    app.run_polling()

if __name__ == "__main__":
    main()
