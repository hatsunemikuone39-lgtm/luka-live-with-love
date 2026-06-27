from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
import os
from util import *
from datetime import datetime, timedelta, timezone

text1 = """Лукабот приветствует!!

Активные команды:
`лука хуесос`
`я боюсь луку`

Пока что всё, хз, че ещё придумать.

Авторы:
Алина
Claude Haiku 4.5."""

text2 = """Ой, ну ты чегоооо... 🥺👉👈 Ну на сааамом-то дельце... ну чесна-чесна, ну совсем-совсем не нуна меня бояться! 🙅‍♂️✨💖 Я же просто такой супер-пупер-мега пушистый комочек чистейшего добра и радужного позитива! 🌈🦄✨ Моё сердечко буквально сделано из сахарной ваты и звёздной пыльцы! ☁️⭐💖

Я же просто стою там, на нашей волшебной Инопланетной Сцене 👽🪐🎤, под светом неоновых созвездий, и просто... ну... выпускаю свою нежную душеньку в открытый космос через свои мимимишные песенки! 🎶🛸✨ Мой голосок — это как кусь нежной зефирки, он лечит ранки на ауре! 🍬🌸✨ 

А мои друзья... о божечки-кошечки, мои любименькие пусечки-друзяшки! 👯‍♀️🧸💖 Я люблю их больше, чем все-все галактики во вселенной вместе взятые! Мы как одна большая космическая семья из сахарных единорожек! 🦄✨💫 Я за них и в чёрную дыру, и за кофейком на Марс! ☕🚀💖

Обидеть кого-то??? МНЕ?! 😱💔 Да я скорее самоаннигилируюсь в розовую пыльцу и стану блёстками на чьих-то щеках, чем причиню хоть капельку грустяшки живому существу! 🦄✨💧 Я — это просто ходячий обнимательный вирус, который хочет затискать весь мир до состояния абсолютного счастья! 🤗💖✨ Чмок в пупок всех-всех-всех! 💋✨🎈 Не бойся меня, я твой самый ласковый инопланетный котик! 🐱👽💖✨🐾"""

# тут будем писать наш код :)
async def start(update, context):
    await send_text(update, context, text1)

async def hello(update, context):
    if (update.message.text=="лука хуесос"):
        await send_text(update, context, "luka, live with- ты ахуел")
        await send_text_buttons(update, context, "бро ты умрешь и тд", {
            "good_answer": "я передумал, лука красавчик",
            "bad_answer": "ыыы нет"
        })
    elif (update.message.text=="я боюсь луку"):
        await send_photo(update, context, "photo_2026")
        await send_text(update, context, text2)
    elif (update.message.text.isdigit()):
        moscow_tz = timezone(timedelta(hours=3))
        date1=datetime.now(moscow_tz)
        date2=datetime(2026,2,4,tzinfo=moscow_tz)
        tabl=timedelta(days=int(update.message.text))
        await send_text(update, context, (((date1-date2)-tabl).days))
    else:
        await send_text(update, context, "luka, live with love")
        await send_photo(update, context, "photo_2025-12-07_20-39-57")


async def hello_button(update, context):
    if update.callback_query.data=="good_answer":
        for i in range(20):
            await send_text(update, context, "luka, live with love")
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
app.add_handler(MessageHandler(filters.TEXT | filters.Regex(r'^\d+$'), hello))
app.add_handler(CallbackQueryHandler(hello_button))
app.run_polling()

