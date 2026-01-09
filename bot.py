import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BUFF TOOL\n\n"
        "Cách dùng (giống tool gốc):\n"
        "/fl1 <username>\n\n"
        "Ví dụ:\n"
        "/fl1 mhien.1m50"
    )

# /fl1
async def fl1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        username = context.args[0]

        # GỌI API GIỐNG Y HỆT TOOL NGƯỜI TA
        url = f"{API_URL}?fl1={username}"
        r = requests.get(url, timeout=30)

        # API trả JSON
        try:
            data = r.json()
            msg = (
                f"✅ Thành công\n"
                f"👤 User: {data.get('username')}\n"
                f"👥 Trước: {data.get('followers_before')}\n"
                f"👥 Sau: {data.get('followers_now')}\n"
                f"➕ Tăng: {data.get('followers_increased')}"
            )
        except:
            msg = r.text

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text(
            "⚠️ Dùng đúng cú pháp:\n/fl1 <username>"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fl1", fl1))

    print("🤖 Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
