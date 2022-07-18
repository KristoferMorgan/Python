# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
#  Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def result(my_list:list)->float:
    new_list = []
    for i in my_list:
        new_list.append(i - int(i))
    return new_list
def min_max(my_list:float):
    max_number = my_list[0]
    min_number = my_list[0]
    for i in my_list:
        if i > max_number:
            max_number = i
        elif min_number > i:
            min_number = i                                                      
    result_min_max = max_number - min_number
    return result_min_max

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f"it's your list: {my_list}")
new_list = result(my_list)
print(f"{new_list}")
result_min_max = min_max(new_list)
print(f"the difference between the minimum and maximum value of a fractional number is {result_min_max}")