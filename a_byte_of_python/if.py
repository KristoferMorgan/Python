number = 23
quess = int(input("Введите число:"))

if quess == number:
    print("Поздравляю вы угадали,")# Начало нового блока
    print("(хотя и не выграли никакого приза!)")# Конец первого блока
elif quess < number:
    print("Нет,загадачное число немного больше этого.")# Ещё один блок
    #Внутри блока вы можете выполнить все что угодно...
else:
    print("Нет,загадочное число немного меньше этого")
    # чтобы попасть сюда,quess должно быть больше, чем number
print("Завершено")
# Это последнее выражение выполняется всегда после выполнения оператора if