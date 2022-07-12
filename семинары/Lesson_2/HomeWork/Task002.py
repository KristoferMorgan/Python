#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3
def fill_array(number:int,list_fact:int):
    fact = 1
    for index in range(1, int(number) + 1):
        fact *= index
        list_fact.append(fact) 
    return list_fact

list_fact = []
number = int(input("enter number:"))
print(f"output a lits from 1 to {number} ")
print(fill_array(number,list_fact))