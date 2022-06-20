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



Ainur = {'sinav1':45, 'sinav2':75,'sinav3':100, 'final':98}
Dimash = {'sinav1':95, 'sinav2':95,'sinav3':90, 'final':98}
Gulnara = {'sinav1':25, 'sinav2':55,'sinav3':100, 'final':48}
Laura = {'sinav1':90, 'sinav2':90,'sinav3':89, 'final':100}
Sabina = {'sinav1':45, 'sinav2':25,'sinav3':100, 'final':98}

Ainur=(45+75+100+98)/4
Dimash=(95+95+90+98)/4
Gulnara=(25+55+100+48)/4
Laura=(90+90+89+100)/4 
Sabina=(45+25+100+98)/4 
print(Ainur)
print(Dimash)
print(Gulnara)
print(Laura)
print(Sabina)


Lina = {'sinav1':80, 'sinav2':79,'sinav3':90, 'final':100}
Mira = {'sinav1':95, 'sinav2':95,'sinav3':70, 'final':55}
Osman = {'sinav1':25, 'sinav2':55,'sinav3':65, 'final':48}
Aruzhan = {'sinav1':90, 'sinav2':90,'sinav3':89, 'final':100}
Sanzhar = {'sinav1':45, 'sinav2':25,'sinav3':55, 'final':60}
Assad = {'sinav1':45, 'sinav2':46,'sinav3':47, 'final':30}
Assel = {'sinav1':95, 'sinav2':95,'sinav3':90, 'final':100}

Lina=(80+79+90+100)/4
Mira=(95+95+70+55)/4
Osman=(25+55+65+48)/4
Aruzhan=(90+90+89+100)/4 
Sanzhar=(45+25+55+60)/4 
Assad=(45+46+47+30)/4
Assel=(95+95+90+100)/4
print(Lina)
print(Mira)
print(Osman)
print(Aruzhan)
print(Sanzhar)
print(Assad)
print(Assel)


print(Ainur<65)
print(Dimash<65)
print(Gulnara<65)
print(Laura<65)
print(Sabina<65)

print(Lina<65)
print(Mira<65)
print(Osman<65)
print(Aruzhan<65)
print(Sanzhar<65)
print(Assad<65)
print(Assel<65)

# 3. Eger Ortalama > 65 bu kisi a2 grubuna ekeleyin.
# 4. Eger Ortalama < 65 Yeni bir liste olusturun (Tekrar) ve bu kisi 
# listeye ekleyin
names_a1_1=[]
names_a1_1.append('Gulnara')
print(names_a1_1)

names_a2_2=[]
names_a2_2.append('Ainur')
names_a2_2.append('Dimash')
names_a2_2.append('laura')
names_a2_2.append('Sabina')
names_a2_2.append('Osman')
names_a2_2.append('Sanzhar')
names_a2_2.append('Assad')
names_a2_2.insert(1,'Assad')
names_a2_2.insert(2,'Sanzhar')
names_a2_2.insert(3,'Sabina')
names_a2_2.pop(6)
names_a2_2.pop(8)
names_a2_2.pop(7)
print(names_a2_2)

names_B1=[]
names_B1.append('Lina')
names_B1.append('Mira')
names_B1.append('Aruzhan')
names_B1.append('Assel')
names_B1.insert(0,'Assel')
names_B1.insert(1,'Aruzhan')
names_B1.pop()
names_B1.pop()
print(names_B1)



