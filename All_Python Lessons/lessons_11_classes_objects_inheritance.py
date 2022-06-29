"""
Classes / Objects

"""
#Sinif olusturmasi
class Person:
    def __init__(self,name,surname,age = 20):
        self.name = name
        self.surname = surname
        self.age = age
        
    def happyBirthday(self):
        print('happyBirthday ' +self.name + self.surname + 'now you are {} years old'.format(self.age+1))
    def work(self):
        print(self.name + ' is working now')
    
    def sleep(self):
        print(self.name + ' is sleeping now')
    
    def eat(self):
        print(self.name + ' is eating now')
    
#Obje olusturmasi   
Jordy = Person('Jordy','Hershel',15) 
Ainur = Person('Ainur','Solnce') 
Dimash= Person('Dimash','Omar')

Ainur.happyBirthday()
Jordy.happyBirthday()
#deger degistirmesi
Jordy.age = 16
Jordy.happyBirthday()
Jordy.age = 17
Jordy.happyBirthday()

#silmek icin 
del Jordy.age
print(Jordy.name,Jordy.surname)



class Araba:
    def __init__(self,model,fiyat,marka,renk ='siyah',boyut = {'uzunlugu':'3.3m','genislik':'1.5m','yukseklik':'1.80m'}):
        self.model = model
        self.renk = renk
        self.fiyat = fiyat
        self.marka = marka
        self.boyut = boyut
    
    def detail_goster(self):
        print('Bu model {} , marka : {} , fiyat : {} ,renk : {}, boyut: {}'.format(self.model,self.marka,self.fiyat,self.renk,self.boyut))
        
    def vergi_hesaplama(self):
        sigorta = 2000
        son_fiyat = self.fiyat + (self.fiyat * 0.20) + sigorta
        print('Senin odeceginin son fiyat : {} TL'.format(son_fiyat))
        
    
range_rover = Araba(model='EVoque',renk ='Beyaz',fiyat = 529000,marka ='Range Rover')
range_rover.detail_goster()
range_rover.vergi_hesaplama()


"""
Inheritance
Наследование Питона
Наследование позволяет нам определить класс, который наследует все методы и свойства другого класса.

Родительский класс — это наследуемый класс, также называемый базовым классом.

Дочерний класс — это класс, который наследуется от другого класса, также называемого производным классом.

"""
class Person:
    def __init__(self,name,surname,age =20):
        self.name = name
        self.surname = surname
        self.age = age
    
    
    def su_ic(self):
        print('Su icmeye zamani geldi {}'.format(self.name))
    def detail_yaz(self):
        print('Name : {} , Surname: {}'.format(self.name,self.surname))
    
Jordy = Person('Jordy','Hershel')
#Jordy.detail_yaz()

#Ogrenci sinifina Person funksiyonlari veriyorum
class Student(Person):
    def __init__(self,name,surname,age = 20):
        super().__init__(name,surname,age)
        
    def ders_calis(self):
        print('Ders calisma zamani geldi'.format(self.name))

ainur = Student('Ainur','Solnce')
ainur.ders_calis()

