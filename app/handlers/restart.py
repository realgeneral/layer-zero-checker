from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from app.create_bot import dp, bot
from app.handlers.first_start import first_free_use
from app.states import UserFollowing


@dp.message_handler(commands=['restart'], state='*')
async def restart_cmd(message: types.Message, state: FSMContext):
    await UserFollowing.get_wallets.set()
    await bot.send_message(message.from_user.id, "🔽 *DROP YOUR WALLETS BELOW AND PRESS ENTER!*  \n\n"
                                                 "*Format: (max. 50)* \n"
                                                 "• _Wallet adress1_\n"
                                                 "• _Wallet adress2_\n"
                                                 "• _Wallet adress3_",
                           parse_mode=types.ParseMode.MARKDOWN,
                           reply_markup=ReplyKeyboardRemove())