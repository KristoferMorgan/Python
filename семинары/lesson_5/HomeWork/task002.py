###Создайте программу для игры с конфетами человек против человека.
###Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

def input_dat(name):
    x = int(input(f"player's move {name}.How many candies do you want to take?(you can take from 1 to 28): "))
    while x < 1 or x > 28:
        x = int(input(f"{name},you can take from 1 to 28: "))
    return x
def p_print(name, variable, count, sweets_on_the_table):
    print(f"player{name} has {count} candies")
    print(f"Remained  {sweets_on_the_table} candies.")
player_one = input("enter the name of the first player: ")
player_two = input("enter the name of the second player: ")
sweets_on_the_table = 2021
priority = randint(0,2)
if priority:
    print(f"the first {player_one} walks")
else:
    print(f"the first {player_two} walks")
count_one = 0 
count_two = 0
while sweets_on_the_table > 28:
    if priority:
        variable = input_dat(player_one)
        count_one += variable
        sweets_on_the_table -= variable
        priority = False
        p_print(player_one,variable,count_one,sweets_on_the_table)
    else:
        variable = input_dat(player_two)
        count_two += variable
        sweets_on_the_table -= variable
        priority = True
        p_print(player_two,variable,count_two,sweets_on_the_table)
if priority:
    print(f"Win {player_one}")
else:
    print(f"Win {player_two}")