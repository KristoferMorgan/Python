# 1. В файле находится N натуральных чисел, записанных через пробел. 
#Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

import os

path = os.path.join(r'Task_files','task001.txt')
with open(path,'r') as data:
    my_list = data.readline()

def f(my_list:list):
    for i in range(1 , len(my_list)):
        if my_list[i] - my_list[i - 1] != 1:
            return my_list[i - 1] + 1
    return 'Not found'
x = tuple(filter(lambda  i: (my_list[i-1]))) != 1
print(x[0] + 1)

# my_list = [1, 2, 4, 5, 6]

# f = lambda i: (my_list[i] - my_list[i - 1]) != 1
# x = tuple(filter(f, range(1, len(my_list))))
# print(x[0] + 1)
