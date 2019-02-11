import telebot
#import parser

#main variables
TOKEN = "772185048:AAG9vTg3xnPyIW48IqJGXM7PpX7myBBya5Q"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Добро пожаловать!")
    elif message.text == "Как ты?" or message.text == "Как ты себя чувствуешь?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    elif message.text == "Кто ты?" or message.text == "Кто?":
        bot.send_message(message.from_user.id, "Я бот smev-0.1v, планирую писать тут оповещения служебного характера")
    else:
        bot.send_message(message.from_user.id, "Незапраграмирован ответ на этот вопрос, скоро тут будет меню или help")

bot.polling(none_stop=True, interval=1)