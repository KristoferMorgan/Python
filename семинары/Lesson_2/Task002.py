##  2. Напишите программу, в которой пользователь будет задавать
##  две строки, а программа - определять количество вхождений одной строки в другой.
one = "hello world world"
two = "world"
def str_count_two(one, two):
    count = 0
    i = -1
    while True:
        i = one.find(two, i+1)
        if i == -1:
            return count
        count += 1
 
print(str_count_two(one, two))




org_text = input("Введите строку: ")
find_text = input("Введите искомую строку: ")

def text_finder(org_text: str, find_text: str):
    counter = 0
    for index in range (0, len(org_text) - len(find_text)+1):
        if find_text in org_text[index:index+len(find_text)]: counter += 1
    return counter

print(f"Текст '{find_text}' втречается в тексте {text_finder(org_text, find_text)} раз")





str_1 = 'Heeeello, world!ll'
str_2 = 'll'
print(str_1.find(str_2))




str_1 = 'Hello, world!ll'
str_2 = 'll'
count = 0
for i in range(len(str_1) - len(str_2) + 1):
    if str_1[i : i + len(str_2)] == str_2:
        count += 1
print(count)
