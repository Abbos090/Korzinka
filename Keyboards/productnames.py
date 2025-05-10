from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from connectionDatabase.get_products import get_products
from main import typ

names = get_products(typ)

products = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=txt)] for txt in names],
    resize_keyboard=True
)



