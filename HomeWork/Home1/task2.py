# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
number = int(input('Ведите трёхзначное число: \n'))
while number < 100 or number > 999:
    print('Вы ошиблись!\n')
    number = int(input('Ведите трёхзначное число: \n'))
firstNum = number // 100  # первое число
thirdNum = number % 10   # третье число
secondNum = (number % 100) // 10  # второе число
sum = firstNum + secondNum + thirdNum
print(f'Cумма цифр числа {number} равна: {sum}')

