# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Function to print binary number for the
# input decimal using recursion
def decimal_to_binary(my_number:int):

	if(my_number > 1):
		decimal_to_binary(my_number//2)

	
	print(my_number%2, end=' ')


your_number = int(input("enter a decimal number to convert it to binary:"))

decimal_to_binary(your_number)

