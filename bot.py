from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
import os

from gpt import *
from util import *

# тут будем писать наш код :)
async def start(update, context):
    await send_text(update, context, "*Command START*")

async def hello(update, context):
    if (update.message.text=="лука хуесос"):
        await send_text(update, context, "luka, live with- ты ахуел")
        await send_text_buttons(update, context, "бро ты умрешь и тд", {
            "good_answer": "я передумал, лука красавчик",
            "bad_answer": "ыыы нет"
        })
    else:
        await send_text(update, context, "luka, live with love")
        await send_photo(update, context, "photo_2025-12-07_20-39-57")


async def hello_button(update, context):
    if update.callback_query.data=="good_answer":
        await send_text(update, context, "luka, live with love luka, live with love, luka live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love luka, live with love")
    else:
        await send_photo(update, context, "photo_1")
        await send_photo(update, context, "photo_2")
        await send_photo(update, context, "photo_3")
        await send_photo(update, context, "photo_4")
        await send_photo(update, context, "photo_5")
        await send_photo(update, context, "photo_6")
        await send_photo(update, context, "photo_7")
        await send_photo(update, context, "photo_8")
        await send_photo(update, context, "photo_9")
        await send_photo(update, context, "photo_10")
        await send_photo(update, context, "photo_11")
        await send_photo(update, context, "photo_12")
        await send_photo(update, context, "photo_13")
        await send_photo(update, context, "photo_14")
        await send_photo(update, context, "photo_15")
        await send_photo(update, context, "photo_16")
        await send_photo(update, context, "photo_17")
        await send_photo(update, context, "photo_18")
        await send_photo(update, context, "photo_19")
        await send_photo(update, context, "photo_20")
        await send_photo(update, context, "photo_21")
        await send_photo(update, context, "photo_22")
        await send_photo(update, context, "photo_23")
        await send_photo(update, context, "photo_24")


app = ApplicationBuilder().token(os.environ.get("TELEGRAM_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, hello))
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()
