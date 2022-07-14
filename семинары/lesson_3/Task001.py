# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

def bin_search(arr,x):
    a=0
    b=len(arr)-1
    if x<arr[0] or x>arr[b]:
        return None
    elif x==arr[0]:
        return 0
    elif x==arr[b]:
        return b
    while (b-a)>1:
        c=(a+b)//2
        if arr[c]==x:
            return c
        elif arr[c]>=x:
            b=c
        else:
            a=c
    return None
    
print(bin_search([1,3,8,9,12,14,43,67],43))
0