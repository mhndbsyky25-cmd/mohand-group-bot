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

from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

server = HTTPServer(("0.0.0.0", int(os.environ.get("PORT", 10000))), HealthHandler)
Thread(target=server.serve_forever, daemon=True).start()

import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
