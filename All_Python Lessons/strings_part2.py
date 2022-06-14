
"""
STRINGS
1. Slicing
Вы можете вернуть диапазон символов, используя синтаксис среза.
Укажите начальный и конечный индексы, разделенные двоеточием, чтобы вернуть часть строки.

2. Modifying STRINGS
3. Concatenate
4. Format STRINGS
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
#print(name[:6].lower(),surname.upper())
# print(fullname)


#3.Strip 
fullname2 = '      Dimash Omar    '
#print(fullname2.strip())

#4. Replace Letter 
# Encryption =  Шифрование
text = 'Jordy and James love Joy. They spend time together'
text2 = text.replace('J','⚰︎')
text3 = text2.replace('o','★')
text4 = text3.replace('a' ,'@')
text5 = text4.replace('e','☪︎')
text6 = text5.replace('y','⚑')
text7 = text6.replace('t','⦿')
print(text7)

#5. Split 
email = 'halinaOmar35@gmail.com'
email_1 = email.split('@')
print(email_1)


# Concatenate
name = 'Jordy'
surname = 'Hershel'

#print(name + " " + surname)

#Format STRINGS 

name = 'Jordy '
age = 35
weight = 75.6
height = 1.75
teacher = True
#print('This is {} , he is {} years old, he is {}KG and {} m'.format(name,age,weight,height))


miktar = 15.5
adet = 76
para = 760

metin = 'Lutfen elmadan {} KG , yumurta dan {} adet, bende {} TL var'
#print(metin.format(miktar,adet,para))


#Escape Characters
#1. \" \"
text = " My name is  \"Jordy\" and \"Hershel\" "
#2. \\ 

#3.New Line
text2 = "My name is Dimash Omar.\n\n\n I am 19 years old"

#4.Big space
text3 = "My name is Dimash Omar.\t\t\tI am 19 years old"
#print(text2)

#Methods 
name = 'solence'

print(name.islower())








