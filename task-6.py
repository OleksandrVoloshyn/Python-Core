# Создать класс File:
# -он должен принимать  не меньше 2-х файлов
# -создать метод который будет проверять существуют ли эти файлы, если нет то создать их
# -создать метод который принимает текст  (записать текст в выбранный файл)
# -создать метод который выводит список файлов, и при выборе, выводит содержимое в консоль
# -создать метод который даёт возможность выбрать два файла и меняет их содержимое местами

# class File:
#     def __init__(self, one, two):
#         self.one = one
#         self.two = two
#
#     def check_files(self):
#         for i in self.one, self.two:
#             try:
#                 with open(i):
#                     print('good')
#             except FileNotFoundError:
#                 with open(i, 'w'):
#                     print('created new file')
#     @staticmethod
#     def write_text(txt, choose_file):
#         with open(choose_file, 'a') as file:
#             file.write(txt + '\n')
#
#     def read_file(self):
#         while True:
#             print(f'1) {self.one}')
#             print(f'2) {self.two}')
#             print(f'3) Назад')
#             choose = input('Виберіть номер файла: ')
#
#             if choose == '1':
#                 with open(self.one) as file:
#                     print(file.read())
#             elif choose == '2':
#                 with open(self.two) as file:
#                     print(file.read())
#             elif choose == '3':
#                 break
#             else:
#                 print('Виберіть з вище наведених')
#     @staticmethod
#     def change(one, two):
#         first = open(one)
#         second = open(two)
#         x = first.read()
#         y = second.read()
#         with open(one, 'w') as file:
#             file.write(y)
#         with open(two, 'w') as file:
#             file.write(x)
#         first.close()
#         second.close()


# class_object = File('xxx', 'yyy')
# class_object.check_files()
# class_object.write_text('text_x', 'xxx')
# class_object.write_text('text_y', 'yyy')
# class_object.change('xxx', 'yyy')
# class_object.read_file()
######################################################################################################################
