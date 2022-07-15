Ainur Dimash Jordy
"""
Try Except
Блок try позволяет проверить блок кода на наличие ошибок.

Блок exclude позволяет обработать ошибку.

Блок else позволяет выполнять код при отсутствии ошибок.

Блок finally позволяет выполнять код независимо от результата блоков try- и exclude.
"""

from classes import Student

ainur = Student('Ainur','Solnce',94,100,'A2')
james = Student('James','Gordon',25,45,'B1')
try:
    final = james.notHesaplama()
    james.harfNotu(final)
except:
    print('*** Yazdiklarinizi kontrol edin ***')
else:
    print(' Hic sikinti yok')
class Student:
    def __init__(self,isim,soyisim,arasinav,final,seviye):
        self.isim = isim
        self.soyisim = soyisim
        self.arasinav = arasinav
        self.final = final
        self.seviye = seviye
    
    def notHesaplama(self):
        try:
            ortalama = (self.arasinav * 2 + self.final) / 3
            print('Ogrencinin ortalamasi : {}'.format(ortalama))
            return ortalama
        except:
            print('Lutfen yanlis deger girdiniz, bir daha deneyin.')
            
    def harfNotu(self,final):
        try:
            if final < 100 and final > 90:
                return print('A+ : sinavdan gectin')
            elif final < 90 and final > 80:
                return print('B+ : sinavdan gectin')
            elif final < 80 and final > 70:
                return print('C+ : sinavdan gectin')
            elif final < 70 and final > 60:
                return print('D- : bi daha sinava gir.')
            else:
                return print('E- : {} seviyesi tekrar edeceksin'.format(self.seviye))
        except:
            print('*******************************************')
            print(' -> Girilen final notu integer yada float //')
            print('********************************************')
    
        """
User Input 
"""
class AkilliProgram:
    def __init__(self,name,surname,age,salary = 2500):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        
    def detailari_sor(self):
        print(' 1: name \n 2: surname \n 3: age \n 4: salary ')
        cevap = input('Hangi detail almak istiyorsun ? ')
        cevap = int(cevap)
        try:
            if cevap == 1:
                print(' 1 sectiniz : Name => {}'.format(self.name))
            elif cevap == 2:
                print(' 2 sectiniz : Surname => {}'.format(self.surname))
            elif cevap == 3:
                print(' 3 sectiniz : Age => {}'.format(self.age))
            elif cevap == 4:
                print(' 4 sectiniz : Salary => {}'.format(self.salary))
            else:
                print('Yanlis sectiniz sadece 1-4 arasi bir rakam secebilirsiniz')
        except:
            print('Yanlis sectiniz sadece 1-4 arasi bir rakam secebilirsiniz')

makine = AkilliProgram('Mehmet','Tozcan',34,2700)
makine.detailari_sor()

"""
String formating
"""

txt =' {1} , {0} sizi ne kadar sevmem ki '.format('Jordy','Ainur')
print(txt)


"""
File Handling

"""
#1. open('')
f = open('test.rtf')
#2. f.read(). file okumak icin
print(f.read())
