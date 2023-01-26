from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import date
import pandas as pd
from config import TOKEN_API
from sheet import free_time
from datetime import timedelta

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)  # default - False
b1 = KeyboardButton('/информация')
b2 = KeyboardButton('/услуги')
b3 = KeyboardButton('/локация')
b4 = KeyboardButton('/запись')
kb.add(b1).insert(b2).add(b3).insert(b4)

ikb = InlineKeyboardMarkup(row_width=1)
now = date.today()
days = pd.date_range(now, periods=4, freq="D")
WEEKDAYS = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']


for i in days:
    weekday_index = i.weekday()
    w = WEEKDAYS[weekday_index]
    ikb.add(InlineKeyboardButton(f'{i.strftime("%d.%m.")}'+w, callback_data=f'{i.strftime("%d.%m.%Y")}'))


HELP_COMMAND = """
вся необходимая информация"""







async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Привет, <b>добро</b> пожаловать в наш бот!</em>',
                         parse_mode="HTML",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['запись'])
async def rec_command(message: types.Message):
    await message.answer('<em>Выбери дату:</em>',
                         parse_mode="HTML",
                         reply_markup=ikb)
    await message.delete()


@dp.message_handler(commands=['информация'])
async def info_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['услуги'])
async def uslugi_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='услуга 1\nуслуга 2\nуслуга 3',
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['локация'])
async def location_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHfQfXQD-FhEfRlBCrWZiLi5PMIYWLRr2d6A&usqp=CAU')
    await message.delete()


@dp.callback_query_handler()
async def time_callback(callback: types.CallbackQuery):
    if callback.data == now.strftime("%d.%m.%Y"):
        j=0
        ikb2 = InlineKeyboardMarkup(row_width=1)
        ikb2.add(InlineKeyboardButton('назад', callback_data='back'))
        for j in free_time(now.strftime("%d.%m.%Y")):
            ikb2.add(InlineKeyboardButton(j, callback_data='23'))
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text="выберите время или нажмите назад", reply_markup=ikb2)


    elif callback.data == (now+timedelta(days=1)).strftime("%d.%m.%Y"):
        j = 0
        ikb2 = InlineKeyboardMarkup(row_width=1)
        ikb2.add(InlineKeyboardButton('назад', callback_data='back'))
        for j in free_time((now+timedelta(days=1)).strftime("%d.%m.%Y")):
            ikb2.add(InlineKeyboardButton(j, callback_data='23'))
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text="выберите время или нажмите назад", reply_markup=ikb2)

    elif callback.data == (now+timedelta(days=2)).strftime("%d.%m.%Y"):
        j = 0
        ikb2 = InlineKeyboardMarkup(row_width=1)
        ikb2.add(InlineKeyboardButton('назад', callback_data='back'))
        for j in free_time((now+timedelta(days=2)).strftime("%d.%m.%Y")):
            ikb2.add(InlineKeyboardButton(j, callback_data='23'))
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text="выберите время или нажмите назад", reply_markup=ikb2)

    elif callback.data == (now+timedelta(days=3)).strftime("%d.%m.%Y"):
        j = 0
        ikb2 = InlineKeyboardMarkup(row_width=1)
        ikb2.add(InlineKeyboardButton('назад', callback_data='back'))
        for j in free_time((now + timedelta(days=3)).strftime("%d.%m.%Y")):
            ikb2.add(InlineKeyboardButton(j, callback_data='23'))
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text="выберите время или нажмите назад", reply_markup=ikb2)
    elif callback.data == 'back':
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text="выберите дату", reply_markup=ikb)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
