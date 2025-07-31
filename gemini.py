import os
import io
import logging
logging.basicConfig(level=logging.INFO)
import PIL.Image # type: ignore
from pyrogram.types import Message # type: ignore
import google.generativeai as genai # type: ignore
from pyrogram import Client, filters # type: ignore
from pyrogram.enums import ParseMode # type: ignore
from config import API_ID, API_HASH, BOT_TOKEN, GOOGLE_API_KEY, MODEL_NAME

# 🚫 Spam keywords
SPAM_KEYWORDS = [
    "free eth", "airdrop", "connect wallet", "claim eth",
    "freeethereum", "www.freeether", "instant reward",
    "click here", "real ethereum", "get rich quick", "free money"
]

app = Client(
    "gemini_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.MARKDOWN
)

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# 🛡️ Spam filter
@app.on_message(filters.text & ~filters.private)
async def spam_filter(client: Client, message: Message):
    text = message.text.lower()
    if any(keyword in text for keyword in SPAM_KEYWORDS):
        try:
            await message.delete()
            print(f"🚫 Deleted spam message from @{message.from_user.username or 'unknown'}")
        except Exception as e:
            print(f"⚠️ Failed to delete spam message: {e}")

# ... your existing handlers stay the same
