# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
quater = int(input("enter the quarter number:"))
if quater == 1:
    print("the range of your coordinates  X = [0,+inf) и Y = [0,+inf)'")
elif quater == 2:
    print("the range of your coordinates X = [0,-inf) и Y = [0,+inf)")
elif quater == 3:
    print("the range of your coordinates X = [0,-inf) и Y = [0,-inf)")
elif quater == 4:
    print("the range of your coordinates X = [0,+inf) и Y = [0,-inf)")
else:
    print("you have entered the number of a non-existent plane")