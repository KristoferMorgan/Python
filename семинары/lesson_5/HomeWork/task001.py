# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

word = 'абв фгбв абв Ура,питон круто,очень интересные семинары!абв'

my_str = word.replace("абв","")
print(my_str)


----------------------------------or--------------------------------------


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