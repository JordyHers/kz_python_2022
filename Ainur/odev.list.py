
names_a1 = ['Ainur','Dimash','Gulnara','Laura','Sabina']
names_a2 = ['Lina','Mira','Osman','Aruzhan','Sanzhar','Assad','Assel']

Ainur = {'sinav1':45, 'sinav2':75,'sinav3':100, 'final':98}
Lina = {'sinav1':75, 'sinav2':35,'sinav3':60, 'final':48}
Dimash = {'sinav1':88, 'sinav2':78,'sinav3':85, 'final':93}
Gulnara = {'sinav1':92, 'sinav2':85,'sinav3':83, 'final':90}
Laura = {'sinav1':92, 'sinav2':86,'sinav3':93, 'final':95}
Sabina = {'sinav1':53, 'sinav2':45,'sinav3':53, 'final':60}
Mira = {'sinav1':79, 'sinav2':82,'sinav3':75, 'final':78}
Osman = {'sinav1':51, 'sinav2':48,'sinav3':45, 'final':53}
Aruzhan = {'sinav1':89, 'sinav2':93,'sinav3':95, 'final':100}
Sanzhar = {'sinav1':78, 'sinav2':63,'sinav3':59, 'final':77}
Assad = {'sinav1':65, 'sinav2':58,'sinav3':55, 'final':61}
Assel = {'sinav1':87, 'sinav2':91,'sinav3':89, 'final':95}

#Students average
Ainur_average = ((((Ainur['sinav1'])+(Ainur['sinav2'])+(Ainur['sinav3'])+(Ainur['final']))/4)>65)
Dimash_average = ((((Dimash['sinav1'])+(Dimash['sinav2'])+(Dimash['sinav3'])+(Dimash['final']))/4)>65)
Gulnara_average = ((((Gulnara['sinav1'])+(Gulnara['sinav2'])+(Gulnara['sinav3'])+(Gulnara['final']))/4)>65)
Laura_average = ((((Laura['sinav1'])+(Laura['sinav2'])+(Laura['sinav3'])+(Laura['final']))/4)>65)
Sabina_average = ((((Sabina['sinav1'])+(Sabina['sinav2'])+(Sabina['sinav3'])+(Sabina['final']))/4)>65)
Mira_average = ((((Mira['sinav1'])+(Mira['sinav2'])+(Mira['sinav3'])+(Mira['final']))/4)>65)
Osman_average = ((((Osman['sinav1'])+(Osman['sinav2'])+(Osman['sinav3'])+(Osman['final']))/4)>65)
Aruzhan_average = ((((Aruzhan['sinav1'])+(Aruzhan['sinav2'])+(Aruzhan['sinav3'])+(Aruzhan['final']))/4)>65)
Sanzhar_average = ((((Sanzhar['sinav1'])+(Sanzhar['sinav2'])+(Sanzhar['sinav3'])+(Sanzhar['final']))/4)>65)
Assad_average = ((((Assad['sinav1'])+(Assad['sinav2'])+(Assad['sinav3'])+(Assad['final']))/4)>65)
Assel_average = ((((Assel['sinav1'])+(Assel['sinav2'])+(Assel['sinav3'])+(Assel['final']))/4)>65)
print(Ainur_average,Dimash_average,Gulnara_average,Laura_average,Sabina_average,Mira_average,Osman_average,Aruzhan_average,Sanzhar_average,Assad_average,Assel_average)

a2 = (names_a1+names_a2)
a2.remove('Sabina')
a2.remove('Osman')
a2.remove('Assad')
print('A2_group: ' , a2)

a1 = list(('Sabina', 'Osman', 'Assad'))
print('A1_group: ', a1)


#a1 = [Ainur,]
#a2 = [Lina,....]

#print(Ainur['ortalamasi']< 65 )
# 2.Her kisi icin Ortalama yapip hesaplayin
# 3. Eger Ortalama > 65 bu kisi a2 grubuna ekeleyin.
# 4. Eger Ortalama < 65 Yeni bir liste olusturun (Tekrar) ve bu kisi 
# listeye ekleyin








