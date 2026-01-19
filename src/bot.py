from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from handlers import (
    start, random, random_button, gpt, message_handler, talk, talk_button,
    translator, translator_button, gpt_button, recommendation, recommendation_button
)


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("random", random))
app.add_handler(CommandHandler("gpt", gpt))
app.add_handler(CommandHandler("talk", talk))
app.add_handler(CommandHandler("translator", translator))
app.add_handler(CommandHandler("recommendation", recommendation))

app.add_handler(CallbackQueryHandler(gpt_button, pattern='^start$'))
app.add_handler(CallbackQueryHandler(random_button, pattern='^(random|start)$'))
app.add_handler(
    CallbackQueryHandler(talk_button, pattern='^talk_.*|^talk$|^start$')
)
app.add_handler(
    CallbackQueryHandler(translator_button, pattern='^translator.*|^start$')
)
app.add_handler(
    CallbackQueryHandler(
        recommendation_button,
        pattern='^rec_.*|^next_recommendation$|^recommendation_back$|^start$'
    )
)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)
