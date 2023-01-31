from export_data import *
from import_data import *


def user_choose():
    print('''Добро пожаловать в справочник школы! 
                Выберите действие:  
                1.Добавить ученика  
                2.Поиск ученика   
                3.Вывести список всех учеников
                4.Вывести список всех учеников
                5.Выход''')
    choose = input("Введите цифру выбора: ")
    if choose == '1':
        create_student()
        print('Выполнено!')
        user_choose()
    elif choose == '2':
        search_student()
        print('Выполнено!')
        user_choose()
    elif choose == '3':
        to_console_st(get_all_students())
        print('Выполнено!')
        user_choose()
    elif choose == '4':
        to_console_cl(get_all_classes())
        print('Выполнено!')
        user_choose()
    elif choose == '5':
        return
    else:
        print("Вы ввели некорректное значение, повторите ввод!")
        user_choose()
