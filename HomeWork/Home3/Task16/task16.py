import os  # ДОБАВЛЕНО ТОЛЬКО ДЛЯ ЛИЧНОГО УДОБСТВА И ЛУЧШЕЙ ЧИТАЕМОСТИ ПРИ ВЫВОДЕ В ТЕРМИНАЛ!!!!!


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 3
# -> 1

numbers = int(input("Введите кол-во элементов списка: "))
list1 = []
i = 0
count = 0
while i < numbers:
    list1.insert(i, int(input(f'Введите {i+1}-е число: ')))
    i += 1
search_numbers = int(input("Введите искомое число: "))
for i in range(len(list1)):
    if search_numbers==list1[i]:
        count+=1
print(f"Искомое числов встрачается {count} раз")
