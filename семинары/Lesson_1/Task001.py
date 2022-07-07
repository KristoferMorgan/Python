# Написать программу,которая принимает на вход два числа и проверяет,является ли одно число квадратом другого.
a=int(input('enter a:'))
b=int(input('enter b:'))

if ( b / a == a):
    print('the number {b} is not the square of the number {a}')
else:
    print('the number {b} is the square of the number {a}')

