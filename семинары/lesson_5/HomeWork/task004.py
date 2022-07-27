## Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(my_string):
    encoding = ""
    prev_char = ""
    count = 1
    if not my_string:
        return ""
    for char in my_string:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
def rle_decoder(my_string):
    decode = ""
    count = ""
    for char in my_string:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ""
    return decode


variable = "aqsdwwwwwwwwwwwwwwwwqqqqqqqqqqqqsssssssssssssssaaaaaaaaaaaaaaxxxxxxxxxxxx"
print(variable)
new_variable = rle_encode(variable)
print(new_variable)
print(rle_decoder(new_variable))

