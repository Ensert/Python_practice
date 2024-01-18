# def info(word):
#     print(word, end=' ')
#     print('for u')
#
#
# def summa(a, b):
#     res = a + b
#     info(res)
#     return res
#
#
# res1 = summa(5, 7)
# summa(5.6, 4.6)
# print(res1)

# def minimal(l):
#     min1 = l[0]
#     for i in l:
#         if i < min1:
#             min1 = i
#     print(min1)
#
#
# nums1 = [5, 4, 7, 4, -8, 45, 5]
# minimal(nums1)
# nums2 = [5, 4, 7, 4, 45, 5]
# minimal(nums2)
#
# Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення.
# def print_greeting(name):
#     print(f"Привіт, {name}!")
#
#
# user_name = input("Введіть ваше ім'я: ")
# print_greeting(user_name)

# Напишіть функцію, яка отримує рядок і ціле число n та повертає n копій заданого рядка.
#def code_loving_amount(text, times):
#    print(text * times)
#
#
#tex = input('enter text: ')
#time = int(input('how many times: '))
#code_loving_amount(tex, time)

# Напишіть функцію для обчислення суми двох цілих чисел.
#
# def suma(a, b):
#     res = a + b
#     print(res)
#
#
# i = int(input('enter 1st number: '))
# t = int(input('enter 2nd number: '))
# suma(i, t)

# Напишіть функцію для перетворення цілого числа в рядок.

# def num_to_string(d):
#     d = str(d)
#     print(f'string value of the entered number is: \'{d}\'')
#
#
# n = int(input('enter number: '))
# num_to_string(n)

# Напишіть функцію для отримання рядка з перших n символів іншого рядка. Якщо довжина рядка менше n, поверніть початковий рядок.
#
# def out(char, n):
#     if n >= len(char):
#         return char
#     else:
#         return char[:n]
#
#
# leght = input('enter string: ')
# a = int(input('enter number: '))
# res = out(leght, a)
# print(res)

# Напишіть функцію для визначення більшого з двох цілих чисел без використання вбудованої функції max().
# Якщо числа рівні, то вивести повідомлення equal.
#
# def sort(a, b):
#     eq = 'equal'
#     if a > b:
#         return a
#     elif a < b:
#         return b
#     elif a == b:
#         return eq
#
#
# var1 = int(input('Enter 1st value: '))
# var2 = int(input('enter 2nd value: '))
# result = sort(var1, var2)
# print(result)

# Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції max().
#
# def h_value(a):
#     return max(a)
#
#
# numbers = []
# i = 1
# while i <= 3:
#     n = int(input('enter number: '))
#     numbers.append(n)
#     i += 1
# res = h_value(numbers)
# print(res)

# Напишіть функцію, яка отримує два слова, об’єднує їх за допомогою пропуску і друкує результат об’єднання.

# def join(a, b):
#     print(f'{a} {b}')


# z = input('enter 1st word: ')
# x = input('enter 2nd word: ')
# join(z, x)

# Напишіть функцію, яка отримує 3 аргументи: перші 2 - числа, третій - операція (+, -, *, /), яка повинна бути проведена над ними.
# У випадку невідомої операції, функція повертає рядок Unknown operation. Результатом має бути дійсне число з двома знаками після десяткової крапки.
#
# def num_operate(a, b, c):
#     if c == '+':
#         res = a + b
#         print(res)
#     elif c == '-':
#         res = a - b
#         print(res)
#     elif c == '*':
#         res = a * b
#         print(res)
#     elif c == '/':
#         res = a / b
#         print(res)
#     else:
#         print(f'\'{c.capitalize()}\' is an unknown operation')
#
#
# var1 = int(input('enter 1st number: '))
# var2 = int(input('enter 2nd number: '))
# var3 = input('enter math operation: ')
# num_operate(var1, var2, var3)

# Напишіть функцію, яка перевіряє, чи подана послідовність порожня чи ні.

# def empty_check(a):
#     return not bool(a)


# tuple1 = (4.5, 4, 'char')
# list1 = [6, ',', 5]
# dict1 = {'key1': 'value1', 'key2': 'value2'}
# tuple2 = ()
# list2 = []
# dict2 = {}
# print(empty_check(tuple1))
# print(empty_check(tuple2))
# print(empty_check(list1))
# print(empty_check(list2))
# print(empty_check(dict1))
# print(empty_check(dict2))










