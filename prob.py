# a = int(input('Введите целоечисло:'))
# b = int(input('Введите целоечисло:'))
# d = input('Введите строку:')
# c = float(input('Введите целоечисло:'))
# print(d, a+b+c)

# import math
# CB = float(input('Введите длинну первого катета:'))
# AC = float(input('Введите длинну второго катета:'))
#
# S = (CB*AC)/2
# AB = math.sqrt(AC**2+CB**2)
# P = AC + CB + AB
# print(S)
# print(P)

# a=5
# a=str(a)
# print(a+a)
import random

# a = random.randint(100, 999)
# print(a)
# b = a%10
#
# c = a//100
#
# d =(a%100)//10
#
# print(b+c+d)
# b=[1,2,3,4,5]
# a = random.choice(b)
# print(a,)
# a = input('\t\tВведите целое число:')
# a = int(a)
# if a%2 == 0:
#     print(f'Число {a} четное')
# else:
#     print(f'Число {a} не четное')
# a = input('\t\tВведите целое число:')
# b = input('\t\tВведите целое число:')
# c = input('\t\tВведите целое число:')
#
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# a = float(input('\t\tВведите целое число:'))
# b = input('\t\tВведите операцию:')
# c = float(input('\t\tВведите целое число:'))
#
# if b == "+":
#     print(a+c)
# elif b == '-':
#     print(a-c)
# elif b == '*':
#     print(a*c)
# else:
#     print(a/c)


# x = float(input('\t\tВведите целое число:'))
# if x > 0:
#     y = 2*x - 10
# elif x == 0:
#     y = 0
# elif x<0:
#     y =2*abs(x) - 1
# print(y)

# a = float(input('\t\tВведите целое число:'))
# b = float(input('\t\tВведите целое число:'))
#
# c = a < b
# if c:
#     print(a, 'меньше',b)
# else:
#     print(a, 'больше', b)

# a = int(input('Введите год:'))
# if a%100 == 0 and a%400 ==0:
#     print(f'{a} Год является високосным')
# elif a%4 == 0 and a%100 != 0 and a%400 !=0:
#     print(f'{a} Год является високосным')
# else:
#     print(f'{a} Год не является високосным')

# a = float(input('Введите сторону:'))
# b = float(input('Введите сторону:'))
# c = float(input('Введите сторону:'))
#
# if a+b > c and b + c > a and a +c >b:
#     print('Треугольник существует')
# else:
#     print('Треугольник не существует')

a = 'Privet privet privet'
#
# b = a[::-1]
# print(b.upper())
# c = a.upper()
# print(c)
# print(c.lower())
# print(c.capitalize())
# d = a.title()
# print(a.title())
# print(d.isupper())
# print(a.swapcase())
# print(a.split(' '))
# b = a.split(' ')
# c = "   ".join(b)
# print(c)
# c='111111'
# print(c.isdigit())
#
# a = input('Введите строку:')
#
# b = a.split(' ')
# print(b)
# print(','.join(b))

# a = 'Привет, как дела? Меня зосут Сергей!'
# b = 11
# c = 18
# # b = a.split(' ')
# # print(' '.join(b))
# print(c, a, b, sep='@', end='!\n')
# print(a)
# for i in range(15,0,-1):
#     print(i)
#
# a = 'Я учу програмирование'
# b = 'о'
#
# for i in a:
#     if i == b:
#         del i
#     else:
#         print(i, end=' ')
#
# a = int(input('Начало'))
# b = int(input('Конец'))
# c = int(input('шаг'))

# for i in range(55,1984):
#     if i%5 == 0:
#         print(i,end= ' ')

# a = [1,2,3,4,5]
# # print(a.count(1))

for i in range(1,10):

    i -= 5
print(i)

i = 0
while i<10:
    i+=1
i-=10
print(i)

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

'a' + 'x' if '123'.isdigit() else 'y'+ 'b'

print('100$ 200$ 300$'.count('$',5))