import telebot
import keborts
import random
# pyTelegramBotApi
# contact -> 050345345
bot = telebot.TeleBot('6679426168:AAEVGJVKsCPrkus767Po8AjeR7d8wIJCQg0')
counter = 0
adminId = [191632816, 345345, 345345, 345453453]
admins = {
    "top-admins": [191632816, 34534534, 345345],
    "manager": [23534, 345, 4533254, 345],
    "buhgalter": [253345, 345345, 345345]
}
# id all users 1 db 2 local file


def genarait_passwort():
    random.randint(1000000, 90000000000)

@bot.message_handler(commands=['admin'])
def user(message):
    print(1)
    if message.chat.id in [191632816, 957139896]:
        with open('Id.txt', 'r' , encoding='utf8') as file:
            text = file.read()
            bot.send_message(message.chat.id,  'Пользователей <b>' +  str(text.count('\n')) + "</b> человека", parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'У вас нет доступа к этой команде')




# command start
@bot.message_handler(commands=['start'])
def handler_message(message):
    bot.send_message(message.chat.id, '<b>hello</b>', parse_mode='html', reply_markup=keborts.kb)

    with open('Id.txt' , 'r' ,  encoding='utf8') as file:
        text = file.read()
        if str(message.chat.id) not in text:
            with open("Id.txt", 'a', encoding='utf8') as file:
                file.write(str(message.chat.id) + '\n')


@bot.message_handler(commands=['statistics'])
def handler_message(message):
    global counter
    if message.chat.id in admins['top-admins']:
        bot.send_message(message.chat.id, counter)
    else:
        bot.send_message(message.chat.id, 'нет доступа')

# message text
@bot.message_handler(func=lambda message:True)
def handler_message(message):
    global counter
    counter += 1
    if message.text == 'hello':
        bot.send_message(message.chat.id, '<i>Вау</i>', parse_mode='html')
    if message.text == 'contact':
        bot.send_message(message.chat.id, '380506789344', reply_markup=keborts.kb_main)


@bot.message_handler(content_types="contact")
def handler_message(message):
    bot.send_message(message.chat.id, '<i>phone number + </i>', parse_mode='html')


@bot.message_handler(content_types='document')
def handler_message(message):
    bot.send_message(message.chat.id, '<i> document + </i>', parse_mode='html')






bot.polling(none_stop=True)

