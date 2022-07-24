# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".



word = 'абв фгбв абв Ура,питон круто,очень интересные семинары!абв'

my_str = word.replace("абв","")
print(my_str)



my_text = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)




word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
col = word.split()
print(col)
new_col = []
search = 'абв'
for item in col:
    if search not in item:
        new_col.append(item)

print(new_col)

new_col = [item for item in col if 'абв' not in item]
print(new_col)



