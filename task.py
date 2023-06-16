task_types = [{1:"translate"}, {2:"insert letter"}]
from telebot import types
from random import randint
import random
import string
class Task():
    task_id = 0
    task_word = ""
    task_right_answer = ""
    task_btn_1=""
    task_btn_2 = ""
    task_btn_3 = ""
    task_btn_4 = ""
    task_descr = ""
    def task_insert_letter(self, user_id, mysql_):
        word, translate = mysql_.get_random_word(user_id)
        #self.task_word = word
        id_letter = randint(0, len(word))

        print("letter to replace id",id_letter)
        letter = word[id_letter]
        self.task_word = word.replace(word[id_letter], '_', 1)
        self.task_right_answer = word[id_letter]
        self.task_descr = f'Какая буква пропущена в слове {self.task_word}'
        unwanted_chars = []
        unwanted_chars.append(word[id_letter])
        wrong_letter_1 = random.choice([s for s in string.ascii_lowercase if s not in unwanted_chars])
        unwanted_chars.append(wrong_letter_1)
        wrong_letter_2 = random.choice([s for s in string.ascii_lowercase if s not in unwanted_chars])
        unwanted_chars.append(wrong_letter_2)
        wrong_letter_3 = random.choice([s for s in string.ascii_lowercase if s not in unwanted_chars])
        btn_correct_ind = randint(1, 4)
        if btn_correct_ind == 1:
            # correct answer
            self.task_btn_1 = types.InlineKeyboardButton(word[id_letter], callback_data='1')
            # wrong answers

            self.task_btn_2 = types.InlineKeyboardButton(wrong_letter_1, callback_data='0')
            self.task_btn_3 = types.InlineKeyboardButton(wrong_letter_2, callback_data='0')
            self.task_btn_4 = types.InlineKeyboardButton(wrong_letter_3, callback_data='0')

        elif btn_correct_ind == 2:
            self.task_btn_2 = types.InlineKeyboardButton(word[id_letter], callback_data='1')
            # wrong answers
            self.task_btn_1 = types.InlineKeyboardButton(wrong_letter_1, callback_data='0')
            self.task_btn_3 = types.InlineKeyboardButton(wrong_letter_2, callback_data='0')
            self.task_btn_4 = types.InlineKeyboardButton(wrong_letter_3, callback_data='0')
        elif btn_correct_ind == 3:
            self.task_btn_3 = types.InlineKeyboardButton(word[id_letter], callback_data='1')
            # wrong answers
            self.task_btn_2 = types.InlineKeyboardButton(wrong_letter_1, callback_data='0')
            self.task_btn_1 = types.InlineKeyboardButton(wrong_letter_2, callback_data='0')
            self.task_btn_4 = types.InlineKeyboardButton(wrong_letter_3, callback_data='0')
        elif btn_correct_ind == 4:
            self.task_btn_4 = types.InlineKeyboardButton(word[id_letter], callback_data='1')
            # wrong answers
            self.task_btn_2 = types.InlineKeyboardButton(wrong_letter_1, callback_data='0')
            self.task_btn_3 = types.InlineKeyboardButton(wrong_letter_2, callback_data='0')
            self.task_btn_1 = types.InlineKeyboardButton(wrong_letter_3, callback_data='0')



    def task_translate(self, user_id, mysql_):
        word, translate = mysql_.get_random_word(user_id)
        extra_words = mysql_.get_trhee_extra_words(user_id, word)
        self.task_word = word
        self.task_right_answer = translate
        btn_correct_ind = randint(1,4)
        if btn_correct_ind == 1:
            # correct answer
            self.task_btn_1 = types.InlineKeyboardButton(translate, callback_data='1')
            # wrong answers
            self.task_btn_2 = types.InlineKeyboardButton(extra_words[0][2], callback_data='0')
            self.task_btn_3 = types.InlineKeyboardButton(extra_words[1][2], callback_data='0')
            self.task_btn_4 = types.InlineKeyboardButton(extra_words[2][2], callback_data='0')

        elif btn_correct_ind == 2:
            self.task_btn_2 = types.InlineKeyboardButton(translate, callback_data='1')
            # wrong answers
            self.task_btn_1 = types.InlineKeyboardButton(extra_words[0][2], callback_data='0')
            self.task_btn_3 = types.InlineKeyboardButton(extra_words[1][2], callback_data='0')
            self.task_btn_4 = types.InlineKeyboardButton(extra_words[2][2], callback_data='0')
        elif btn_correct_ind == 3:
            self.task_btn_3 = types.InlineKeyboardButton(translate, callback_data='1')
            # wrong answers
            self.task_btn_2 = types.InlineKeyboardButton(extra_words[0][2], callback_data='0')
            self.task_btn_1 = types.InlineKeyboardButton(extra_words[1][2], callback_data='0')
            self.task_btn_4 = types.InlineKeyboardButton(extra_words[2][2], callback_data='0')
        elif btn_correct_ind == 4:
            self.task_btn_4 = types.InlineKeyboardButton(translate, callback_data='1')
            # wrong answers
            self.task_btn_2 = types.InlineKeyboardButton(extra_words[0][2], callback_data='0')
            self.task_btn_3 = types.InlineKeyboardButton(extra_words[1][2], callback_data='0')
            self.task_btn_1 = types.InlineKeyboardButton(extra_words[2][2], callback_data='0')
        self.task_descr = f"Переведите слово: {self.task_word}"





