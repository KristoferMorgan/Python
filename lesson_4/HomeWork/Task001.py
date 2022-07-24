# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
x = int(input(f"enter the number of decimal places:"))
print(x)
print ( round(math.pi,x) )