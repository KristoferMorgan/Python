#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму. 
# *Пример:
# *- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}





def create_list(number: int):
    new_list = []
    for element in range(1, number+1):
        new_list.append((1+1/element)**element)
    return new_list

number = int(input("enter number:"))
print(create_list(number))