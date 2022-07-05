"""
Inheritance
Наследование Питона
Наследование позволяет нам определить класс, который наследует все методы и свойства другого класса.
Родительский класс — это наследуемый класс, также называемый базовым классом.
Дочерний класс — это класс, который наследуется от другого класса, также называемого производным классом.
"""
class Person:
    def __init__(self,name,surname,salary=1500):
        self.name = name
        self.surname= surname
        self.salary = salary
    
    def getName(self):
        print('name: {}'.format(self.name)) 
        
    def getFullName(self):
        return self.name + ' ' + self.surname
        
    def isBoss(self):
        return False
        
# Inheritance Yapiyoruz burada        
class Boss(Person):
    def isBoss(self):
        return True
    
    def calculate_salary(self):
        final_salary = self.salary - (self.salary * 0.20)
        print('Your salary is {} TL'.format(final_salary))
    
list_names = ['Laura','Alina','Lina','James','Dimash','Jordy','Ainur','Kezban']

for name in list_names:
    if name == 'Jordy':
        boss_1 = Boss('Jordy','Hershel',30000)
        boss_1.getName()
        print('isBoss: {}'.format(boss_1.isBoss()))
        boss_1.calculate_salary()
    elif name == 'James':
        boss_2 = Boss('James','Cameron',10000)
        boss_2.getName()
        print('isBoss: {}'.format(boss_2.isBoss()))
        boss_2.calculate_salary()
    else:
        person = Person(name,'surname')
        person.getName()
        print('isBoss: {}'.format(person.isBoss()))
        print('No Salary, Not a Boss')
        
#_________________________________________________________________
#Baba sinifi
class Hayvanlar:
    def __init__(self,isim,kilo,boy,renk,tip='yerde'):
        self.isim = isim
        self.kilo = kilo
        self.boy = boy
        self.renk = renk
        self.tip = tip
    
    def yemek(self):
        print('{} yemek yiyebilirim'.format(self.isim))
        
    def uyumak(self):
        saat = int((self.kilo * 0.20)/5)
        print('{} saat uyuyabilirim'.format(saat))

# Cocuk sinifi
class YerdeHayvanlar(Hayvanlar):
    def surun(self):
        return True
        
    def zipla(self):
        return True
        
    def kos(self):
        return True
class UcanHayvanlar(YerdeHayvanlar):
    def ucmak(self):
        print('орел gibi ucabnilirim')
        
        
kopek_balik = Hayvanlar('kopek_balik',100,'2.3m','gri','su')
antilop = YerdeHayvanlar('antilop',150,'1.5m','kahverengi')
kartal = UcanHayvanlar('kartal',70,'78cm','kahverengi','ucan')
print(kartal.kos())



# jordy = Boss('Jordy','Hershel',3000)   
# name = jordy.getFullName()   
 
# if jordy.isBoss() == True:
#     print('Welcome Boss.')
#     jordy.calculate_salary()
# else:
#     print('{} is not a boss'.format(jordy.getFullName()))

# dimash = Person('Dimash',2000)
# dimash.getName()
# print(dimash.isBoss())

# ainur = Boss('Ainur',2000)
# ainur.getName()
# ainur.calculate_salary()
# print(ainur.isBoss())
        
        
        
