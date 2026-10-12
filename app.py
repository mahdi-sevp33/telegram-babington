import telebot
import andro_cfw
from dotenv import load_dotenv
import os 

# 1-Line Auto-Patcher: Routes 100% of Telegram API calls through Cloudflare Worker
session = andro_cfw.patch()
load_dotenv()

token=os.getenv("YOUR_BOT_TOKEN_FROM_BOTFATHER")

if not token:
    print("your token of your bot was not found")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
        "🤖 **Hello from behind the filter!**\n\n"
        f"🌐 **Worker URL**: `{session.worker_url}`\n"
        "🔒 **Status**: Unfiltered & Running Smoothly!"
    )


if __name__ == "__main__":
    print(f"🚀 Bot starting behind Cloudflare Worker ({session.worker_url})...")
    bot.infinity_polling(timeout=20, long_polling_timeout=20)     #یک تابع هست که برای این فراخوانی میشه که مدام گوش بزنگ باشدواگرپیامی ازتلگرام بهش رسید باتوابع ازپیش تعریف شده هندل کند 





