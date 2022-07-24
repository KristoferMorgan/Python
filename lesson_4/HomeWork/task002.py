# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

number = int(input("Integer: "))
multipliers = []
divider = 2
save_number = number
while divider * divider <= number:
        if number % divider == 0:
            multipliers.append(divider)
            number//=divider
        else:
            divider += 1
multipliers.append(number)
print(f"list of number multipliers {save_number} = {multipliers}")s