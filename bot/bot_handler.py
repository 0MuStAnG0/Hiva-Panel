# bot/bot_handler.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils.subscription import build_subscription_links

WELCOME_MSG = "👋 خوش آمدید به ربات Hiva VPN
برای دریافت لینک اشتراک خود از دستور /account استفاده کنید."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MSG)

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # فرض بر این است که فقط یک اکانت دارد
    from configs.models import VPNAccount
    account = VPNAccount.objects.filter(user__telegram_id=user_id).first()

    if not account:
        await update.message.reply_text("⛔️ هیچ اکانتی برای شما یافت نشد.")
        return

    link = build_subscription_links(account)
    await update.message.reply_text(f"🔗 لینک اشتراک شما:

{link}")
