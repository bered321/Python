from logger import input_data, print_data, filter_data, delete_data, swap_value
from data_create import old_value, new_value


def interface():
    while True:
        print(""" Выберите режим работы:
                1 - запись данных
                2 - вывод данных
                3 - поиск данных по параметрам
                4 - удаление данных
                5 - замена данных
                6 - выход
                """)

        operation_number = int(input('Введите номер операции: '))

        if operation_number == 1:
            input_data()
        elif operation_number == 2:
            print_data()
        elif operation_number == 3:
            print("Введите параметры поиска через ';': ")
            filter_string = input()
            filter_data(filter_string)
        elif operation_number == 4:
            delete_string = int(input("Введите номер строки для удаления: "))
            delete_data(delete_string)
        elif operation_number == 5:
            swap()
        elif operation_number == 6:
            break

def swap():
    print(""" Выберите элемент справочника, который хотите заменить:
              1 - порядковый номер абанента
              2 - имя абонета
              3 - фамилия абонента
              4 - телефон абонента
              5 - адрес абонента
              """)
    operation_number = int(input('Введите номер операции: '))

    while operation_number < 1 or operation_number > 5:
        print('Вы ввели некорректный номер операции!\n',
              'Введите корректный номер операции! ')
        operation_number = int(input('Введите номер операции: '))

    if operation_number == 1:
        swap_value(old_value(), new_value())
    elif operation_number == 2:
        swap_value(old_value(), new_value())
    elif operation_number == 3:
        swap_value(old_value(), new_value())
    elif operation_number == 4:
        swap_value(old_value(), new_value())
    elif operation_number == 5:
        swap_value(old_value(), new_value())
