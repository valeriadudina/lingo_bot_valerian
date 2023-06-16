import telebot
from telebot import types
from NewWords import NewWords
from MySQL import MySQL
from User import User
from random import randint
from task import Task, task_types
bot_token = "6261932886:AAHB_4UGpUX5kvT8omdu1vp-fxCpNMQI_ag"
bot = telebot.TeleBot(bot_token)
mysql_ = MySQL()
task = Task()
global mode
def get_user(tg_nikname, name):
    user_id = mysql_.search_user(tg_nikname)
    print(user_id)
    if user_id == 0:
        user_id, user_name, user_tg_nikname = mysql_.insert_user(name=name, tg_nikname=tg_nikname)
    else:
        user_id, user_name, user_tg_nikname = mysql_.get_user_by_id(user_id)
    user_ = User(user_id, user_name, user_tg_nikname)
    return user_
#start bot
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Добавить слова в словарь")
    btn2 = types.InlineKeyboardButton("Выполнить задание", callback_data='task')
    btn3 = types.InlineKeyboardButton("Учить слова")
    markup.add(btn1, btn2, btn3)
    print(message.from_user)
    name = message.from_user.first_name +" "+ message.from_user.last_name
    tg_nikname = message.from_user.username

    global user
    user = get_user(tg_nikname, name)
    bot.send_message(message.from_user.id, "Добавьте первое слово в свой словарь", reply_markup=markup)


@bot.message_handler(func= lambda message: True)
def add_newwords(message):

    print(message.text)
    print("user")
    if 'user' not in globals():
        name = message.from_user.first_name + " " + message.from_user.last_name
        tg_nikname = message.from_user.username
        global user
        user = get_user(tg_nikname, name)

    print(user.user_id)

    if message.text == "Добавить слова в словарь":
        global new_words
        new_words = NewWords
        bot.send_message(message.from_user.id, 'Напишите иностранное слово')
    elif message.text == "Выполнить задание":
        global mode
        mode = 'task'
        print('do a task')
        #id = randint(1, 2)
        id = 1
        if id == 1:
            task.task_id = 1
            task.task_translate(user.user_id, mysql_)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(task.task_btn_1, task.task_btn_2, task.task_btn_3, task.task_btn_4)
            bot.send_message(message.from_user.id, f'{task.task_descr}',
                             reply_markup=markup)
        elif id == 2:
            task.task_id = 2
            task.task_insert_letter(user.user_id, mysql_)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(task.task_btn_1, task.task_btn_2, task.task_btn_3, task.task_btn_4)
            bot.send_message(message.from_user.id, f'{task.task_descr}',
                             reply_markup=markup)

    elif task.task_id != 0:
        print('task id not 0')
        if message.text == task.task_right_answer:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardButton("Добавить слова в словарь")
            btn2 = types.InlineKeyboardButton("Выполнить задание", callback_data='task')
            btn3 = types.InlineKeyboardButton("Учить слова")
            markup.add(btn1, btn2, btn3)
            task.task_id = 0
            bot.send_message(message.from_user.id, f'Верно!',
                             reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(task.task_btn_1, task.task_btn_2, task.task_btn_3, task.task_btn_4)
            bot.send_message(message.from_user.id, f'Неверно, попробуй еще раз)\n{task.task_descr}',
                             reply_markup=markup)

    elif message.text == "Учить слова":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Добавить слова в словарь")
        btn2 = types.InlineKeyboardButton("Выполнить задание", callback_data='task')
        btn3 = types.InlineKeyboardButton("Учить слова")
        #bot.send_message(message.from_user.id, f'Добавлено новое слово {word} - {translate}', reply_markup=markup)

    else:
        if new_words.word == "":
            print(message.text)

            new_words.word = message.text
            bot.send_message(message.from_user.id, 'Напишите перевод этого слова')
        elif new_words.translate =="":
            print(message.text)
            new_words.translate = message.text
            mysql_.insert_word(user, new_words )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.InlineKeyboardButton("Добавить слова в словарь")
            btn2 = types.InlineKeyboardButton("Выполнить задание", callback_data = 'task')
            btn3 = types.InlineKeyboardButton("Учить слова")
            markup.add(btn1, btn2, btn3)
            word = new_words.word
            translate = new_words.translate
            new_words.translate = ""
            new_words.word = ""
            bot.send_message(message.from_user.id, f'Добавлено новое слово {word} - {translate}',reply_markup=markup )




if __name__=='__main__':
    bot.polling(none_stop=True, interval=0)