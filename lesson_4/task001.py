# Считать строку из файла.Напишите программу,которая покажет большее и
#  меньшее число.В качестве символа-разделителя используйте пробел.


def convert_to_int(str):
    return [int(x) for x in str.split()]

path =  (r'lesson_4','Task_file','task001.txt')
text = ''
with open(path , 'r') as f:
    text = f.readline()
    print(text)



int_list = convert_to_int(text)


print(int_list)
print(max(int(int_list)))
print(min(int(int_list)))