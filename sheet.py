import gspread
def free_time(a:str)->list:
    gc = gspread.service_account(filename='my-project-2023-375610-9c983bcdb0e0.json')
    sh = gc.open("Записи")
    worksheet = sh.sheet1
    a_row = worksheet.find(a).row
    freetime=list()
    for i in range(1,8):
        if worksheet.cell(a_row,i).value is None:
            freetime.append(worksheet.cell(1,i).value)
    return freetime
