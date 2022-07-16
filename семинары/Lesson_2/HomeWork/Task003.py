#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму. 
# *Пример:
# *- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}





def create_list(number: int) -> list:
    new_list = []
    for n in range(1, number+1):
        new_list.append((1+1/n)**n)
    return new_list
def sum_elements(list:list) -> float:
    summ =0
    for i in list:
        summ += i
    return summ
number = int(input("enter number:"))
my_list = create_list(number)
summ = sum_elements(my_list)
print(f"это ваш список:{my_list}")
print(f"сумма элементов масива равна: {summ}")