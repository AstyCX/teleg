import telebot
from telebot import types

joinedFile = open("C:/Users/Macris/PycharmProjects/teleg/joined.txt", "r")
joinedUsers = set()

token = "1798183558:AAGluY3FicxM_thxynA_QjjnDcxPC81_XfI"

client = telebot.TeleBot(token)

@client.message_handler(commands = ['start'])
def get_user_info(message):

    markup_start = types.ReplyKeyboardMarkup()
    item_start = types.KeyboardButton('Начать')
    markup_start.add(item_start)

    client.send_message(message.chat.id, 'Приветствую!', reply_markup=markup_start)

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("C:/Users/Macris/PycharmProjects/teleg/joined.txt", "a")
        joinedFile.write(str(message.chat.id)+"\n")
        joinedUsers.add(message.chat.id)

    client.register_next_step_handler(message, start_1)

def start_1(message):
    if message.text == 'Начать' or message.text == 'Назад':

       start_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
       item_carr = types.KeyboardButton('Расписание')
       item_contacts = types.KeyboardButton('Контакты')
       item_tests = types.KeyboardButton('Работы')
       start_reply.add(item_carr, item_tests, item_contacts)

       client.send_message(message.chat.id, 'Выберите раздел.', reply_markup=start_reply)

    else:
        pass
    client.register_next_step_handler(message, carr)
    client.register_next_step_handler(message, contacts)
    client.register_next_step_handler(message, tests)

def carr(message):
    if message.text == 'Расписание':

        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_back = types.KeyboardButton('Назад')
        item_monday = types.KeyboardButton('Понедельник')
        item_tuesday = types.KeyboardButton('Вторник')
        item_wednesday = types.KeyboardButton('Среда')
        item_thursday = types.KeyboardButton('Четверг')
        item_friday = types.KeyboardButton('Пятница')
        markup_reply.row(item_back, item_monday, item_tuesday)
        markup_reply.row(item_wednesday, item_thursday, item_friday)

        client.send_message(message.chat.id, 'Выберите день недели.', reply_markup=markup_reply)
    else:
        pass
    client.register_next_step_handler(message, get_text)

def get_text(message):
    if message.text == 'Понедельник':
        client.send_message(message.chat.id, """
1. Всемирная история
2. Математика
3. Русский язык
4. Русская литература
5. Химия
6. Физика
7. Искусство
    """)
    elif message.text == 'Вторник':
        client.send_message(message.chat.id, """
1. Русский язык
2. Биология
3. Физкультура
4. Английский язык
5. Математика
6. Информатика
""")
    elif message.text == 'Среда':
        client.send_message(message.chat.id, """
1. Труд
2. Белорусский язык
3. География
4. Английский язык
5. Математика
6. ЧЗС
7. Классный час
""")
    elif message.text == 'Четверг':
        client.send_message(message.chat.id, """
1. Химия
2. История Беларуси
3. Математика
4. Физика/Биология
5. Математика/Химия
6. Белорусский язык
7. Белорусская литература
""")
    elif message.text == 'Пятница':
        client.send_message(message.chat.id, """
1. Биология
2. Русская литература
3. Физика
4. География
5. Английский язык
6. Математика
7. Физкультура
""")
    client.register_next_step_handler(message, get_text)
    client.register_next_step_handler(message, start_1)

def contacts(message):
    if message.text == 'Контакты':

        client.send_message(message.chat.id, """
А - 1234
Б - 1254
В - 135
Г - 13512  
""")
    else:
        pass

    client.register_next_step_handler(message, carr)
    client.register_next_step_handler(message, contacts)
    client.register_next_step_handler(message, tests)

def tests(message):
    if message.text == 'Работы':

        client.send_message(message.chat.id, """
Биология - 239
Математика - 123
""")
    else:
        pass

    client.register_next_step_handler(message, carr)
    client.register_next_step_handler(message, contacts)
    client.register_next_step_handler(message, tests)

@client.message_handler(commands=['special'])
def mess(message):
    for user in joinedUsers:
        client.send_message(user, message.text[message.text.find(' '):])

client.polling(none_stop=True, interval=0)
