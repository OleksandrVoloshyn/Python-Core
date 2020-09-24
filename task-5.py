# Створити клас rectangle
# 1) об'єкт приймає два параметри - дві сторони х у
# 2) описати методи арифметичні
#   + сума площин двок об'єктів
#   - різниця площин
# 3) логічні оператори:
#   == повертає true якщо рівні по площині
#   != якщо не рівні
#   >, < відповідно
# 4) len() - сума сторін
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return self.x + self.y + other.x + other.y
#
#     def __sub__(self, other):
#         return (self.x + self.y) - (other.x + other.y)
#
#     def __eg__(self, other):
#         if self.x + self.y == other.x + other.y:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if self.x + self.y != other.x + other.y:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if self.x + self.y > other.x + other.y:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.x + self.y < other.x + other.y:
#             return True
#         else:
#             return False
#
#     def __len__(self):
#         return self.x + self.y
#
#
# xxx = Rectangle(5, 4)
# yyy = Rectangle(3, 5)
# print(xxx + yyy)
# print(xxx - yyy)
# print(xxx == yyy)
# print(xxx != yyy)
# print(xxx > yyy)
# print(xxx < yyy)
# print(len(xxx))
# ######################################################################
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
# my_list = list()
#
#
# class Letter:
#     __count = 0
#
#     def __init__(self):
#         self.__text = ''
#         Letter.__count += 1
#
#     @property
#     def my_text(self):
#         return self.__text
#
#     @my_text.setter
#     def my_text(self, new_text):
#         self.__text = new_text
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#     def change_my_list(self, your_list):
#         your_list.append(self.__text)
#
#
# xxx = Letter()
# xxx.my_text = 'Hello World !!!'
# print(xxx.my_text)
#
# yyy = Letter()
# print(Letter.get_count())
#
# xxx.change_my_list(my_list)
# print(my_list)
############################################################################################
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)
#
# class Travel:
#     __count = 0
#     __register = {}
#
#     def __init__(self, time, price=0):
#         self.time = time
#         self.price = price
#         self.name = self.__class__.__name__
#         Travel.__count += 1
#         Travel.__register[Travel.__count] = {self.__class__.__name__: self.__dict__}
#
#     @classmethod
#     def get_register(cls):
#         return cls.__register
#
#     def get_time(self, other):
#         if self.time < other.time:
#             result = other.time - self.time
#             return f'{self.name} на {result} хвилин швидший за {other.name}'
#         else:
#             result = self.time - other.time
#             return f'{other.name} на {result} хвилин швидший за {self.name}'
#
#
# class Plane(Travel):
#
#     def __init__(self, price, time, reg, comfort_class):
#         super().__init__(time, price)
#         self.reg = reg
#         self.comfort_class = comfort_class
#
#     def full_time(self):
#         return self.time + self.reg
#
#
# class Train(Travel):
#     def __init__(self, price, time, place):
#         super().__init__(time, price)
#         self.place = place
#
#     def info(self):
#         print(self.__dict__)
#
#
# class Car(Travel):
#     def __init__(self, person, time, fuel, distance):
#         super().__init__(time)
#         self.person = person
#         self.fuel = fuel
#         self.distance = distance
#
#     @property
#     def get_value(self):
#         value = self.fuel // self.person
#         return f'З особи по {value} гривасів'
#
#
# xxx = Plane(200, 60, 15, 1)
# yyy = Train(120, 300, 1.2)
# zzz = Car(3, 120, 450, 8000)
# print(Travel.get_register())
