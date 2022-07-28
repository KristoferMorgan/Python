# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
x = '12*x+2y + 5 = 0'
y = '3,*,x, +, 3,y, +,3, =, 0'
import numbers
import os

def list_pr(polly_1:str,polly_2):
  polly_array_1 = polly_1.split('+')
  polly_array_2 = polly_2.split('+')
  x = ""
  y = ""
  z = ""
  numbers = ""
  new_polly = ""
  for i in polly_1,polly_2:
    for k in i:
      if k == x:
        x =x + i
      elif k == y:
        y = y + i
      elif k == z:
        z = z + i 
      else:
        numbers = numbers + i
  print(x)





polly_1 = ""
polly_2 = ""
path_polly_1 = os.path.join("Task_file","Task005-1.txt")
path_polly_2 = os.path.join("Task_file","Task005-2.txt")

with open(path_polly_1,"r") as file:
  polly_1 = file.readline()
with open(path_polly_2,"r") as file:
  polly_2 = file.readline()
print(list_pr(polly_1,polly_2))
