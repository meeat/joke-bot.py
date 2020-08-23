import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Да, что надо?')
    elif message.text.lower() == 'иди нахуй':
        bot.send_message(message.chat.id, 'Агр сукаааааа')
    elif message.text.lower() == 'санай':
        bot.send_message(message.chat.id, 'Что ебать?')
    elif message.text.lower() == 'лох':
        bot.send_message(message.chat.id, 'Саси урод')
    elif message.text.lower() == 'агр':
        bot.send_message(message.chat.id, 'Агр сук отвечаю')
    elif message.text.lower() == 'санай лох':
        bot.send_message(message.chat.id, 'лафкииии пидр')
    elif message.text.lower() == 'санай пидр':
        bot.send_message(message.chat.id, 'Еблан тупой, дааааа блять ебал я таких друзей ааааааааагр')
    elif message.text.lower() == 'сасайка':
        bot.send_message(message.chat.id, 'фаталите))))))')
    elif message.text.lower() == 'вы где?':
        bot.send_message(message.chat.id, 'Тебя не должно ебать')
    elif message.text.lower() == 'ты где?':
        bot.send_message(message.chat.id, 'мммммммммбля не твоего ума дела щенок!')
    elif message.text.lower() == 'прости меня':
        bot.send_message(message.chat.id, 'Пиздабол')
    elif message.text.lower() == 'пидр':
        bot.send_message(message.chat.id, 'Спасибо я такой')
    elif message.text.lower() == 'да иди нахуй':
        bot.send_message(message.chat.id, 'Только после тебя АААААГР')
    elif message.text.lower() == 'Саша':
        bot.send_message(message.chat.id, 'что?')
    elif message.text.lower() == 'бмв':
        bot.send_message(message.chat.id, 'Еби гусей!')
    elif message.text.lower() == 'сасай':
        bot.send_message(message.chat.id, 'Сасай-это очень уютный уголок в теплой пижамке!')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'днс дела, ты тупой пздц')
    elif message.text.lower() == 'как дела':
        bot.send_message(message.chat.id, 'работаю, вечером туса есть?')
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'агр!король')
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Пидр ответ ахах')
    elif message.text.lower() == 'хз':
        bot.send_message(message.chat.id, 'В жопу даеш?')
    elif message.text.lower() == 'сам сасай':
        bot.send_message(message.chat.id, 'это я люблю))')
    else:
        bot.send_message(chat_id, 'Сасай')

bot.polling()