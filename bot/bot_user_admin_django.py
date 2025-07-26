# bot_user_admin_django.py
import os
import django
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تنظیم مسیر پروژه Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hivapanel.settings")
django.setup()

from core.models import User, Reseller
from django.contrib.auth.models import User as Admin

TOKEN = os.getenv("HIVA_BOT_TOKEN", "YOUR_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)

    # بررسی نقش‌ها
    try:
        admin = Admin.objects.get(profile__telegram_id=uid)
        await update.message.reply_text("👑 خوش آمدید ادمین عزیز!
/admin")
        return
    except:
        pass

    try:
        reseller = Reseller.objects.get(telegram_id=uid)
        await update.message.reply_text("📦 خوش آمدید فروشنده عزیز!
/reseller")
        return
    except:
        pass

    try:
        user = User.objects.get(telegram_id=uid)
        await update.message.reply_text("🌐 خوش آمدید کاربر عزیز!
/account")
        return
    except:
        pass

    await update.message.reply_text("⛔️ شما ثبت نشده‌اید.")

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    try:
        user = User.objects.get(telegram_id=uid)
        await update.message.reply_text(
            f"🧾 اکانت شما:
نام: {user.username}
ترافیک: {user.traffic} GB
انقضا: {user.expire_date}"
        )
    except:
        await update.message.reply_text("❌ اطلاعات یافت نشد.")

async def reseller(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    try:
        reseller = Reseller.objects.get(telegram_id=uid)
        users = User.objects.filter(reseller=reseller)
        await update.message.reply_text(f"📊 کاربران شما: {users.count()} نفر")
    except:
        await update.message.reply_text("❌ شما فروشنده نیستید.")

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    try:
        admin = Admin.objects.get(profile__telegram_id=uid)
        users = User.objects.all().count()
        resellers = Reseller.objects.all().count()
        await update.message.reply_text(f"📌 کاربران کل: {users}
📦 فروشنده‌ها: {resellers}")
    except:
        await update.message.reply_text("❌ فقط ادمین دسترسی دارد.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("account", account))
    app.add_handler(CommandHandler("reseller", reseller))
    app.add_handler(CommandHandler("admin", admin))
    app.run_polling()

if __name__ == "__main__":
    main()
