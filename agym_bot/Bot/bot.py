import telebot
import config

def listener(messages):
	for m in messages:
		if m.content_type == 'text':
			bot.send_message(m.chat.id, m.text)

if __name__ == '__main__':
	bot = telebot.TeleBot(config.token)
	# bot.remove_webhook()
	bot.set_update_listener(listener)
	bot.polling(none_stop=True)