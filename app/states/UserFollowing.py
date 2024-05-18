from aiogram.dispatcher.filters.state import State, StatesGroup


class UserFollowing(StatesGroup):
    check_subscribe = State()
    get_wallets = State()
