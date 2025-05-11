from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from connectionDatabase.get_products import get_products

def get_products_list(type):

    names = get_products(type)

    products = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=txt[0])] for txt in names],
        resize_keyboard=True
    )

    return products

