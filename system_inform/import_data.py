from controller import *

def create_student():
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите номер класса ученика: ")
    id = get_student_id()
    write_data_student([id, surname, name, otch, birth, tel, adress])
    write_data_class([class_name, id, surname, name])
     


def search_student():
    word = input('Введите данные для поиска: ')
    data = get_all_students()
    if len(data) > 0:
        lst = []
        for item in data:
            if word in item:
                lst.append(item)
        if lst == []:
            print('Данные не найдены.')
        else:
            print("ID".center(5), "Фамилия".center(10), "Имя".center(10), "Отчество".center(10), "Дата рождения".center(10), "Телефон".center(10), "Адрес".center(10))
        print("----"*20)
        for item in lst:
            print(item[0].center(5), item[1].center(10), item[2].center(10), item[3].center(10), item[4].center(10), item[5].center(15), item[6].center(10))
    else:
        print('Данные не найдены.')