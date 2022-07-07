# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N 
#  *Примеры:*  
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
number = int(input('Enter number: '))
number_1 = -number
while number_1 < number:
    print (number_1)
    number_1 += 1
2