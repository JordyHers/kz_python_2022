
"""
 Variables
 Переменные
 Переменные — это контейнеры для хранения значений данных.
"""

x = 5

"""
Создание переменных
В Python нет команды для объявления переменной.
Переменная создается в тот момент, когда вы впервые присваиваете ей значение.
"""
name = "Jordy"
age = 75
surname = "Hershel"
birthplace = "Turkey"
kg = 65

#print('это мое имя :' + name,'это моя фамилия' + surname, 'age' + age, 'place :' + birthplace, 'weight:' + kg )
#print()


"""
Casting 
Если вы хотите указать тип данных переменной,
это можно сделать с помощью приведения типов.
"""
age = str(75)
weight = float(89)
#print(weight)

"""
Variables types
string = " "
integer = 5 4, 56
float = 57.8
"""

name = "Dimash" 
age = 46
grade = 98.6 

grade1 = 44
grade2 = 53
grade3 = 98

(grade1 + grade2 + grade3) / 3
#print(type((grade1 + grade2 + grade3) / 3))
#print(type(name))

"""
Variables declaration mistakes
Ошибки в объявлении переменных
"""

# 1. Case the first letter is in lower case [Если первая буква в нижнем регистре]
name = 'Solnce'
time = '16.20'
 
# 2. Case the variables contains more than one word [Случай, когда переменные содержат более одного слова]
isim_soyisim = 'Dimash Omar'
name_surname = 'Ainur Solnce'
the_most_beautiful_country = 'Kazakhstan'
# print(the_most_beautiful_country)

# 3. Case the name starts with the underscore _
_myName = 'Jordy'
#print(_myName)

# 4. Case the variable has a number or a capital letter
grade1 = 75
grade2 = 45.5
myName = 'Jordy'
MYNAME = 'Dimash'


#print(grade1 * grade2)

"""
BU VARIABLES YASAK 

24myname = "James"
my-=/@var = "John"
name surname = "John"
"""


"""
Multiple variables declaration
Объявление нескольких переменных

name = 'Dimash'
surname ='Omar'
place = 'Kazakhstan'
"""


name, surname , place = 'Dimash','Omar','Kazakhstan'
#print(name,surname,place)

student1 = 'Aruzhan'
student2 = 'Aruzhan'
student3 = 'Aruzhan'

# Burada bir sikinti var [❌] Boyle YAPMAYIN 
#student1 ,student2 ,student3 = 'Aruzhan','Aruzhan','Aruzhan'

# Boyle yapin ✅ 
student1 = student2 = student3 = 'Aruzhan'

meyve1, meyve2, meyve3 = 'elma', 'portakal','cilek'
w , x , y , z  = [ 'elma', 'portakal','cilek','karpuz' ] 

"""
UYGULAMA 

Kimlik :
isim soyisim dogumyeri
x,y,v = ......,....,....
baba isim 
dogumyili
kilo
yas = 2022.......
"""

name,surname,birth_place = 'Jordy','Hershel','Turkey'
father_name = 'James'
birth_date = 2003
weight = float(75)
age = 2022 - birth_date

print( 'Name: ' + name, 'Surname: ' + surname , 'Age: ' + str(age))



















