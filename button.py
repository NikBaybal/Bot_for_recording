


async def time_button(callback: types.CallbackQuery):
    if callback.data == now.strftime("%d.%m.%Y"):
        j=0
        ikb2 = InlineKeyboardMarkup(row_width=1)
        ikb2.add(InlineKeyboardButton('назад', callback_data='back'))
        for j in free_time(now.strftime("%d.%m.%Y")):
            ikb2.add(InlineKeyboardButton(j, callback_data=j))
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text="выберите время или нажмите назад", reply_markup=ikb2)

async def time_button(a:str):
    gc = gspread.service_account(filename='my-project-2023-375610-9c983bcdb0e0.json')
    sh = gc.open("Записи")
    worksheet = sh.sheet1
    a_row = worksheet.find(a).row
    freetime=list()
    for i in range(1,8):
        if worksheet.cell(a_row,i).value is None:
            freetime.append(worksheet.cell(1,i).value)
    return freetime