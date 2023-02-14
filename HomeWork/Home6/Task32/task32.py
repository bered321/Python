import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

list1 = list(input("Введите элементы массива: ").split())
min_number = int(input("Введите минимум: "))
max_number = int(input("Введите максимум: "))
for i in range(len(list1)):
    if min_number <= int(list1[i]) <= max_number:
        print(f"Номер элемента попадающего в диапозон: {i}")
