import os  # ДОБАВЛЕНО ТОЛЬКО ДЛЯ ЛИЧНОГО УДОБСТВА И ЛУЧШЕЙ ЧИТАЕМОСТИ ПРИ ВЫВОДЕ В ТЕРМИНАЛ!!!!!


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 6
# -> 5
numbers = int(input("Введите кол-во элементов списка: "))
list1 = []
i = 0
s = set()
while i < numbers:
    list1.insert(i, int(input(f'Введите {i+1}-е число: ')))
    i += 1
search_numbers = int(input("Введите искомое число: "))
for element in list1:
    if search_numbers==element or search_numbers == element + 1 or search_numbers == element - 1:
       s.add(element)
print(f"Ближайшее число/числа к искомому: {s}")