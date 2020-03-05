#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# a='00000000'
# for i in range(1,6):
#     print(i,a,sep=' ')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
#
# count=0
# for i in range(10):
#     if input('Введите число ')=='5':
#         count+=1
# print('Число 5 введено', count, 'раз(а)', sep=' ')


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# prois = 1
# for i in range(1,11):
#     prois*=i
# print(prois)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# sum = 0
# integer_number = int(input('Введите число '))
# while integer_number>0:
#     sum+=integer_number%10
#     integer_number = integer_number//10
# print(sum)
'''
Задача 7
Найти произведение цифр числа.
'''
# prois = 1
# integer_number = int(input('Введите число '))
# while integer_number>0:
#     prois*=integer_number%10
#     integer_number = integer_number//10
# print(prois)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = int(input('Введите число '))
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# max_number = 0
# integer_number = int(input('Введите число '))
# while integer_number>0:
#
#     if max_number <integer_number%10:
#         max_number=integer_number%10
#     integer_number = integer_number//10
# print('Самое большое число - ', max_number)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# count=0
# integer_number = int(input('Введите число '))
# while integer_number>0:
#     if integer_number%10 == 5:
#         count+=1
#
#     integer_number = integer_number//10
# print(count)