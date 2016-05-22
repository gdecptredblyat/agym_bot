from Functions import db, reciever
from Functions.reciever.utilities import *

bot = bot.bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['delete_me'])
def delete_user(message):
	bot.send_message(message.chat.id, 'Ваш профиль был удалён из базы данных.')
	db.student.delete(message.chat.id)


@bot.message_handler(commands=['me'])
def me(message):
	bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(commands=['add_student'])
def recive(message):
	reciever.add_student(message)


@bot.message_handler(commands=['get_mobile'])
def recieve(message):
	reciever.get_mobile(message)

@bot.message_handler(content_types=['text'])
def recive(message):
	if message.chat.id in shared.functions:
		shared.functions[message.chat.id](message)


bot.polling()
