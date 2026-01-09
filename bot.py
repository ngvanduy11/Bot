import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ====== CẤU HÌNH ======
TOKEN = os.getenv("BOT_TOKEN")  # nhớ export BOT_TOKEN trong Termux
API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

# ====== /start ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT BUFF\n\n"
        "Cách dùng:\n"
        "/buff <username> <số_lượng>\n\n"
        "Ví dụ:\n"
        "/buff _l0v3ly.10 100"
    )

# ====== /buff ======
async def buff(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        username = context.args[0]
        amount = context.args[1]  # chỉ để hiển thị (API không dùng)

        # API của bạn cần fl1=username=xxx
        params = {
            "fl1": f"username={username}"
        }

        r = requests.get(API_URL, params=params, timeout=30)

        # API có thể trả text hoặc json
        try:
            data = r.json()
            api_msg = data
        except:
            api_msg = r.text

        await update.message.reply_text(
            f"✅ Đã gửi buff\n"
            f"👤 User: {username}\n"
            f"🔥 Số lượng: {amount}\n\n"
            f"📩 Phản hồi API:\n{api_msg}"
        )

    except:
        await update.message.reply_text(
            "⚠️ Sai cú pháp\n/buff <username> <số_lượng>"
        )

# ====== MAIN ======
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buff", buff))

    print("🤖 Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
