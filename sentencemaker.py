import telebot

import random

API_KEY = 'YoUrApIkEy'
bot = telebot.TeleBot(API_KEY)


def create_story(m, g, e):
    story = []

    for i in range(11):
        random_m = random.choice(m)
        random_g = random.choice(g)
        random_e = random.choice(e)

        if "над" in random_g:
          random_e = random_e[0:-1] + "ой"

        if " в" in random_g:
          random_e = random_e[0:-1] + "у"

        arr_sentence = [random_m, random_g, random_e]
        sentence = " ".join(arr_sentence)

        story.append(sentence)

        full_story = ". ".join(story)

    return full_story


@bot.message_handler(commands=['story'])
def send_story(message):
    mestoimenia = ['Он', "Она", "Оно", "Олег", "Адилет", "Бомж", "Шрек", "Фиона", "Осел", "Гений", "Тупой", "Козел", "Алкаш", "Машина", "Собака", "Кошка", "Физрук"]
    glagoly = ["делает", "работает с", "сидит на", "смотрит на", "кушает", "смеется над", "играет в", "ищет", "печатает", "нашел", "потерял", "уехал в", "кинул в", "ударил"]
    end = ["машину", "мальчика", "корзину", "луне", "сиденье", "стуле", "бананы", "ашлянфу", "приколом", "улицу", "картошку"]

    story = create_story(mestoimenia, glagoly, end)

    bot.send_message(message.chat.id, story)

bot.polling(non_stop=True)
