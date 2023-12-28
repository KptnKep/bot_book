from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return callback.data.isdigit()

class IsDelBookMarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return callback.data.endswith('del') and callback.data[:-3].isdigit()