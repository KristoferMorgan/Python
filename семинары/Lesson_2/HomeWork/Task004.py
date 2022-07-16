# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.
import random


def list_minus_n_to_n(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(random.randint(-number, number+1))

    return list
def product_of_coordinates(coordinates_list:str,work_list:int) -> int:
    split_coordinate = coordinate.split()
    a = int(split_coordinate[0])
    b = int(split_coordinate[1])
    summ = 1
    for i in work_list[a - 1:b ]:
        summ *= i
    return summ
number_N = int(input(f"enter number N:"))
my_list = list_minus_n_to_n(number_N)
print(f"it's your list:{my_list}")
coordinate = input(f"enter position:")
print(f"the product of your coordinates in the list = {product_of_coordinates(coordinate,my_list)}")