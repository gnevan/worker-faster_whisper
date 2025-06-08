import os
import logging

from fastapi import FastAPI, Request, HTTPException
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ContextTypes, CallbackContext
)

# Configure logging for better debug output
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Retrieve the token from environment
BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not BOT_TOKEN:
    raise Exception("Missing Telegram bot token. Please set the TELEGRAM_TOKEN environment variable.")

# Create the FastAPI app
app = FastAPI()

# Build the telegram application (bot) instance.
telegram_app = Application.builder().token(BOT_TOKEN).build()

# Define a command handler (e.g., /start)
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Hello from RunPod Serverless Telegram Bot!")

async def message_handler(update: Update, context: CallbackContext) -> None:
    if update.message:
        await update.message.reply_text("This is a reply from RunPod Serverless Telegram Bot!")

# Add the handler to the Telegram application
telegram_app.add_handler(CommandHandler("start", start_command))
telegram_app.add_handler(MessageHandler(None, message_handler))

# Webhook endpoint where Telegram posts updates.
@app.post("/")
async def webhook(request: Request):
    try:
        update = Update.de_json(await request.json(), telegram_app.bot)
    except Exception as e:
        logger.error("Error parsing update: %s", e)
        raise HTTPException(status_code=400, detail="Invalid request format")
    
    # Process the update asynchronously
    await telegram_app.process_update(update)
    return {"status": "ok"}
