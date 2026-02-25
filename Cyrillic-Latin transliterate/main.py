from django.db.models.expressions import result

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "8654129454:AAH9Rk2vk3eQ-iAjJ1POsELBeHAJWE8mbtc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalamu alaykum, Xush kelibsiz!"
    answer += "\nMatn kiriting: "
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    result = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, result(msg))

    # if msg.isascii():
    #     result = to_cyrillic(msg)
    # else:
    #     result = to_latin(msg)
    # bot.reply_to(message, result)

bot.polling()


# word = input("Matn kiriting: ")
# if word.isascii():
#     print(to_cyrillic(word))
# else:
#     print(to_latin(word))

