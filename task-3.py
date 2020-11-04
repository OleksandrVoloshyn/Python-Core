# - створити функцію яка виводить ліст
# l = [1, 2, 3, 4, 5]
#
#
# def list_func(l):
#     for i in l:
#         print(f'[{l.index(i)}] -> {i}')
#
#
# list_func(l)
#####################################################################################################
# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def get_min(num1, num2, num3):
#     res = min(num1, num2, num3)
#     print(res)
#     return res
#
#
# get_min(7, 2, 4)
#####################################################################################################
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def get_max(num1, num2, num3):
#     res = max(num1, num2, num3)
#     print(res)
#     return res
#
#
# get_max(8, 1, 0)
#####################################################################################################
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def get_min(*args):
#     res = min(args)
#     print(max(args))
#     return res
#
#
# print(get_min(7, 14, 0, 3, -5))
#####################################################################################################
# - створити функцію яка повертає найменьше число з ліста
# my_list = [1, 2, 3, 4, 5, 6, 7]
#
#
# def get_min(l):
#     return min(l)
#
#
# print(get_min(my_list))
#####################################################################################################
# - створити функцію яка повертає найбільше число з ліста
# my_list = [1, 2, 3, 14, 5, 6, 7, 8, 9]
#
#
# def get_max(*args):
#     return max(args)
#
#
# print(get_max(*my_list))
#####################################################################################################
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# number_list = [1, 2, 3, 4, 5, 6, 7]
#
#
# def get_sum(*args):
#     return sum(args)
#
#
# print(get_sum(*number_list))
#####################################################################################################
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# number_list = [1, 2, 3, 4, 5]
#
#
# def get_avg(*args):
#     return sum(args) // len(args)
#
#
# print(get_avg(*number_list))
#####################################################################################################
# Приклад
# l1 = [1, 2, 3, 4]
# l2 = [2, 3, 4, 5]
# результат
# [3, 5, 7, 9]

# first_list = [1, 2, 3, 4]
# second_list = [2, 3, 4, 5]
#
#
# def lists_sum(a, b):
#     xxx = dict(zip(a, b))
#     res = []
#
#     for k, v in xxx.items():
#         res.append(k + v)
#     print(res)
#
#
# lists_sum(first_list, second_list)
#####################################################################################################
# написати декоратор який замінює нижні підчеркування на пробіли і повертає це значення

# def decorator(func):
#     def wrapper():
#         res = func().replace('_', ' ')
#         return res
#
#     return wrapper
#
#
# @decorator
# def hello():
#     return 'Hello_boss_!!!'
#
#
# print(hello())
#####################################################################################################
# def create_generator():
#     my_list = range(1000)
#     print('Start')
#     for i in my_list:
#         print('Before')
#         yield i
#         print('After')
#
#
# my_generator = create_generator()
# print(next(my_generator))
# print(next(my_generator))
#####################################################################################################
# Імітуємо роботу банкомату
# Є рахунок та дії над ним
# 1. Етап логінації - ввести логін + пароль
# 2 Меню :  (кожен пункт меню це функція)
# 1) Подивитись стан рахунку : виводить стан рахунку
# 2) Зняти кошти (ввести кількість коштів, + дивитись над тим щоб не залазити в борг)
# 3) покласти кошти (ви вводите скільки коштів потрібно покласти)
# 0) вихід

# account = [
#     {'login': 'login1', 'password': 'password1', 'value': 10000},
#     {'login': 'login2', 'password': 'password2', 'value': 500},
#     {'login': 'login3', 'password': 'password3', 'value': 2000},
#     {'login': 'login4', 'password': 'password4', 'value': 700},
# ]

# # Етап логінації
#
# login = input('login: ')
# login = 'login1'
# password = input('password: ')
# password = 'password1'
# choose_account = 0
# enter = False
#
# for i in range(len(account)):
#     if account[i]['login'] == login and account[i]['password'] == password:
#         enter = True
#         choose_account = i
#
# if not enter:
#     print('Неправильний логін чи пароль')
#

# Кінець етапу логінації
#
# def check():
#     check_value = account[choose_account]['value']
#     print(f'На вашому рахунку {check_value} гривень')
#
#
# def pull():
#     number = int(input('Яку суму ви бажаєте отримати : '))
#     if account[choose_account]['value'] < number:
#         print('---------------------')
#         print('Недостатньо коштів')
#         print('---------------------')
#     else:
#         account[choose_account]['value'] -= number
#         print('Отримайте ваші кошти')
#
#
# def plus():
#     give = int(input('Скільки бажаєте внести :'))
#     account[choose_account]['value'] += give
#     print('Операція проведена успішно')
#
#
# while enter:
#     print('1) Подивитись стан рахунку')
#     print('2) Зняти кошти')
#     print('3) Покласти кошти')
#     print('4) Вихід')
#
#     choice = input('Зробіть свій вибір: ')
#
#     if choice == '1':
#         check()
#
#     elif choice == '2':
#         pull()
#
#     elif choice == '3':
#         plus()
#
#     elif choice == '0':
#         break
#     else:
#         print('Виберіть з переліку')
