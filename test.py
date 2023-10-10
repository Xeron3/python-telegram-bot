import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level = logging.INFO
)

async def start(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id,text="hello, world ! :)")

async def echo(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id, text=update.message.text)

if __name__ == "__main__":
    print('starting app..')
    application = ApplicationBuilder().token('6482211458:AAFiOEY3sq13UoRB-U-4D51ocrjHTSWgfBo').build()
    application.add_handler(CommandHandler('start',start))
    application.add_handler(MessageHandler(filters.TEXT and (~filters.COMMAND) , echo))
    print('polling..')
    application.run_polling()
