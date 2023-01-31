from import_data import *


def to_console_st(data):
    if len(data) > 0:
        print("ID".center(5), "Фамилия".center(10), "Имя".center(10), "Отчество".center(10), "Дата рождения".center(10), "Телефон".center(10), "Адрес".center(10))
        print("----"*20)
        for item in data:
            print(item[0].center(5), item[1].center(10), item[2].center(10), item[3].center(10), item[4].center(10), item[5].center(15), item[6].center(10))
    else:
        print("Данные отсутствуют.")

def to_console_cl(data):
    if len(data) > 0:
        print("Класс".center(10), "ID".center(10), "Фамилия".center(10), "Имя".center(10))
        print("--"*20)
        for item in data:
            print(item[0].center(10), item[1].center(10), item[2].center(10), item[3].center(10))
    else:
        print("Данные отсутствуют.")

