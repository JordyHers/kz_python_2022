""
#1.
def test(name = 'James', surname='Ben',age =12):
    print('My name is {0} {1} ,I am {2} years old,'.format(name,surname,age))
  
test('Dimash')


#2.
def sinif_ortalamasi(sinav1,sinav2,sinav3,sinav4):
    return (sinav1+sinav2+sinav3+sinav4)/4
    
ort = sinif_ortalamasi(60,82,40,91)
if ort < 50:
    print('sinavtan gecemedin tekrar kalacaksin')
elif ort <75:
    print('iyi sen aptal degilsin')
else:
    print('aferin sana')
print(ort)




'''
UYGULAMA 2
Напишите программу на Python для создания лямбда-функции,
которая добавляет 15 к заданному числу, переданному в качестве аргумента,
а также создайте лямбда-функцию, которая умножает аргумент x на аргумент y и печатает результат.


Write a Python program to create a lambda function that adds 15 to a given number 
passed in as an argument, also create a lambda function that multiplies argument 
x with argument y and print the result
Пример вывода:
25
76
'''
x= lambda a: a+15
print(x(15))
y=lambda a,b: a*b 
print(y(25,76))




"""
UYGULAMA 3
iPhone
Напишите функцию, которая будет принимать 5 аргументов. Аргументами будут цвет, 
память, модель, цена и батарея.
Функция будет использовать значения по умолчанию для каждого из параметров, чтобы убедиться,
что что-то отображается, когда пользователь их не ввел.

Write a function that will take 5 arguments. The arguments will be color, memory, model, 
price, and battery. The function will use default values for each of the parameters 
to make sure to display something when the user has not entered them.
"""
def iPhone (colors =' dark green ',memory =' 1T ',model =' iPhone 13 pro max ',price =' 1515$ ',battery = ' 4,352 mAh ' ):
    print( 'my color:' + colors +',my memory is:' + memory + ',i am new genertion:' + model + ',i am worth my money:'+price + ',i will work until you fall asleep:'+battery)
iPhone()


#_______________________________________________
"""
Uygulama 4 
Напишите 4 функции. Каждая лямбда-функция будет вычислять
1. Площадь квадрата 
2. Теорема Пифагора 
3. Площадь прямоугольника.
4. Площадь круга.
Write 4 functions. Each lambda function will calculate 
1. Area of a Square 2. Pythagorean theorem 3. Area of a Rectangle. 
4. Area of the circle
#pi = 3.14159
"""

# S= a**2
x = lambda a: a**2 
print(x(5))

# c**2 =a**2+b**2 
y = lambda a,b: ((a**2+b**2)**0,5)
print(y(3,4))


# S = a*b 
z = lambda a,b: a*b
print(z(5,9))

# S = pi*R**2
w = lambda pi,R: pi * R**2 
print(w(3.14159,4))
