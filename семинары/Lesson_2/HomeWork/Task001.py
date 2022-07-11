# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
 #   *Пример:*
 #   - 6782 -> 23
 #  - 0,56 -> 11


def Sum_simbol_number(number:str,sum: int):
   for i in number:
    if i in ",.":
        continue
    sum += int(i)
   return sum


sum = 0
number = str(input("enter number:"))
print(Sum_simbol_number(number,sum))
