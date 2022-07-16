# Реализуйте алгоритм перемешивания списка
import random

def shuffle(my_list:list):
    my_list = list(my_list)
    random.shuffle(my_list)
    return my_list

your_list = [i for i in input("enter element list:").split()]
new_list = shuffle(your_list)
print (f"it's your list: {your_list}")
print (f"after mixing the elements, we get: {new_list}")