# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

# def my_func(string_val):
#     for index in string_val:
#         if not index.replace("-", "").isdigit():
#             return []
#     return string_val

# def min_sum(val):
#     art = my_func(val)
#     if art:
#         return min(art, key=int), max(art, key=int)
#     else:
#         return []

# print(min_sum(input().split()))

# Tot jlyj--------------------------

# def check(str_list):
#     for i, num in enumerate(str_list):
#         str_list[i] = num.strip('.,;:?!')
#         if not str_list[i].replace("-", "").isdigit():
#             return []
#     return str_list


# def find_max_min(nums_str: str):
#     list_nums = nums_str.split()
#     right_list = check(list_nums)

#     if right_list:
#         return min(right_list, key=int), max(right_list, key=int)
#     else:
#         print("The data is incorrect")
#         return []
# # print(*find_max_min(input("Enter the numbers separated by a space: ")))


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

# from math import sqrt

# def roots_equ(a, b, c):
#     d = b ** 2 - 4 * a * c
#     with open("roots.txt", "a", encoding="utf-8") as my_f:
#         my_f.write(f"{a}x ** 2 + {b}x + {c}\n")
#         if d > 0 and a:
#             my_f.write(f"The first root: {(-b + sqrt(d)) / (2 * a):.2f}\n")
#             my_f.write(f"The first root: {(-b - sqrt(d)) / (2 * a):.2f}\n")
#         elif d == 0 and a:
#             my_f.write(f"The root: {-b / (2 * a):.2f}\n")
#         else:
#             my_f.write("There are no roots.\n")

# # 1 2 -3, 5 6 -7, 8 9 -10
# for i in range(3):
#     roots_equ(int(input("Enter the coefficient 'a': ")), int(input("Enter the coefficient 'b': ")),
#               int(input("Enter the coefficient 'c': ")))


# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.
# from math import gcd


# print("Введите два числа: ")
# a = int(input("a = "))
# b = int(input("b = "))

# def nok (first, second):
#     return(first*second) // gcd(first, second)
# print(nok(a,b))
