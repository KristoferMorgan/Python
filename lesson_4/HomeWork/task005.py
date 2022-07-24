# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
x = '12*x+2y + 5 = 0'
y = '3,*,x, +, 3,y, +,3, =, 0'
def poly_add( x, y):
  r = []
  min_len = min( len(x), len(y))
  for i in range(min_len):
    if x[i][1] == y[i][1]:
      m = x[i][0] + y[i][0]
      if m != 0:
        r.append((m, x[i][1]))
    if x[i][1] != y[i][1]:
      r.append((y[i]))
      r.append((x[i]))
  return r
print((poly_add(x,y)))