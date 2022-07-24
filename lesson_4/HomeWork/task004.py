# k.Задана натуральная степень
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os
def operation(k:int,my_list:list):
    if k == 0:
        print("степень не может быть в значении 0")
    else:
        while(k > 0 ):
            y = random.randint(1,100)
            my_list.append(f'({y} * x ^ {k})')
            k -= 1
    return my_list
def  convert_to_string(my_list:list):
    my_string = "+".join(my_list) + " = 0"
    return my_string
my_list = []
k = int(input("enter the natural degree k:"))
operation(k,my_list)
path = os.path.join("Task_file","task004.txt")
new_list = convert_to_string(my_list)
with open(path, 'w') as file:
    file.writelines(new_list)
