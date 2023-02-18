import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                       Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам      Парам пам-пам

# text = input("Введи текст кричалки: ").lower().split()
# letters = list('аоуыэеёиюя')
# rifma = lambda x: sum (1 for i in x if i in letters)
# first_phrase = rifma(text[0])
# if all([rifma(i) == first_phrase for i in text]):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


def count(a, b):
    my_list = list()
    for phraze in song:
        summa = 0
        for symbol in phraze:
            if symbol in vowels:
                summa += 1
        my_list.append(summa)
    return my_list


vowels = list('аоуыэеёиюя')
song = input('введите текст песни винипуха: ').lower().split()

my_list_2 = count(song, vowels)
if my_list_2.count(my_list_2[0]) == len(my_list_2):
    print('Парам пам-пам')
else:
    print('Пам парам')

# if len(set(my_list_2)) == 1:
#      print('Парам пам-пам')
# else:
#      print('Пам парам')


