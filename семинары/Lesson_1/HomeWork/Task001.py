# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
Number = int(input("enter namber week:" ))

if Number <= 5 :
    print("It's a working day")
elif 6 <= Number <= 7:
    print("It's a weekend")
else:
    print("The number is not correct.There are only 7 days in a week")