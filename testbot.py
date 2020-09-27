from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;
import telebot
from telebot import types


TG_TOKEN = "1004232792:AAH9NbYZhmXYBZNaNAxTYFVSQFMJoTw7OrM"

bot = telebot.TeleBot("1004232792:AAH9NbYZhmXYBZNaNAxTYFVSQFMJoTw7OrM")

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="Страница моего создателя в ВК", url="https://vk.com/psychocave")
    nextpage_button = types.InlineKeyboardButton(text="Перейти на следующую страницу", callback_data="next")
    faq_button = types.InlineKeyboardButton(text="Часто задаваемые вопросы (FAQ)", callback_data="faq")
    keyboard.add(faq_button, nextpage_button, url_button)
    bot.send_message(message.chat.id, "Добро пожаловать!👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle_start_text(message):
    if message.text == "Максон":
        bot.send_message(message.chat.id, "Да\nДа Да\nЭт я)")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="Страница моего создателя в ВК", url="https://vk.com/psychocave")
    nextpage_button = types.InlineKeyboardButton(text="Перейти на следующую страницу", callback_data="next")
    faq_button = types.InlineKeyboardButton(text="Часто задаваемые вопросы (FAQ)", callback_data="faq")
    keyboard.add(faq_button, nextpage_button, url_button)
    bot.send_message(message.chat.id, "Добро пожаловать!👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
        if call.data == "faq":
            keyboard = types.InlineKeyboardMarkup (row_width=1)
            qa1_button = types.InlineKeyboardButton(text="Распитие в общественном месте", callback_data = "qa1")
            back_button = types.InlineKeyboardButton(text="Вернуться назад", callback_data = "back")
            keyboard.add(qa1_button, back_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="❓ Ниже представлен список часто задаваемых вопросов ❓", reply_markup=keyboard)
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Cписок задаваемых вопросов!")
        elif call.data == "back":
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Страница моего создателя в ВК", url="https://vk.com/psychocave")
            nextpage_button = types.InlineKeyboardButton(text="Перейти на следующую страницу", callback_data="next")
            faq_button = types.InlineKeyboardButton(text="Часто задаваемые вопросы (FAQ)", callback_data="faq")
            keyboard.add(faq_button, nextpage_button, url_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать!👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖", reply_markup=keyboard)
        elif call.data == "qa1":
            keyboard = types.InlineKeyboardMarkup (row_width=1)
            back_button = types.InlineKeyboardButton(text="Вернуться назад", callback_data = "back")
            keyboard.add(back_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вам могут предъявить штраф, а так же могут забрать в участок.", reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()


##Program by h350yam
