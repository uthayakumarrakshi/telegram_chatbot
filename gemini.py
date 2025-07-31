from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 12345678  # Replace with your API ID
API_HASH = "your_api_hash"  # Replace with your API Hash
BOT_TOKEN = "your_bot_token"  # Replace with your Bot Token

app = Client("gemini_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ /start command
@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply("👋 Hello! I’m your Gemini bot. Send /gem or /imgai to start.")

# ✅ /help command
@app.on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    await message.reply("ℹ️ Commands:\n/start - Welcome message\n/help - List commands\n/gem - AI chat\n/imgai - Image generation")

# ✅ Example /gem command
@app.on_message(filters.command("gem"))
async def gem_handler(client: Client, message: Message):
    await message.reply("✨ Gemini AI: This feature is under development.")

# ✅ Example /imgai command
@app.on_message(filters.command("imgai"))
async def imgai_handler(client: Client, message: Message):
    await message.reply("🖼️ Image AI: This feature is under development.")

# ✅ Basic spam filter: auto-delete messages with scam keywords
SPAM_KEYWORDS = [
    "free eth", "airdrop", "connect wallet", "claim ethereum",
    "scamdrop.com", "freeether.net", "crypto giveaway"
]

@app.on_message(filters.text & ~filters.command(["start", "help", "gem", "imgai"]))
async def spam_filter_handler(client: Client, message: Message):
    text = message.text.lower()
    if any(keyword in text for keyword in SPAM_KEYWORDS):
        try:
            await message.delete()
            print(f"[SPAM] Deleted message from {message.from_user.id if message.from_user else 'Unknown'}: {message.text}")
        except Exception as e:
            print(f"Error deleting spam message: {e}")

if __name__ == '__main__':
    print("🤖 Bot is running...")
    app.run()
the same
