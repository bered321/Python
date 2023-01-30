import os # ДОБАВЛЕНО ТОЛЬКО ДЛЯ ЛИЧНОГО УДОБСТВА И ЛУЧШЕЙ ЧИТАЕМОСТИ!!!!!

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Ведите трёхзначное число: '))
firstNum = number // 100  
thirdNum = number % 10   
secondNum = (number % 100) // 10  
sum = firstNum + secondNum + thirdNum
print(f'Cумма цифр числа {number} равна: {sum}')

