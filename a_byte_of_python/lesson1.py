#!/a_byte_of_python\lesson1.py python3
print('привет мир!') 
#print---- эта функция

print('''Это многострочная строка.Это её первая строка.
Это её вторая строка.
"What's your name?",-спросил я.
Он ответил:"Bond,James bond"
''')

age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {} забавляется с этим Phython?'.format(name))

# десятичное число (.) с точностью в три знака для плавающих:
# '{0:.3}'.format(1/3))
a = '{0:.3}'.format(1/3)
print(a)
# заполнить подчёркиваниями(_) с центровкой текста(^) по ширине 11:
b = "{0:_^11}".format("hello")
print(b)
# по ключевым словам:
print("{name} написал {book}".format(name = "Swaroop", book ="A bate of Python"))

