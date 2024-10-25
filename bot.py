import telebot
import logging
from config import TOKEN
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from logic import get_schedule_for_monday, get_schedule_for_tuesday, get_schedule_for_wednesday, get_schedule_for_thursday, get_schedule_for_friday

logging.basicConfig(level=logging.INFO)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(TOKEN)

# Функция для создания кнопок с днями недели
def start():
    keyboard = [
        [InlineKeyboardButton("Понедельник", callback_data='monday')],
        [InlineKeyboardButton("Вторник", callback_data='tuesday')],
        [InlineKeyboardButton("Среда", callback_data='wednesday')],
        [InlineKeyboardButton("Четверг", callback_data='thursday')],
        [InlineKeyboardButton("Пятница", callback_data='friday')],  
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

# Обработчик выбора кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        # Определяем расписание по дню недели
        if call.data == 'monday':
            schedule = get_schedule_for_monday()
        elif call.data == 'tuesday':
            schedule = get_schedule_for_tuesday()
        elif call.data == 'wednesday':
            schedule = get_schedule_for_wednesday()
        elif call.data == 'thursday':
            schedule = get_schedule_for_thursday()
        elif call.data == 'friday':
            schedule = get_schedule_for_friday()
        
        # Обновляем сообщение с новым расписанием
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"Расписание на {call.data.capitalize()}:\n\n{schedule}",
            reply_markup=start()  # Оставляем кнопки для нового выбора
        )
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Ошибка: {e}")

# Функция для отправки начального сообщения с кнопками
@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply_markup = start()
    bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=reply_markup)

# Запуск бота
try:
    bot.polling(non_stop=True)
except Exception as e:
    logger.error(f"Polling failed: {e}")
