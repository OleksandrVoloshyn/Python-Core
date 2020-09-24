# 1)-написать lambda функцию, которая находит среднее арифметическое
# значение входных аргументов, этих входных аргументов может быть сколько угодно
# average = lambda *args: sum(args) // len(args)
# print(average(5, 5, 7, 7))
##########################################################################################
# 2)-написать lambda функцию которая принимает строку и возвращает лист слов,
# при этом каждое слово это лист его букв:
# к примеру:
#  "Hello from owu"=> [['H', 'e', 'l', 'l', 'o'], ['f', 'r', 'o', 'm'], ['o', 'w', 'u']]
# print((lambda st: [list(w) for w in st.split()])('Hello from owu'))
# print(list(map(lambda st: list(st), 'Hello from owu'.split())))
##########################################################################################
# 3)создать два класса Owner и Pet:
# у владельца должны быть такие методы:
# -добавить питомца
# -удалить питомца
# -показать всех питомцев
# -показать питомцев по типу

# 4) создать реестр владельцев и питомцев + создать меню:
# -добавить владельца
# -удалить владельца
# -показать всех владельцев
# -показать всех владельцев и их питомцев
# -выбрать владельца:
#       -добавить питомца
#       -удалить питомца
#       -показать всех питомцев
#       -показать питомцев по типу
# class Owner:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.pets = []
#
#     def __str__(self):
#         return f'{self.name} {self.age} {self.city} {self.pets}'
#         # return str(self.__dict__)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#     def add_pet(self, pet_name, pet_age, animal_type):
#         self.pets.append(Pet(pet_name, pet_age, animal_type))
#
#     def remove_pet(self, pet_name):
#         for i in self.pets:
#             if i.pet_name == pet_name:
#                 self.pets.remove(i)
#
#     def show_all_pets(self):
#         print(self.pets)
#
#     def show_type_pets(self):
#         for i in self.pets:
#             print(f'{i.pet_name}-->{i.animal_type}')
#
#
# class Pet:
#     def __init__(self, pet_name, pet_age, animal_type):
#         self.pet_name = pet_name
#         self.pet_age = pet_age
#         self.animal_type = animal_type
#
#     def __str__(self):
#         return f'{self.pet_name} {self.pet_age} {self.animal_type}'
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#
# register = []
# while True:
#     print('1) Добавить владельца')
#     print('2) Удалить владельца')
#     print('3) Показать всех владельцев')
#     print('4) Показать всех владельцев и их питомцев')
#     print('5) Вибрать владельца')
#     print('0) Вихід')
#     choose = input('Зробіть свій вибір: ')
#
#     if choose == '1':
#         name = input('Введіть імя: ')
#         age = input('Введіть вік: ')
#         city = input('Введіть місто: ')
#         register.append(Owner(name, age, city))
#
#     elif choose == '2':
#         remove_name = input('Введіть імя:')
#         for owner in register:
#             if owner.name == remove_name:
#                 register.remove(owner)
#
#     elif choose == '3':
#         for owner in register:
#             only_owners = [owner.name, owner.age, owner.city]
#             print(only_owners)
#
#     elif choose == '4':
#         print(register)
#
#     elif choose == '5':
#         choose_owner = input('Введіть ім\'я: ')
#         print(choose_owner)
#         # Перевірка на наявність в реєстрі
#         for owner in register:
#             if choose_owner in owner.name:
#                 # Запускаю нову менюшку з вибраним власником
#                 while True:
#                     print('1) добавить питомца')
#                     print('2) удалить питомца')
#                     print('3) показать всех питомцев')
#                     print('4) показать питомцев по типу')
#                     print('0) Назад')
#
#                     change_owner = input('Зроби свій вибір: ')
#
#                     if change_owner == '1':
#                         pet_name = input('Назва тваринки: ')
#                         pet_age = input('Вік: ')
#                         pet_type = input('Тип: ')
#                         owner.add_pet(pet_name, pet_age, pet_type)
#
#                     elif change_owner == '2':
#                         remove_name = input('Введіть назву: ')
#                         owner.remove_pet(remove_name)
#
#                     elif change_owner == '3':
#                         owner.show_all_pets()
#
#                     elif change_owner == '4':
#                         owner.show_type_pets()
#
#                     elif change_owner == '0':
#                         break
#                     else:
#                         print('Виберіть з переліку')
#
#     elif choose == '0':
#         break
#     else:
#         print('Виберіть з переліку')
##########################################################################################
# Создаем класс Fighter,
# cоздаем два бойца(экземпляр класса)
# делам формат поединка, каждый из бойцов поочередно наносит друг другу удары забирая случайное число жизни у своего соперника
# в конце выводится победитель
# P.S. Случайные числа в пайтоне можно получить импортировав библиотеку random:
# from random import random
#
#
# class Fighter:
#     def __init__(self, name, health=100, win=False):
#         self.name = name
#         self.health = health
#         self.win = win
#
#     def kick_enemy(self, enemy_name):
#         if self.health > 0 and not enemy_name.win and not self.win:
#             enemy_name.health -= round(random() * 100)
#             if enemy_name.health < 0:
#                 print(f'{self.name} win !!!')
#                 self.win = True
#
#
# one = Fighter('Sasha')
# two = Fighter('Kokos')
#
# # round 1
# one.kick_enemy(two)
# two.kick_enemy(one)
#
# # round 2
# one.kick_enemy(two)
# two.kick_enemy(one)
#
# # round 3
# one.kick_enemy(two)
# two.kick_enemy(one)
#
# # round 4
# one.kick_enemy(two)
# two.kick_enemy(one)
