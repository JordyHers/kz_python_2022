#5.Элементы списка — типы данных
#Элементы списка могут иметь любой тип данных:

answer_list =[True,False,True,True,False]
age_list = [21,18,32,14,8,45]
kg_list = [56.005,73.9,82.90]
all_list = ['Orange',True,35,['test1','test2'],56.0]

# for x in range(0,5):
#     print(type(all_list[x]))
# print(type(all_list[0]))
# print(type(all_list[1]))
# print(type(all_list[2]))
# print(type(all_list[3]))
# print(type(all_list[4]))

meyve,sebze,yemek = 'portakal','patates','yumurta'
alisveris = list((meyve,sebze,yemek)) #mutlaka (()) parentez koyun
#print(alisveris)
#print('Sanzhar' in names_a2)


#6. Чтобы изменить значение определенного элемента, обратитесь к номеру индекса:

names_a1 = ['Aaeinur','Dimasssrh','Gulnaaaara','Laura','Sabina']
names_a2 = ['Lina','Mira','Osman','Aruzhan','Sanzhar','Assad','Assel']

names_a1[0:3] = ['Ainur','Dimash','Gulnara']
#print(names_a1[0:3])

#names_a2[1:3]= []
#print(names_a2)

#insert methodu sirayi degistirmek icin [0,1,2,3,4,'Assel']
#names_a2.insert(3,'Jordy')
#print(names_a2)

#Добавить элементы
#Чтобы добавить элемент в конец списка, используйте метод append():
#names_a1.append('Tarkan')
#print(names_a1)

names_b2 = [] #0,1,2,3,....
# names_b2.append('James')
# names_b2.append('Halina')
# names_b2.append('Ainur') #['James','Halina',     , 'Ainur']
# names_b2.insert(2,'Jordy') 
#print(names_b2)

#Расширить список
#Чтобы добавить элементы из другого списка в текущий список, используйте метод extend().

# [Lina,'Aruzhan','Ainur','Dimash']
# names_a1.extend(names_a2)
# print(names_a2)
# print(names_a1)
# names_a2.extend(names_a1)
# names_b2.extend(names_a2)

# Удалить указанный элемент
# Метод remove() удаляет указанный элемент.
# names_a1.remove('Sabina')

# Удалить указанный индекс
# Метод pop() удаляет указанный индекс.
names_a1.pop(4)
#print(names_a1)

names_a2.insert(0,'Sanzhar')
names_a2.remove('Sanzhar') # ikinci Sanzhar silmek icin
#print(names_a2)



sanzhar = ['Jordy','Sanzhar','Sanzhar','James','Sanzhar']
sanzhar.pop(1)
print(sanzhar)
sanzhar.pop(1)
print(sanzhar)













names_a1 = ['Ainur','Dimash','Gulnara','Laura','Sabina']
names_a2 = ['Lina','Mira','Osman','Aruzhan','Sanzhar','Assad','Assel']

# 1. Her kisi icin bir dictionary olusturun 
Ainur = {'sinav1':45, 'sinav2':75,'sinav3':100, 'final':98}
Lina = {'sinav1':75, 'sinav2':35,'sinav3':60, 'final':48}

a1 = [Ainur,...]
a2 = [Lina,....]

print(Ainur['ortalamasi']< 65 )
# 2.Her kisi icin Ortalama yapip hesaplayin
# 3. Eger Ortalama > 65 bu kisi a2 grubuna ekeleyin.
# 4. Eger Ortalama < 65 Yeni bir liste olusturun (Tekrar) ve bu kisi 
# listeye ekleyin

