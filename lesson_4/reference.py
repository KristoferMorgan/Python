#cd ''

...
# Режимы 
# 
#  a - добавить и читать 
#  w - писать
#  r - читать





import os                                                                          

##path = 'folder + os.sep + file.txt'                                                ## or
##path = os.path.join('folder','file.txt')                                           ## or
path = r'lesson_4/file.txt'
with open (path,'r') as f:
#    data = f.read()                                                        #можно забить память
#    print(data)
    data = f.readlines()
    print(data)
##                    as data:                                                        # or
#   for line in data:
#   print(line)


##with open (part , w ) as data:
##      print(type(data))

