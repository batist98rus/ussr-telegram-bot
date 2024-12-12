import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("7508943729:AAGAtWmuzOC4fGTlZRn8gv98PR8Ld71WoAE")

# Функция обработки команды /info
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать на сервер RUST USSR PVE!\n\n"
        "🌟 **Основная информация:**\n"
        "🔹 **IP сервера:** 123.456.789:28015\n"
        "🔹 **Особенности:** PVE-режим, квесты, торговля, ивенты.\n"
        "🔹 **Правила:** /rules\n\n"
        "📅 Следующий вайп: **12 июня 2024**\n"
        "👥 Присоединяйтесь к нашему сообществу!\n\n"
        "Приятной игры! 🚀"
    )

# Запуск приложения
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("info", info_command))
    print("Бот запущен на Railway 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
