import re
from typing import Union

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ParseMode

from .keyboards import menu_markup, days_keyboard, menu_cd, shift_markup, days_shift_keyboard
from ..services import get_shift_days, get_month_text


def register_handlers(dp: Dispatcher):
    # Register your handlers here
    dp.register_message_handler(simple_handler, commands=["shedule_sift"])
    dp.register_message_handler(show_menu, commands=["menu"])
    dp.register_callback_query_handler(navigate, menu_cd.filter())


# Create your handlers here
async def simple_handler(message: Message):
    await message.answer('Hello from "SheduleSift" app!')


async def show_menu(message: Union[CallbackQuery, Message], **kwargs):
    markup = await menu_markup()
    if isinstance(message, Message):
        await message.answer("Выбери месяц", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def days(callback: CallbackQuery, month, **kwargs):
    markup = await days_keyboard(month=month)
    await callback.message.edit_text(text='Выбери день', reply_markup=markup)


async def day_shift(callback: CallbackQuery, month, item_id, **kwargs):
    markup = await shift_markup(month=month, item_id=item_id)
    await callback.message.edit_text(text='Выбери смену', reply_markup=markup)


async def day_shift_final(callback: CallbackQuery, month, item_id, shift, **kwargs):
    markup = await days_shift_keyboard(month=month, item_id=item_id, shift=shift)
    text = await get_shift_days(month=month, item_id=item_id, shift=shift)
    month = await get_month_text(numbr=text[0].month)
    a= f'<b>{text[0].day_month} {month[0]} Смена {text[0].shift}:</b> \n<b>Мастер:</b> {await text[0].master} \n\n<b>Слесаря:</b> {await text[0].locksmith}\n                  {await text[0].locksmith1}\n                  {await text[0].locksmith2}\n                  {await text[0].locksmith3}\n                  {await text[0].locksmith4}\n                  {await text[0].locksmith5}\n                  {await text[0].locksmith6}\n                  {await text[0].locksmith7}\n                  {await text[0].locksmith8} \n\n<b>Электрики:</b> {await text[0].electrician}\n                      {await text[0].electrician1}\n                      {await text[0].electrician2}\n                      {await text[0].electrician3}\n                      {await text[0].electrician4}\n                      {await text[0].electrician5}\n                      {await text[0].electrician6}\n                      {await text[0].electrician7}\n                      {await text[0].electrician8} \n\n<b>Киповец:</b> {await text[0].kip} \n\n<b>Наладчик оборудования металлопокрытия:</b> {await text[0].paint_adjuster}'
    a= re.sub(r'\n                  None|\n                      None', '', a)
    await callback.message.edit_text(text=a, reply_markup=markup, parse_mode=ParseMode.HTML)


async def navigate(cal: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    item_id = int(callback_data.get('item_id'))
    month = int(callback_data.get('month'))
    shift = int(callback_data.get('shift'))

    levels = {
        "0": show_menu,
        "1": days,
        '2': day_shift,
        '3': day_shift_final
    }
    current_level_function = levels[current_level]
    await current_level_function(cal, item_id=item_id, month=month, shift=shift)
