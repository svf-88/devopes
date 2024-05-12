#!/usr/bin/env python
# @craftvrnbot

import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("#ПА и #задача - прикладные администраторы\n#DevOps - девопс-инженеры\n* регистр не важен")



async def callback_method(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Получите текущую дату и время
    current_date_time = datetime.now()
    # Получите номер дня недели (0 - понедельник, 1 - вторник, и т.д.)
    weekday_number = current_date_time.weekday()
    # Получите текущее время
    current_time = current_date_time.strftime("%H:%M:%S")

    # Проверьте, находится ли текущее время между 9:00 и 18:00 и является ли сегодня будним днем
    if current_date_time.hour >= 9 and current_date_time.hour < 18 and weekday_number < 5:
        message = update.message.text
        if any(tag in message.lower() for tag in ["#па", "#задача"]): 
        # Функция any() использует список хештегов для проверки каждого элемента списка tag in message.в_нижнем_регистре.
            await  update.message.reply_text(text="Прошу обратить внимание 👆 \n@yaroslav_redin @Lashalom @SilentScream89")
        elif  any(tag in message.lower() for tag in ["#devops"]):
            await  update.message.reply_text(text="Прошу обратить внимание 👆 \n@SergeyPh @KyHaHbIp @danilsaushin")
    else:
        await  update.message.reply_text(text="Рабочий день окончен или еще не начался.🦦")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("***").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.Entity("hashtag"), callback_method))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
