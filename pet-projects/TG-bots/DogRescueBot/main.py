
import telebot
from telebot import types
from datetime import datetime
from sql import *

bot = telebot.TeleBot()
db = "test.db"


conn = sqlite_open_connection(db)


# Обработчик команд '/start'.
@bot.message_handler(commands=['start'])
def handle_start(message):
    print("Со мной начал диалог пользователь " + str(message.from_user.id))
    bot.send_message(message.from_user.id,
                     "Добрый день! \n" +
                     "Я создан для помощи тем, кто заботится о животных.")
    sqlite_insert_chat_status(str(message.from_user.id), str(datetime.now()))


# Обработчик команд '/blacklist'.
@bot.message_handler(commands=['blacklist'])
def handle_start_help(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    key_check = types.KeyboardButton(text="Проверить")
    key_insert = types.KeyboardButton(text="Добавить")
    keyboard.add(key_check)
    keyboard.add(key_insert)
    bot.send_message(message.from_user.id, "Пожалуйста, укажите, что вы хотите сделать.", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower() == "проверить":
        pass

    elif message.text.lower() == "добавить" and sqlite_get_status(message.from_user.id)[0] != "create new line":
        new_bl_id = sqlite_insert_new_bl_line()
        new_status = "create new line"
        sqlite_update_chat_status_full(
            chat_id=message.from_user.id,
            chat_status=new_status,
            user_in_process=new_bl_id,
            last_update=str(datetime.now())
        )
        bot.send_message(message.from_user.id, "Пожалуйста, введите имя.")

    elif sqlite_get_status(message.from_user.id)[0] == "create new line":
        sqlite_update_bl_line(line_id=sqlite_get_status(message.from_user.id)[1], name=message.text)
        new_status = "name updated"
        sqlite_update_chat_status_only(
            chat_id=message.from_user.id,
            chat_status=new_status,
            last_update=str(datetime.now())
        )
        bot.send_message(message.from_user.id, "Пожалуйста, укажите фамилию")

    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")


bot.polling(none_stop=True, interval=0)


# Обработчик команд '/help'.
@bot.message_handler(commands=['help'])
def handle_start_help(message):
    pass


# Обработчик команд '/animals'.
@bot.message_handler(commands=['animals'])
def handle_start_help(message):
    pass


# Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "check":
        bot.send_message(call.message.from_user.id, "Да что там проверять, виновен!")

    elif call.data == "insert":
        bot.send_message(call.message.from_user.id, "Достаю тетрадь смерти..")


bot.polling(none_stop=True, interval=0)


sqlite_close_connection(conn)
