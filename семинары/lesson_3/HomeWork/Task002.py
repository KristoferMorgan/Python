# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# 
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def product_of_pairs_of_numbers(my_list:list) -> list:
    product = 1
    list_product = []
    index = 0
    while(index < len(my_list) // 2):
        product = my_list[index] * my_list[-index - 1]
        list_product.append(product)
        index += 1
    return list_product








your_list = [int(i) for i in input("enter the list items separated by a space: ").split()]
print(f"it's your list: {your_list}")
print("we output the sum of pairs of numbers from the first to the last:")
print(product_of_pairs_of_numbers(your_list))
