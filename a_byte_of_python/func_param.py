def printMax(a,b):
    if a > b:
        print(a,"максимальное")
    elif a == b:
        print(a ,"равно",b)
    else:
        print(b,"максимальное")
printMax(3,4) #прямая передача значений
x = 5
y = 7
printMax(x,y) # передача переменных в качестве аргументов
