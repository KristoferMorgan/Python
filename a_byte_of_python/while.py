number = 23
running  = True

while running:
    quess = int(input("Введите число:"))

    if quess == number:
        print("Поздравляю,вы угадяли.")
        running = False # Это останавливает цикл while
    elif quess < number:
        print("нет,заданное число несколько больше этого")
    else:
        print("нет,заданное число несколько меньше этого")
else:
    print('цикл while завершен')
    # здесь вы можете выполнить все что вам ещё нужно
print("Завершение")