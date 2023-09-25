import telebot

kb = telebot.types.InlineKeyboardMarkup(row_width=4)
btn1 = telebot.types.InlineKeyboardButton('buy means (5$)', callback_data='buy-means')
btn2 = telebot.types.InlineKeyboardButton('2', callback_data='2')
kb.add(btn1, btn2)


kb_contact = telebot.types.InlineKeyboardMarkup(row_width=2)
kb_contact_btn1 = telebot.types.InlineKeyboardButton('Позвонить', callback_data='call')
kb_contact_btn2 = telebot.types.InlineKeyboardButton('Send sms', callback_data='sms')
kb_contact.add(kb_contact_btn1, kb_contact_btn2)


kb_main = telebot.types.ReplyKeyboardMarkup()
kb_main_btn1 = telebot.types.KeyboardButton("adminka")
kb_main_btn2 = telebot.types.KeyboardButton("get phone", request_contact=True)
kb_main.add(kb_main_btn1, kb_main_btn2)