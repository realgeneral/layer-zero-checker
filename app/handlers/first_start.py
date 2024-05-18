from datetime import date

from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InputFile
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.states.UserFollowing import UserFollowing


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    buttons = [
        KeyboardButton(text="💪 LFGGG !"),
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

    await UserFollowing.get_wallets.set()
    photo_path = 'app/checker.JPEG'  # Local path or URL to the image
    caption = f"👋 Do u know we have a <a href='https://t.me/ARNI_Concepts'>channel</a>?"
    photo = InputFile(photo_path)
    await message.answer_photo(photo,
                               caption=caption,
                               parse_mode=types.ParseMode.HTML,
                               reply_markup=reply_markup)

@dp.message_handler(Text(equals="💪 LFGGG !"), state=UserFollowing.get_wallets)
async def first_free_use(message: types, state: FSMContext):
    await UserFollowing.get_wallets.set()
    mess = (f"*Found 803093 ineligible wallets.*\n\n ")
    await bot.send_message(message.from_user.id, mess + "🔽 *DROP YOUR WALLETS BELOW AND PRESS ENTER!*  \n\n"
                                                 "*Format: (max. 50)* \n"
                                                 "• _Wallet adress1_\n"
                                                 "• _Wallet adress2_\n"
                                                 "• _Wallet adress3_",
                           parse_mode=types.ParseMode.MARKDOWN,
                           reply_markup=ReplyKeyboardRemove())



