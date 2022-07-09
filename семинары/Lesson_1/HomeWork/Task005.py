# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#  Пример:
#  - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21
import math
x1 = int(input("enter x1:")) 
y1 = int(input("enter y1:")) 
x2 = int(input("enter x2:")) 
y2 = int(input("enter y2:")) 
point_one = [x1, y1]
point_two = [x2, y2]
distance = math.sqrt( ((point_one[0]-point_two[0])**2)+((point_one[1]-point_two[1])**2) )
print(f"the distance between these points = {distance}")