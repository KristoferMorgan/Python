# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# 
# Пример:
# 
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 
def sum_of_odd_elements(my_list:list) -> int:
    summ = 0
    for i in my_list:
        if i % 2 == 0:
            continue
        else:
            summ += i
    return summ



your_list = [int(i) for i in input("enter the list items separated by a space:").split()]
print(f"it't your list: {your_list}")
print(f"sum of odd elements = {sum_of_odd_elements(your_list)}")