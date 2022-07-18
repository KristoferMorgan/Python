# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# 
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(number):
    if number>=0:
       index = range(number+1)
       x = [0,1]
       for k in index[2:]:
           x.append(x[k-1] + x[k-2]) 
       return x[number]
    else:
       number=-(number-1)
       index = range(number+1)
       x = [1,0]
       for k in index[2:]:
           x.append(x[k-2] - x[k-1]) 
       x.reverse()
    return x[0]
number = int(input("enter number:"))
print(f"output of fibonacci numbers:")
for i in range(-number,number + 1):
   print(f"{i}:{fibonacci(i)}")

