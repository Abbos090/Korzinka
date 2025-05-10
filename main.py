import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

from Keyboards.menu import main_menu




dp = Dispatcher()

typ = None

class Form(StatesGroup):
    product = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=main_menu)
    await state.set_state(Form.product)


@dp.message(Form.product)
async def product_types(message: Message, state: FSMContext) -> None:
    global typ
    typ = message.text
    from Keyboards.productnames import products
    await message.answer("Mahsulot tanlang : ", reply_markup=products)



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())