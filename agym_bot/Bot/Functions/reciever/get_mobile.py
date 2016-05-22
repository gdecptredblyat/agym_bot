from .utilities import *
from .. import db
import telebot

bot = bot.bot

def get_mobile(message):
	bot.send_message(message.chat.id, 'Введите номер и букву класса СЛИТНО' + 
		' (10i) или фамилию и имя человека.')

	def find_mobile(message):
		words = message.text.split(' ')

		if len(words) == 1:
			mobiles = db.get_mobile.group(message.text)

			for person in mobiles:
				bot.send_message(message.chat.id, person["last_name"] + " " + 
					person["first_name"] + ": " + person["mobile"])
		elif len(words) == 2:
			mobile = db.get_mobile.person(words[0], words[1])

			if mobile:
				bot.send_message(message.chat.id, words[0] + " " + words[1] + 
					": " + mobile)
			else:
				bot.send_message(message.chat.id, 
					'Этого человека нет в базе данных.')
		else:
			bot.send_message(message.chat.id, 'Неверный ввод данных.')

	shared.functions[message.chat.id] = find_mobile