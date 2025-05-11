from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from connectionDatabase.get_typses import get_type

def get_main_menu():
    typses = get_type()

    main_menu = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=txt[0])] for txt in typses],
        resize_keyboard=True
    )

    return main_menu