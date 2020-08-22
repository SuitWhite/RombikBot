import telebot

bot = telebot.TeleBot("1303456504:AAGh8gJera2TdLX0myrAmVHjt1UgwUYho9w")


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('About', 'Gachimuchi', 'Our Tovarish language')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('sorry for what? My dad told me...', 'cum')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, it`s RombikBot. Please use buttons.', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'about':
        bot.send_message(message.chat.id, 'I was created by Boss of this gym Igor, @crusaderking for his great ambitions.', reply_markup=keyboard1)
    elif message.text.lower() == 'our tovarish language':
        bot.send_message(message.chat.id, 'https://t.me/setlanguage/tovarish', reply_markup=keyboard1)
    elif message.text.lower() == 'gachimuchi':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBPRBfQFeNQXMYrlTXqFVIXTDRr6Y3LwACHwAD8fNzE_MOb13TBgsKGwQ', reply_markup=keyboard1)
    elif message.text.lower() == 'send gachi' :
        bot.send_photo(message.chat.id, photo="https://telegram.org/img/t_logo.png")
    else: bot.send_message(message.chat.id, 'What you talking about? Go fuck yourself or use the buttons', reply_markup=keyboard1)

bot.polling()

