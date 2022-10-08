# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

# import decimal

# num = float(input("Введи число: "))
# num1 = decimal.Decimal(num)
# accuracy = int(input("Сколько знаков после запятой надо?: "))
# a = round(num1, accuracy)
# print(a)
# ________________________________________________________________________________________________________


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

# def divisible(num):
#     array = list()
#     divider = 2
#     while(divider <= num):
#         if (num % divider) == 0:
#             array.append(divider)
#             num = num/divider
#         else:
#             divider +=1
#     print(array)

# divisible(int(input("Введите число: ")))
# ___________________________________________________________________________________________________________


# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# from random import randint

# array = [randint(1, 10) for i in range(int(input("Введите число: ")))]
# print(array)
# a = []
# for i in array:
#     if array.count(i) == 1:
#         a.append(i)
# print(a)
#_______________________________________________________________________________________________________    

# # 4.* Задана натуральная степень k. 
# # Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# # записать в файл полученный многочлен не менее 3-х раз.
# # in
# # 9
# # 5
# # 3

# # out in the file
# # 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# # 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# # 4*x^2 - 4 = 0

# # in
# # 0
# # -1
# # 4

# # out in the file
# # 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# # 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# # 4*x^2 - 4 = 0
# # 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)

# Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios(k) 
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('33_Polynomial2.txt', 'w') as data:
#     data.write(polynom2)



# # 5. ** Даны два файла, в каждом из которых находится запись многочленов. 
# # Задача - сформировать файл, содержащий сумму многочленов.
# # in
# # "poly.txt"
# # "poly_2.txt"

# # out in the file
# # 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# # 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# # 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# # in
# # "poly.txt"
# # "poly_2.txt"

# # out
# # The contents of the files do not match!

# from random import choice


# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()

#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")


# # poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")
