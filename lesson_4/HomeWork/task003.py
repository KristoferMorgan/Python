# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list_number = [21 ,22,231,313,22,3123,22,33,12,33,313,1,23214,231]
unique_numbers = list(set(list_number))
print(unique_numbers)



#------------------------------or---------------------------------

list_number = [21 ,22,231,313,22,3123,22,33,12,33,313,1,23214,231]
def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
unique_numbers = get_unique_numbers(list_number)
print(unique_numbers)
