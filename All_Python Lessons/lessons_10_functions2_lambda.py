"""
FUNCTIONS part 2
"""

def print_my_name(name,surname,age,birth_place):
    print('My name is ' + name + surname + 'I am ' + age +'years old' +'from '+birth_place)

# print_my_name('Dimash',' Omar','35','KZ')
# print_my_name('Jordy',' Hershel')


"""
Произвольные аргументы, *args
Если вы не знаете, сколько аргументов будет передано в вашу функцию, добавьте * перед именем параметра в определении функции.

Таким образом, функция получит кортеж аргументов и сможет получить соответствующий доступ к элементам:
"""

def my_info(*details):
    print('My name is '+ details[0] +' I am from ' + details[1] + details[2] + details[3])

# my_info('Jordy Hershel','KZ',' 1,75m ',' 75KG ')
# my_info('Ainur Solnce','KZ',' 1,65m ',' 25KG ')
# my_info('1,85m ','Dimash Omar',' 83KG ',' 3 ')

"""
Аргументы ключевых слов
Вы также можете отправлять аргументы с синтаксисом ключ = значение.

Таким образом, порядок аргументов не имеет значения.
"""

def benim_cocuklarim(cocuk3,cocuk1,cocuk2):
    print('En kucuk cocuk' + cocuk3)

# benim_cocuklarim(cocuk1 ='Ainur',cocuk2 = 'Dimash',cocuk3 =' James')


"""
Значение параметра по умолчанию
В следующем примере показано, как использовать значение параметра по умолчанию.

Если мы вызываем функцию без аргумента, она использует значение по умолчанию:
"""
def my_info(country = ' Kazakhstan',year = '1980'):
    print('I am from ' + country + ' born in '+ year)


# my_info('Turkey')
# my_info('USA','2000')
# my_info('1973')
#my_info('Kazakhstan')

"""
Возвращаемые значения
Чтобы функция возвращала значение, используйте оператор return:
"""

def hesaplama_maas(saat,ucret):
    return (saat*ucret) - 1000

maas = hesaplama_maas(153,65)
maas = hesaplama_maas(49,65)
if maas < 4500:
    print('Ты разорен и беден в этом месяце, приятель.')
elif maas > 4500 and maas < 7000:
    print('У тебя достаточно денег, ты можешь пригласить свою девушку на свидание.')
else:
    print('Ты богатый приятель.')
print(maas)

"""
LAMBDA 
Лямбда-функция — это небольшая анонимная функция.
Лямбда-функция может принимать любое количество аргументов, но может иметь только одно выражение.
"""

# def add_ten(num):
#     return num + 10
# print(add_ten(2))

x = lambda a: a + 10
print(x(10))

y = lambda a,b: a % b
print(y(20,9))

z = lambda a,b,c,w :(a+b+c)/w

print(z(6000,2000,3000,2))


