import random
import os

import aiogram
from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InputFile
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from datetime import datetime, date, timedelta
from app.utils.checker import Checker


from app.create_bot import dp, bot
from app.states.UserFollowing import UserFollowing

checker = Checker()


@dp.message_handler(state=UserFollowing.get_wallets)
async def statistic_of_wallets(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    message_reply = ""
    addresses = [addr.strip().lower() for addr in message.text.split('\n') if addr.strip()]

    if len(addresses) == 0:
        message_reply += "🙁 Invalid address"

        await UserFollowing.get_wallets.set()
        await message.answer(message_reply, reply_markup=ReplyKeyboardRemove(), parse_mode=types.ParseMode.MARKDOWN)
        return

    wait_message = await message.answer("⏳ Getting information about wallets ...")

    eligible_wallets, ineligible_wallets = checker.check_wallets(addresses)

    statistic = f"✅ Eligible wallets: {len(eligible_wallets)}\n🚫 Ineligible wallets: {len(ineligible_wallets)}\n"

    await bot.delete_message(chat_id=wait_message.chat.id, message_id=wait_message.message_id)
    await message.answer(statistic, reply_markup=ReplyKeyboardRemove(), parse_mode=types.ParseMode.MARKDOWN)

    # Create results directory if it doesn't exist
    if not os.path.exists("results"):
        os.makedirs("results")

    eligible_file_path = f"results/eligible_wallets_{user_id}.txt"
    ineligible_file_path = f"results/ineligible_wallets_{user_id}.txt"

    if eligible_wallets:
        with open(eligible_file_path, 'w') as file:
            for wallet in eligible_wallets:
                file.write(wallet + '\n')
        await message.answer_document(InputFile(eligible_file_path))
        os.remove(eligible_file_path)

    if ineligible_wallets:
        with open(ineligible_file_path, 'w') as file:
            for wallet in ineligible_wallets:
                file.write(wallet + '\n')
        await message.answer_document(InputFile(ineligible_file_path))
        os.remove(ineligible_file_path)  # Удаляем файл после отправки

    await message.answer("🔄 *Check another one!*", reply_markup=ReplyKeyboardRemove(),
                         parse_mode=types.ParseMode.MARKDOWN)
    await UserFollowing.get_wallets.set()