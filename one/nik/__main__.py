import telebot
from telebot import types

bot = telebot.TeleBot('5186574353:AAEpwo_sWNba7m3Ubf1aIozUQyR2XDbN03I')

@bot.message_handler(commands=['start'])
def main(message):
        markp = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("Python")
        button_2 = types.KeyboardButton("C++")
        button_3 = types.KeyboardButton("C#")
        button_4 = types.KeyboardButton("Java")
        button_5 = types.KeyboardButton("JavaScript")
        markp.add(button_1, button_2, button_3, button_4, button_5)
        bot.send_message(message.chat.id,text="Выбирай ЯП, о котором хочешь узнать факт и получить курс для новичка!!!", reply_markup=markp)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Python"):
        bot.send_message(message.chat.id, text="Python не нуждается в компиляторе: \n https://avatars.mds.yandex.net/get-vthumb/1625998/997027170e64b1e64c94d86ace45a852/564x318_1")
    elif (message.text == "C++"):
        bot.send_message(message.chat.id, text="C ++ является одним из преобладающих языков для разработки всех видов технического и коммерческого программного обеспечения: \n https://avatars.mds.yandex.net/get-vthumb/3447593/d01d55dabada823d234666d51e203887/564x318_1")
    elif (message.text == "C#"):
        bot.send_message(message.chat.id, text="Язык C# хорош для разработки игр. Он также используется Unity (лидером большинства в коммерческих игровых движках) для разработки игр: \n https://avatars.mds.yandex.net/get-vthumb/3843733/ef13a8171e73fd403afcc8a3b463f717/564x318_1")
    elif (message.text == "Java"):
        bot.send_message(message.chat.id, text="Java была сделана случайно. Около 1992 года Джеймс Гослинг работал в лаборатории Sun Labs. Он и его команда в то время занимались созданием телевизионной приставки, которая начиналась с «очистки» C++, и все они получили новый язык Java или Oak: \n https://avatars.mds.yandex.net/get-vthumb/4099810/b8228dc03f1a49dbbc60758be70db672/564x318_1")
    elif (message.text == "JavaScript"):
        bot.send_message(message.chat.id, text="Язык был разработан Брендоном Айком за 10 дней: \n https://avatars.mds.yandex.net/get-vthumb/986839/de01517dffbe344279c7174b45c4b769/564x318_1")

    elif (message.text == "Вернуться в главное меню"):
        markp = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("Python")
        button_2 = types.KeyboardButton("C++")
        button_3 = types.KeyboardButton("C#")
        button_4 = types.KeyboardButton("Java")
        button_5 = types.KeyboardButton("Kotlin")
        button_6 = types.KeyboardButton("Вернуться в главное меню")
        markp.add(button_1, button_2, button_3, button_4, button_5, button_6)
        bot.send_message(message.chat.id, text="Вы опять у выбора", reply_markup=markp)
    else:
        bot.send_message(message.chat.id, text="Я не могу ответить на подобный вопрос")

if __name__ == '__main__':
    main()
bot.polling(none_stop=True)
