"""
STRINGS

1. Slicing
Вы можете вернуть диапазон символов, используя синтаксис среза.
Укажите начальный и конечный индексы, разделенные двоеточием, чтобы вернуть часть строки.

2. Modifying STRINGS
3. Format STRINGS
4. Concatenate
5. Escape Characters
6. String Methods

"""


#1. Slicing
text = 'Dimash Omar'
text2 = 'Hello World!'

#Direkt 0 dan basliyor
#print(text[:6])

#Direkt Sona kadar aliyor
#print(text[7:])
"""
Получить символы:
Откуда: "о" в "Мире!" (позиция -5)
Чтобы, но не включено: "д" в "Мир!" (позиция -2):
"""

#. ----> [5:2]
#.  <---  [-1:-2]
# Hello World!  <=
#print(text2[-6:])


#2. Modifying String 
#Dogru
#name , surname = 'Jordy','HERSHEL'

#Yanlis
fullname = 'Jordy Hershel'


#1.Slicing
name = fullname[:6]
surname = fullname[6:]

#2.Modifying
print(name[:6].lower(),surname.upper())
print(fullname)


#3.Strip 
fullname2 = '        Dimash Omar    '
print(fullname2.strip())







