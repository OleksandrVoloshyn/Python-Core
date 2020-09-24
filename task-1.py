# -------------3) переделать первое задание под меню с помощью цикла--------------
# my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# while True:
#     print('1. найти min число в листе')
#     print('2. удалить все одинаковые значения')
#     print('3. заменить каждое четвертое значение на "Х"')
#     print('4. вывести элемент листа, значение которого ближе всего к среднему арифметическому')
#     print('5 Вихід')
#     choice = input('Зробіть свій вибір: ')
#
#     if choice == '1':
#         my_list.sort()
#         print('minNum', my_list[0])
#
#     elif choice == '2':
#         for num in my_list:
#             if my_list.count(num) > 1:
#                 my_list.remove(num)
#
#         for num in my_list:
#             if my_list.count(num) > 1:
#                 my_list.remove(num)
#         print(my_list)
#
#     elif choice == '3':
#         l = my_list.copy()
#         for i in range(3, len(l), 4):
#             l[i] = 'X'
#         print(l)
#
#     elif choice == '4':
#         num = (sum(my_list) / len(my_list))
#         my_list.append(num)
#         my_list.sort()
#         index = my_list.index(num)
#         small = my_list[index - 1]
#         big = my_list[index + 1]
#         right = big - num
#         left = num - small
#
#         if right > left:
#             print(small)
#         else:
#             print(big)
#
#     elif choice == '5':
#         break
#
#     else:
#         print('Такої цифри немає в переліку')
#####################################################################################################
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# side = 10
# i = side
# while i >= 1:
#     if i == side or i == 1:
#         j = side
#         while j > 0:
#             print('*', end='')
#             j -= 1
#         print()
#     else:
#         j = side - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1
####################################################################################################
# 4) вывести табличку умножения с помощью цикла while
# i = 1
# size = 10
# while i <= size:
#     j = 1
#     while j <= size:
#         res = i * j
#         if res // 10:
#             print(res, end='  ')
#         else:
#             print(res, end='   ')
#         j += 1
#     print()
#     i += 1
#####################################################################################################
# написати програму, яка підраховує вартість витрачених коштів.
#  1)Ви записуєте: дату, товар і ціну,
#  2)ці записи можна редагувати,
#  3)таких записів у вас може бути безліч
#  4)у вас має бути меню:
#    - список всіх записів
#    - загальна вартість всіх покупок
#    - найдорожча покупка
#    - пошук по назві товару
#    - покупки по днях

# costs = [{'data': '12.03', 'name': 'apple', 'price': 100},
#          {'data': '01.04', 'name': 'lemon', 'price': 50}]
#
# while True:
#     print('1. Добавити покупку')
#     print('2. Список всіх витрат')
#     print('3. Загальна вартість всіх покупок')
#     print('4. Найдорожча покупка ')
#     print('5. Пошук по назві товару')
#     print('6. Покупка по днях')
#     print('7. Вихід')
#
#     choice = input('Зробіть свій вибір: ')
#
#     if choice == '1':
#         data = input('Дата покупки (XX.XX) :')
#         name = input('Назва товару:')
#         price = int(input('Ціна :'))
#
#         costs.append({'data': data, 'name': name, 'price': price})
#
#     elif choice == '2':
#         print(costs)
#
#     elif choice == '3':
#         spending = 0
#
#         for cost in costs:
#             spending += cost.get('price')
#         print(spending)
#
#     elif choice == '4':
#         maxPrice = {'data': '01.01', 'name': 'test', 'price': 0}
#
#         for cost in costs:
#             if cost['price'] > maxPrice['price']:
#                 maxPrice.update(cost)
#         print(maxPrice)
#
#     elif choice == '5':
#         findName = input('Введіть назву товару:')
#
#         for cost in costs:
#             if cost['name'] == findName:
#                 print(cost)
#
#     elif choice == '6':
#         findData = input('Введіть дату (XX.XX) :')
#
#         for cost in costs:
#             if cost['data'] == findData:
#                 print(cost)
#
#     elif choice == '7':
#         break
#
#     else:
#         print('Введіть число зі списку !')
