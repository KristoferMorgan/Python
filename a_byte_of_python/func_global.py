x = 50

def func():
    global x

    print("x равно", x)
    x = 2
    print("Заменяем глабальное значение x на ",x)

func()
print("Значение x составляет",x)