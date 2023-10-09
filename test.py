import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level = logging.INFO
)

async def start(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id,text="hello, world ! :)")

if __name__ == "__main__":
    print('starting app..')
    application = ApplicationBuilder().token('6482211458:AAFiOEY3sq13UoRB-U-4D51ocrjHTSWgfBo').build()
    application.add_handler(CommandHandler('start',start))

    print('polling..')
    application.run_polling()
