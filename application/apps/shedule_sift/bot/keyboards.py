from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.callback_data import CallbackData

from ..services import get_schedule, get_shift_days, get_month

menu_cd = CallbackData("show_menu", "level", 'month', 'shift', "item_id")


def make_callback_data(level, item_id="0", month=0, shift=0):
    return menu_cd.new(level=level, item_id=item_id, month=month, shift=shift)


async def menu_markup():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()
    items = await get_month()
    for item in items:
        button_text = f"{item.name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, month=item.numbr)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


async def days_keyboard(month):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    items = await get_schedule(month)
    for item in items:
        button_text = f"{item.day_month}"
        callback_data = make_callback_data(level=CURRENT_LEVEL+1, item_id=item.day_month, month=month)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, month=month))
    )
    return markup


async def shift_markup(month, item_id):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='1',
                             callback_data=make_callback_data(level=CURRENT_LEVEL + 1, month=month, item_id=item_id, shift=1)),
        InlineKeyboardButton(text='2',
                             callback_data=make_callback_data(level=CURRENT_LEVEL + 1, month=month, item_id=item_id, shift=2)),
        InlineKeyboardButton(text='3',
                             callback_data=make_callback_data(level=CURRENT_LEVEL + 1, month=month, item_id=item_id, shift=3)),
    ]])
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, item_id=item_id, month=month))
    )
    return markup


async def days_shift_keyboard(month, item_id, shift):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, item_id=item_id, month=month, shift=shift))
    )
    return markup