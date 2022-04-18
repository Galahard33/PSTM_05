from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("menu", "Показать меню расписания"),
            types.BotCommand("now", "Показеть текущую смену"),
            types.BotCommand("today", "Показеть все смены на сегодня"),
        ]
    )
