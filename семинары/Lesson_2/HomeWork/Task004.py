# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.
import random


def list_minus_n_to_n(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(random.randint(-number, number+1))

    return list





number_N = (f"enter number N:")
my_list = list_minus_n_to_n(number_N)