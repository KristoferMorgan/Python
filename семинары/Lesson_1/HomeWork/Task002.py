# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
    
x = bool(input("enter X (Enter any value to define 'true' or leave blank to define 'false'):"))
y = bool(input("enter X (Enter any value to define 'true' or leave blank to define 'false'):"))
z = bool(input("enter X (Enter any value to define 'true' or leave blank to define 'false'):"))
print(f"Х = {x}")
print(f"Y = {y}")
print(f"Z = {z}")
if not (x or y or z) == (not x and not y and not z):
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) True")
else:
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) False")