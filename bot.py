import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! للعب النرد اكتب /dice")

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_dice()

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("dice", dice))
app.run_polling()
