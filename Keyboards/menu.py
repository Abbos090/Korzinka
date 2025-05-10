from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from connectionDatabase.get_typses import get_type

typses = get_type()

main_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=txt)] for txt in typses],
    resize_keyboard=True
)

