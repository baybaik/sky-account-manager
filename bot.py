
import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🌟 Sky Account Manager\n\n"
        "/add - Tambah akun\n"
        "/accounts - Daftar akun\n"
        "/status - Status bot"
    )

@bot.message_handler(commands=["add"])
def add(message):
    bot.reply_to(message, "Kirim nama label akun:")
    bot.register_next_step_handler(message, save_account)

accounts = {}

def save_account(message):
    name = message.text.strip()
    accounts[name] = "Terdaftar"
    bot.reply_to(message, f"Berhasil menambahkan {name}")

@bot.message_handler(commands=["accounts"])
def list_accounts(message):
    if not accounts:
        bot.reply_to(message, "Belum ada akun.")
    else:
        bot.reply_to(message, "\n".join(accounts.keys()))

@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(message, "Bot aktif!")

bot.infinity_polling()
