import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler

logging.basicConfig(
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level = logging.INFO
)

async def start(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id,text="hello, world ! :)")

async def echo(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id, text=update.message.text)

async def caps(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = ' '.join(context.args).upper())

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

if __name__ == "__main__":
    print('starting app..')
    application = ApplicationBuilder().token('6482211458:AAFiOEY3sq13UoRB-U-4D51ocrjHTSWgfBo').build()
    application.add_handler(CommandHandler('start',start))
    application.add_handler(MessageHandler(filters.TEXT and (~filters.COMMAND) , echo))
    application.add_handler(CommandHandler('caps',caps))
    application.add_handler(InlineQueryHandler(inline_caps))
    print('polling..')
    application.run_polling(allowed_updates=Update.ALL_TYPES)
