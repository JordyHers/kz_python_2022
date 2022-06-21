
names_a1 = ['Ainur','Dimash','Gulnara','Laura','Sabina']
names_a2 = ['Lina','Mira','Osman','Aruzhan','Sanzhar','Assad','Assel']

# 1. Her kisi icin bir dictionary olusturun 
Ainur = {'sinav1':45, 'sinav2':75,'sinav3':100, 'final':98}
Lina = {'sinav1':75, 'sinav2':35,'sinav3':60, 'final':48}

#a1 = [Ainur,...]
#a2 = [Lina,....]

#print(Ainur['ortalamasi']< 65 )
# 2.Her kisi icin Ortalama yapip hesaplayin
# 3. Eger Ortalama > 65 bu kisi a2 grubuna ekeleyin.
# 4. Eger Ortalama < 65 Yeni bir liste olusturun (Tekrar) ve bu kisi 
# listeye ekleyin


# 1. Dictionary

Ainur = {'sinav1':45, 'sinav2':75,'sinav3':100, 'final':98}
Dimash = {'sinav1':95, 'sinav2':95,'sinav3':90, 'final':98}
Gulnara = {'sinav1':55, 'sinav2':85,'sinav3':100, 'final':88}
Laura = {'sinav1':90, 'sinav2':90,'sinav3':89, 'final':100}
Sabina = {'sinav1':45, 'sinav2':25,'sinav3':100, 'final':98}

# 1. Ortalama

Ortalama= (Ainur['sinav1']+Ainur['sinav2']+Ainur['sinav3']+Ainur['final'])
print('Ainuranin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Dimash['sinav1']+Dimash['sinav2']+Dimash['sinav3']+Dimash['final'])
print('Dimashin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Gulnara['sinav1']+Gulnara['sinav2']+Gulnara['sinav3']+Gulnara['final'])
print('Gulnaranin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Laura['sinav1']+Laura['sinav2']+Laura['sinav3']+Laura['final'])
print('Lauranin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Sabina['sinav1']+Sabina['sinav2']+Sabina['sinav3']+Sabina['final'])
print('Sabinanin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)

# 2. Dictionary

Lina = {'sinav1':80, 'sinav2':79,'sinav3':90, 'final':100}
Mira = {'sinav1':95, 'sinav2':95,'sinav3':70, 'final':55}
Osman = {'sinav1':25, 'sinav2':55,'sinav3':65, 'final':48}
Aruzhan = {'sinav1':90, 'sinav2':90,'sinav3':89, 'final':100}
Sanzhar = {'sinav1':45, 'sinav2':25,'sinav3':55, 'final':60}
Assad = {'sinav1':45, 'sinav2':46,'sinav3':47, 'final':30}
Assel = {'sinav1':95, 'sinav2':95,'sinav3':90, 'final':100}

# 2. Ortalama

Ortalama= (Lina['sinav1']+Lina['sinav2']+Lina['sinav3']+Lina['final'])
print('Linanin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Mira['sinav1']+Mira['sinav2']+Mira['sinav3']+Mira['final'])
print('Miranin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Osman['sinav1']+Osman['sinav2']+Osman['sinav3']+Osman['final'])
print('Osmanin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Aruzhan['sinav1']+Aruzhan['sinav2']+Aruzhan['sinav3']+Aruzhan['final'])
print('Aruzhanin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Sanzhar['sinav1']+Sanzhar['sinav2']+Sanzhar['sinav3']+Sanzhar['final'])
print('Sanzhrin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Assad['sinav1']+Assad['sinav2']+Assad['sinav3']+Assad['final'])
print('Assattin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)
Ortalama= (Assel['sinav1']+Assel['sinav2']+Assel['sinav3']+Assel['final'])
print('Aeselin ortalamasi :',Ortalama/4)
print(Ortalama/4<65)

names_a2_2=[]
names_a2_2.append('Ainur'),names_a2_2.append('Dimash'),names_a2_2.append('laura'),names_a2_2.append('Sabina'),names_a2_2.append('Osman'),names_a2_2.append('Sanzhar'),names_a2_2.append('Assad'),names_a2_2.append('Gulnaranin')
names_a2_2.sort()
print(names_a2_2)
names_B1=[]
names_B1.append('Lina'),names_B1.append('Mira'),names_B1.append('Aruzhan'),names_B1.append('Assel')
names_B1.sort()
print(names_B1)