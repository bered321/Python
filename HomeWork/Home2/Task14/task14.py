import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число: "))
print(f"Все степени 2 не превосходящие число {n}:")
for i in range(n):
    if 2**i <= n:
        print(2**i)
