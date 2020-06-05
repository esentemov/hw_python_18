import telebot
from random import choice

bot = telebot.TeleBot('token')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Саня', 'Мем')

memes = ['https://imbt.ga/B2ZpDO32r2', 'https://imbt.ga/7N8sm7voA6', 'https://imbt.ga/pjoJLQHWZh', 'https://imbt.ga/dEI6Q6ewd7']
jokes = ['Саня, верни сотку', 'Видишь, на дороге А нарисована? Это для Александров', 'Смешная шутка про Саню']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, меня зовут Саня, перейди в меню и нажми на кнопку', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'саня':
        bot.send_message(message.chat.id, choice(jokes))
    if message.text.lower() == "мем":
      bot.send_photo(message.chat.id, choice(memes))

@bot.message_handler(content_types=['photo'])
def photo(message):
    print(message)

bot.polling()
