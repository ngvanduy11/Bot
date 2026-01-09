import requests
from telegram.ext import Updater, CommandHandler

TOKEN = "BOT_TOKEN_CUA_BAN"
API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

def start(update, context):
    update.message.reply_text(
        "🤖 BOT BUFF\n\n"
        "Cách dùng:\n"
        "/buff <username> <số_lượng>\n\n"
        "Ví dụ:\n"
        "/buff _l0v3ly.10 100"
    )

def buff(update, context):
    try:
        username = context.args[0]
        amount = context.args[1]

        params = {
            "username": username,
            "amount": amount
        }

        r = requests.get(API_URL, params=params, timeout=30)
        data = r.json()

        if data["status"] == "success":
            update.message.reply_text(
                f"✅ BUFF THÀNH CÔNG\n"
                f"👤 User: {data['username']}\n"
                f"🔥 Số lượng: {data['amount']}"
            )
        else:
            update.message.reply_text(f"❌ Lỗi: {data['message']}")

    except IndexError:
        update.message.reply_text("⚠️ Sai cú pháp\n/buff <username> <số_lượng>")
    except Exception as e:
        update.message.reply_text(f"❌ Lỗi hệ thống:\n{e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buff", buff))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
