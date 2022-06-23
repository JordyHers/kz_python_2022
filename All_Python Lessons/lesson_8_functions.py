"""
Functions

Функция — это блок кода, который запускается только при вызове.
Вы можете передавать данные, известные как параметры, в функцию.
В результате функция может возвращать данные.
"""

"""
Создание функции
В Python функция определяется с помощью ключевого слова def:
"""
def my_name():
  print("My name is Jordy")

"""
Вызов функции
Чтобы вызвать функцию, используйте имя функции, за которым следуют круглые скобки:
"""

def my_name():
  print("My name is Jordy")

my_name()

"""
Аргументы
Информация может передаваться в функции в качестве аргументов.

Аргументы указываются после имени функции в круглых скобках. Вы можете добавить столько аргументов, сколько хотите, просто разделите их запятой.

В следующем примере есть функция с одним аргументом (fname). Когда функция вызывается, мы передаем имя, которое используется внутри функции для вывода полного имени:
"""
def my_name(fname):
  print("My name is :"+ fname)

my_function("Dimash")
my_function("Ainur")
my_function("Jordy")

# def my_name(name):
#     print('My name is ' + name)

# def my_age(age):
#     print('I am {} years old'.format(age))
   
# print('What is your name ?')
# my_name('Dimash Omar')
# print('How old are you?')
# my_age(25)

#Hesap Makinesi

# benim Funksiyon
def addition(num1,num2): #добавление
    print('Сложение двух значений: {}'.format(num1 + num2))

def subtraction(num1,num2): #вычитание
    print('Сложение двух значений: {}'.format(num1 - num2))
"""
Modulus %
Floor division //
Exponentiation 2**3 = 2 x 2 x 2
"""

#________________
numara1 = 78
numara2 = 90
numara3 = 24
addition(5,3)
