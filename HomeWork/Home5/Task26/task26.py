import os  # ДОБАВЛЕНО ТОЛЬКО ДЛЯ ЛИЧНОГО УДОБСТВА И ЛУЧШЕЙ ЧИТАЕМОСТИ ПРИ ВЫВОДЕ В ТЕРМИНАЛ!!!!!


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(a, b):
    if b == 1:
        return a
    else:
        return a*power(a, b-1)


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(f"Число {a} в степени {b} равно: {power(a, b)}")