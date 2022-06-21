"""
IF ELSE :

Equals: a == b. [is]
Not Equals: a != b [is not]
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

Эти условия можно использовать несколькими способами, чаще всего в операторах if и циклах.

Оператор if записывается с использованием ключевого слова if.
"""

#Отступ - 
#Python полагается на отступы (пробелы в начале строки) для определения области действия в коде. Другие языки программирования часто используют для этой цели фигурные скобки.
# if type(jordy) == int:
#     print('Jordy is an integer')

word = 'программирования'

# if len(word) == 16:
#     print('You found the right length')

# Elif
#Элиф
#Ключевое слово elif — это способ python сказать: «Если предыдущие условия были неверны, попробуйте это условие».
jordy = 40
dimash = 68
ainur = 40

# if jordy > ainur and jordy > dimash:
#     print('Jordy is the oldest')
# elif jordy == ainur or jordy == dimash:
#     print('Jordy is as old as Dimash or Ainur')
# elif ainur > dimash and ainur > jordy:
#     print('Ainur is the oldest')
# elif dimash > ainur and dimash > jordy:
#     print('Dimash is the oldest')
    
# print('Jordy : {} , Ainur: {}, Dimash: {}'.format(jordy,ainur,int(dimash)))

print('Lutfen gizli rakam bulun. 0 - 100 ')
x = 68
if x < 50 :
    print('10 dan buyuk') # ]∞;10]
    if x > 20:
        print('20 dan daha buyuk')# ]∞;20]
        if x < 50:
            print('x arasinda 50 - 20')




"""
LOOPS циклb
while в то время как
for 
"""
age = 16 #2022
# while age < 100:
#   print(' Alcohol icemezsin sen hala: {} yasindasin'.format(age))
#   if age == 18:
#       print('Yok Ama Ehliyet alabilirsin artik {} yasindasin'.format(age))
#   if age == 22:
#         print('Evet Alcohol icebilirsin')
#         break
#   age +=1
   
# i = 0
# while i < 6:
#     i+=1
#     if i == 3:
#       continue #beni atla
#     print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("artik i 6 yi ulasti")
  
  
  """
  Odev:
  
  """
text = """
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam id quam tincidunt, sollicitudin diam vel, dignissim enim. Integer id porta velit. Fusce et posuere lectus, a consequat nisl. Donec ut ex posuere, gravida ligula sit amet, rhoncus risus. Cras dapibus ipsum at nisl laoreet, ac efficitur nibh bibendum. In enim neque, dictum ac justo rhoncus, consequat faucibus urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam varius eu felis eu finibus. Sed venenatis iaculis mauris nec porta. Nullam rutrum odio egestas ligula tempor venenatis. Sed efficitur, justo vel viverra varius, lacus enim sagittis dui, id posuere lorem odio nec nisl. Ut urna lacus, convallis lobortis convallis ut, venenatis sit amet leo. Mauris facilisis vitae tellus sit amet sollicitudin.
   """
 #  Go through the entire text
   
cumle = 'Hello World My name is Jordy'

kelime_listesi = cumle.split(' ')
finst = []

  
   
   
   
   
   
   