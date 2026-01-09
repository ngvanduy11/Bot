import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ====== CẤU HÌNH ======
TOKEN = os.getenv("BOT_TOKEN")
API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

# ====== /start ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BUFF TOOL (giống tool gốc)\n\n"
        "Cách dùng:\n"
        "/fl1 <username>\n\n"
        "Ví dụ:\n"
        "/fl1 mhien.1m50"
    )

# ====== /fl1 ======
async def fl1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # kiểm tra cú pháp
    if len(context.args) < 1:
        await update.message.reply_text("⚠️ Dùng đúng cú pháp:\n/fl1 <username>")
        return

    username = context.args[0]

    # gọi API đúng chuẩn tool gốc
    url = f"{API_URL}?fl1={username}"

    try:
        r = requests.get(url, timeout=30)
    except Exception as e:
        await update.message.reply_text(f"❌ Lỗi kết nối API\n{e}")
        return

    # parse JSON
    try:
        data = r.json()
    except:
        await update.message.reply_text("❌ API không trả JSON hợp lệ")
        return

    # API báo thất bại
    if data.get("success") is not True:
        await update.message.reply_text(
            f"❌ Thất bại\n📩 {data.get('message')}"
        )
        return

    # API thành công (GIỐNG TOOL NGƯỜI TA)
    await update.message.reply_text(
        f"✅ Thành công\n"
        f"👤 User: {data.get('username')}\n"
        f"👥 Trước: {data.get('followers_before')}\n"
        f"👥 Sau: {data.get('followers_now')}\n"
        f"➕ Tăng: {data.get('followers_increased')}"
    )

# ====== MAIN ======
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fl1", fl1))

    print("🤖 Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
