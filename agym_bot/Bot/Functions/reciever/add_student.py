from .utilities import *
from .. import db
import telebot

bot = bot.bot

def add_student(message):
	shared.data["new_student"] = [0, ]

	def add_mobile(message):
		if message.text != '*':
			shared.data["new_student"].append(message.text)
		else:
			shared.data["new_student"].append('Не указано')

		print(shared.data["new_student"])
		db.student.add(shared.data["new_student"])

		bot.send_message(message.chat.id, 'Пользователь был успешно добавлен' +
		' в базу данных.')

	def add_class(message):
		if message.text != '*':
			shared.data["new_student"].append(message.text)
		else:
			shared.data["new_student"].append('Не указано')

		shared.functions[message.chat.id] = add_mobile
		bot.send_message(message.chat.id, 'Телефон: ')

	def add_first_name(message):
		if message.text != '*':
			shared.data["new_student"].append(message.text)
		else:
			shared.data["new_student"].append('Не указано')

		shared.functions[message.chat.id] = add_class
		bot.send_message(message.chat.id, 'Класс: ')

	def add_last_name(message):

		if message.text != '*':
			shared.data["new_student"].append(message.text)
		else:
			shared.data["new_student"].append('Не указано')

		shared.functions[message.chat.id] = add_first_name
		bot.send_message(message.chat.id, 'Имя: ')


	bot.send_message(message.chat.id, 'Если не хотите что-то указывать,' + 
		' напишите *')

	shared.functions[message.chat.id] = add_last_name
	bot.send_message(message.chat.id, 'Фамилия: ')
