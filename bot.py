import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT BUFF\n\n"
        "Cách dùng:\n"
        "/buff <username> <số_lượng>\n\n"
        "Ví dụ:\n"
        "/buff _l0v3ly.10 100"
    )

async def buff(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        username = context.args[0]
        amount = context.args[1]

        params = {
            "username": username,
            "amount": amount
        }

        r = requests.get(API_URL, params=params, timeout=30)
        data = r.json()

        if data.get("status") == "success":
            await update.message.reply_text(
                f"✅ BUFF THÀNH CÔNG\n"
                f"👤 User: {username}\n"
                f"🔥 Số lượng: {amount}"
            )
        else:
            await update.message.reply_text(f"❌ Lỗi: {data}")

    except:
        await update.message.reply_text("⚠️ Dùng đúng cú pháp:\n/buff <username> <số_lượng>")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buff", buff))

    print("🤖 Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
