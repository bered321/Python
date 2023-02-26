import os
from data_create import id_number, name_data, surname_data, phone_data, adress_data

file_name = 'data.txt'

def input_data():
    print('Введите данные для записи в файл:\n ')
    id = id_number()
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    with open(file_name,'a', encoding = 'utf-8') as file:
        file.write(f'{id}; {name }; {surname }; {phone}; {adress}; \n')
        

def print_data():    
    if os.path.exists(file_name):
        print('Вывод данных из файла: ')
        with open(file_name, 'r', encoding="utf-8") as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("Файла не существует!!!")


def filter_data(filter_string):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        list_data = file.readlines()
        if '; ' in filter_string:
            list_filter = filter_string.split('; ')
        else:
            list_filter = [filter_string]

        is_found = False

        for element in list_data:    
            temp_record = element.split('; ') 
            for record in temp_record: 
                for element_filter in list_filter: 
                    if element_filter.lower() in record.lower() and len(element_filter.lower())==len(record.lower()):
                        print(element)                     
                        is_found = True               
        if is_found == False:                   
            print('Таких записей как: ', element_filter,' нет ')

        
def delete_data(delete_string):
    with open(file_name, "r", encoding="utf-8") as file:
        list_data = file.readlines()
        for i in range(len(list_data)):
            if delete_string == int(list_data[i].split(";")[0]):
                list_data.pop(i) 
                break
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(len(list_data)):
            temp_record = list_data[i].split(";")
            file.write(f"{temp_record[0]};{temp_record[1]};{temp_record[2]};{temp_record[3]};{temp_record[4]};\n")


def swap_value(old_value, new_value):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        Flag = False

        for line_i in range(len(list_data)):
            if Flag: break

            record_list_data = list_data[line_i].split('; ')
            for element in range(len(record_list_data)):
                count = 0
                if  old_value in record_list_data[element]:
                    record_list_data[element] = new_value

                    new_line = '; '.join(record_list_data)
                    list_data[line_i] = new_line
                    Flag = True
                    print('Элемент успешно изменён!')
                    break
                else:
                    count +=1
        if count == len(record_list_data):
            print('Такого элемента нет.')
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in list_data:
                file.write(line + '\n')           