"""
***************************************
SCOPE
global
Переменная доступна только внутри области, в которой она создана. Это называется размахом.
***************************************
"""

# def my_func():
#     x = '300TL'
#     def my_func_2():
#         x = '400TL'
#         print(x)
#     my_func_2()

#funk kullaniyorum    
# my_func()

# def hesaplama():
#     global fiyat
#     fiyat = 3000
    
# hesaplama()  
# son_fiyat = fiyat * 10
# print(son_fiyat)

class Person:
    def _init_(self,name,surname):
        self.name = name
        self.surname = surname
    
#Ainur insani olusturduk   
ainur = Person('ainur','Solnce')

def changeName():
    global name,surname
    if ainur.surname == 'Solnce' and ainur.name == 'ainur':
        surname = ainur.surname.upper()
        name = ainur.name.capitalize()
        
changeName()
print(name,surname)


"""
***************************************
MODULE
modul kullanmak icin 'import' kelimesi kullanman
gerekir.
***************************************
"""

# main.py _____________________________
import hesaplama
import metin
#Burada 'as' kelimesi kullaniyoruz. Uzun dosyalar icin. burada biz bbhd kullandik ama baska bir isim verebilirsiniz.
import bu_benim_hesaplama_dosyasi as bbhd
# Встроенные модули
#В Python есть несколько встроенных модулей, которые вы можете импортировать в любое время.
import platform
import datetime
system = platform.system()
date = datetime.datetime.now()
print(system,date)

hesaplama.ekleme(34,78)
bbhd.carpi(3,5)
text2 = metin.text.replace('a','@')
# print(text2)

#hesaplama.py______________________________
def ekleme(num1,num2):
    print('Cevap : {}'.format(num1+num2))
    
#metin.py_________________________________
text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content 
of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less 
normal distribution of letters, as opposed to using 'Content here, content here', making it look like 
readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their 
default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).

"""

#bu_benim_hesaplama_dosyasi.py______________
def carpi(num1,num2):
    print(num1*num2)
