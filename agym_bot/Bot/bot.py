from Functions import db
import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['delete_me'])
def delete_user(message):
	bot.send_message(message.chat.id, 'ня.пока')


@bot.message_handler(commands=['get_number'])
def get_mobile(message):
	if message.text:
		if len(message.text.split(' ')) == 2:
			db.get_mobile.group(message.text.split(' ')[1])


@bot.message_handler(content_types=['text', 'sticker'])
def repeat_all_messages(message):
	if message.text:
		bot.send_message(message.chat.id, message.text)
	else:
		bot.send_message(message.chat.id, ';')

bot.polling()
