# 1)написати прогу яка вибирає з введеної строки цифри і виводить їх через кому,
# st = 'as 23 fd1fdg544'
# result = ''
#
# for i in st:
#     if i.isdecimal():
#         result += i
# result = ', '.join(result)
# print(result)
#####################################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# st = 'as 23 fd24fdg544 34  34!!1!'
# result = ''
#
# for i in st:
#     if i.isdigit():
#         result += i
#     else:
#         result += " "
# result = ', '.join(result.split())
# print(result)
#####################################################################################################
# 3)прога, що виводить кількість кожного символа з введеної строки,
# st = 'as 23 fdfdg544'
#
# for i in st:
#     count = st.count(i)
#     if count:
#         print(f"'{i}' -> {count}")
#         st = st.replace(i, '')
#####################################################################################################
# дз 2 часть(list comprehension):
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# upper_greeting = [i.upper() for i in greeting]
# print(upper_greeting)
#####################################################################################################
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# цей приклад більш відповідає умові
# my_list = [i ** 2 for i in range(0, 50) if i % 2 != 0]

# цей спосіб вертає те саме що й в прикладі
# my_list = [i ** 2 for i in range(0, 50)]
# print(my_list)
#####################################################################################################
# 3)  есть лист:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
# пример:
# ['LT', 'LT', 'LT', 'LT', 'GT', 'GT', 'GT', 'GT']
#
# result = ['GT' if x > 4 else 'LT' for x in numbers]
# print(result)
#####################################################################################################
# 4) есть два листа:
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
# записать в лист тюплы (x,y) если x+y == 0
# result = [(x, y) for x in list1 for y in list2 if not x + y]
# print(result)
#####################################################################################################
# Нужно проверить, все ли числа в листе уникальны.
# лист нужно сделать со строки полученной с помощью input()
# my_list = input('Enter :')
#
# for i in my_list:
#     if i.isdigit():
#         res = my_list.count(i)
#         if res > 1:
#             print(f"{','.join(my_list)} -> False")
#             break
# else:
#     print(f"{','.join(my_list)} -> True")
#####################################################################################################
# ввести строчку с input() и вывести самое длинное и повторяющееся слово
# пример:
# "python the best of the best programming language because is python"
# Вывод: python
# my_string = 'python the best language of the best programming language because is python'
# # my_string = input('XXX :')
# split_string = my_string.split()
# count_number = 1
# first_check = []
# 
# for i in split_string:
#     if split_string.count(i) >= count_number and i not in first_check:
#         first_check.append(i)
#         count_number = split_string.count(i)
#
# count_len = 0
# result = []
#
# for j in first_check:
#     if len(j) > count_len:
#         result.clear()
#         result.append(j)
#         count_len = len(j)
# print(result)
