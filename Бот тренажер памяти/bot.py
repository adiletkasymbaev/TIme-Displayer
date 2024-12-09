import telebot
from sleeptime import sleep
from difficults import easy, medium, hard, extreme
import time

bot = telebot.TeleBot('7963921102:AAELl5Q5l4O4SkVPMX2XoxQDuzhrdlkw6uM')

@bot.message_handler(func=lambda message: message.text == 'Начать тренировку')
def messages(message):
	@bot.message_handler()
	chat = message.chat.id
	easy_numbers = easy()
	medium_numbers = medium()
	hard_numbers = hard()
	extreme_numbers = extreme()
	difficults = [easy_numbers, medium_numbers, hard_numbers, extreme_numbers]
	current_index = 0
	sleeptime = sleep(difficults[current_index])

	bot.send_message(chat, f'Запомните следующие числа: {difficults[current_index]}')
bot.infinity_polling()