import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

from config import TOKEN
from Keyboards.menu import get_main_menu
from Keyboards.productnames import get_products_list
from connectionDatabase.get_product_quantity import get_quantity
from Keyboards.ha_yoq import ha_yoq


dp = Dispatcher()

class Form(StatesGroup):
    type = State()
    product = State()
    quantity = State()
    price = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=get_main_menu())
    await state.set_state(Form.type)

typ = None
produc = None
quantit = None

@dp.message(Form.type)
async def products_type(message: Message, state: FSMContext):
    global typ
    typ = message.text
    await message.answer("Mahsulot tanlang : ", reply_markup=get_products_list(message.text))
    await state.set_state(Form.product)


@dp.message(Form.product)
async def products_product(message: Message, state: FSMContext) -> None:
    global produc
    produc = message.text
    await message.answer("Qancha olishingizni kiriting : ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.quantity)


@dp.message(Form.quantity)
async def product_quantity(message: Message, state: FSMContext):
    if message.text.isdigit() and message.text > 0:
        global quantit
        quantit = message.text
        await state.set_state(Form.price)
        await message.answer("Yaxshi son")
    else:
        await message.answer("Son kiriting !")

@dp.message(Form.price)
async def product_price(message: Message):
    await message.answer("Men price holatiga o'tdim")
    global typ
    global produc
    global quantit
    narx = get_quantity(typ,produc,quantit)
    await message.answer(f"Tanlagan mahsulotingiz narxi: {narx}")
    await message.answer("Olasizmi ?", reply_markup=ha_yoq)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())