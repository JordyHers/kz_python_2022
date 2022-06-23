"""

LIST 
List = [0,1,True,34.8,'Jordy']
len(List)
type()
list(('elma','portakal','karpuz')) casting  ==> ['elma','portakal','karpuz']
list[1:5]
list.insert(0,'cilek')
list_a1 
list_a2.extend(list_a1)
list.remove('karpuz')
list.pop(2)
"""
# 1.Sorting strings a,b,c ......
fruits = ['Orange','mango','Kiwi','apple','banana','Pineapple']
number = [14,89,74,3,0]
#fruits.sort()
number.sort()
print(fruits)

#2. Sorting Descending z,y,x,w ....
#fruits.sort(reverse = True)
#print(fruits)


#3.lower Key case-sensitive
#fruits.sort(key = str.lower)
#print(fruits)

#4. Reverse List Order
fruits.reverse() #   is not  fruits.sort(reverse = True)
print(fruits)

"""
TUPLES are lists  using  (0,1,2) 
list = [0,1,2,3]
"""

#Кортеж — это упорядоченная и неизменяемая коллекция.
#Кортежи пишутся с круглыми скобками.

#После создания кортежа вы не можете изменить его значения. Кортежи неизменяемы, или immutable, как это еще называется.
List = ('******','HalinaOmar59@T84','test') #TUPLE
List2 = ['elma','portakal','karpuz'] #List
print(List)
yeni = list(List)
yeni[0] = 'cilek'
List = tuple(yeni)
print(List[0:2])


"""
SET 
Наборы используются для хранения нескольких элементов в одной переменной.
NOTE: * Примечание. Элементы набора нельзя изменить, но вы можете удалять элементы и добавлять новые элементы.
students = {}
list ['cilek','cilek','cilek'] ==> [0,1,2,3]
tuples ('cilek','cilek','cilek')
"""
"""
Неупорядоченный означает, что элементы в наборе не имеют определенного порядка.

Элементы набора могут появляться в другом порядке каждый раз, когда вы их используете, и на них нельзя ссылаться по индексу или ключу.
"""
students ={'Dimo','Ainur','Jordy'}
students.add('Laura')

# Update
new_students = ['Aruzhan','Osman','Nursultan','Assel','Lina','Gulnara','Ainur']
students.update(new_students)
students.remove('Dimo')
print(students)



"""
Dictionary
Элементы словаря упорядочены, изменяемы и не допускают дублирования.
"""
Jordy = {'name':'Jordy','surname':'Hershel','birth_place':'Turkey'}
Dimash = {'name':'Dimash','surname':'Omar','birth_place':'Kazakhstan'}
Car = {
  "brand": "Ford",
  "model": "Mustang",
  "year":1789,
}

print(Jordy['name'])
print(Dimash['name'])
print(len(Car))
