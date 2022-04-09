from . import models
from typing import List


async def get_schedule(month)-> List[models.Month]:
    return await models.Month.filter(month=month, shift=1)


async def get_shift_days(month, item_id, shift) -> List[models.Month]:
    return await models.Month.filter(month=month, day_month=item_id, shift=shift)


async def get_month()-> List[models.NameMonth]:
    return await models.NameMonth.all()


async def get_month_text(numbr)-> List[models.NameMonth]:
    return await models.NameMonth.filter(numbr=numbr)