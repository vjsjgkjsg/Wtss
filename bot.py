#!/usr/bin/env python3
"""
W.T.S HUB — Telegram Bot
Отправляет ссылку на лендинг wtswalletbot.pro
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ===== КОНФИГ =====
BOT_TOKEN = "8375191812:AAHPymoZBB0oXyan5xlJfYp5GhkEHF2o1z8"
LANDING_URL = "https://wtswalletbot.pro"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===== КОМАНДЫ =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /start — приветствие + ссылка на лендинг"""
    user = update.effective_user
    name = user.first_name if user.first_name else "участник"

    keyboard = [
        [InlineKeyboardButton("🌐 Открыть W.T.S HUB", url=LANDING_URL)],
        [InlineKeyboardButton("📢 Новостной канал", url="https://t.me/wtsprj")],
        [InlineKeyboardButton("📖 WTS FAQ", url="https://t.me/wtsproject")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        f"👋 Привет, *{name}*\\!\n\n"
        f"Добро пожаловать в *W\\.T\\.S PROJECT*\n\n"
        f"🔗 Перейди на наш официальный хаб:\n"
        f"`{LANDING_URL}`\n\n"
        f"На сайте ты найдёшь ссылку на основной чат\\.\n"
        f"⚠️ Ссылка на чат выдаётся *3 раза* и действует *10 минут*\\."
    )

    await update.message.reply_text(
        text,
        parse_mode="MarkdownV2",
        reply_markup=reply_markup
    )


async def hub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /hub — просто ссылка на лендинг"""
    keyboard = [[InlineKeyboardButton("🌐 W.T.S HUB", url=LANDING_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🔗 Официальный хаб: {LANDING_URL}",
        reply_markup=reply_markup
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /help"""
    await update.message.reply_text(
        "📋 *Команды бота:*\n\n"
        "/start — Приветствие и ссылки\n"
        "/hub — Ссылка на лендинг\n"
        "/help — Это сообщение",
        parse_mode="Markdown"
    )


# ===== ЗАПУСК =====

def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hub", hub))
    app.add_handler(CommandHandler("help", help_cmd))

    logger.info("✅ W.T.S Bot запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
