import math

class Operation:
    # +
    def addition():
        print('Addition')
        numara = float(input(' Numara Gir: ')) #1 => 1.0
        t = 0
        toplam = 0
        while numara != 0:
            toplam = toplam + numara
            t+=1
            numara = float(input('Baska Numara Gir: 0 - hesaplamak icin'))
        return [toplam,t]
    # - 
    def substraction():
        print('Substraction')
        numara = float(input(' Numara Gir: ')) #1 => 1.0
        t = 0
        toplam = 0
        while numara != 0:
            toplam = abs(numara - toplam)
            t+=1
            numara = float(input('Baska Numara Gir: 0 - hesaplamak icin'))
        return [toplam,t]
    # *
    def multiplication():
        print('Multiplication')
        numara = float(input(' Numara Gir: ')) #1 => 1.0
        t = 0
        toplam = 0
        while numara != 0:
            toplam = toplam * numara
            t+=1
            numara = float(input('Baska Numara Gir: 0 - hesaplamak icin'))
        return [toplam,t]
    # /
    def average():
        print('Average')
        an = []
        an = addition()
        t = an[1]
        a = an[0]
        ans = a / t
        return [ans,t]
        
    
"""
Hesap Makinesi

"""
from operation import Operation

while True:
    list = []
    print(" ______  Hesap Makinesine Hos Geldin _____ ")
    print(" Jordy tarafindan yapildi")
    print(" Addition [+] icin 'a' basin:  ")
    print(" Substraction [-] icin 's' basin:  ")
    print(" Multiplication [*] icin 'm' basin:  ")
    print(" Average [/] icin 'v' basin:  ")
    print(" ******* Cikmak icin 'q' bas *******")
    try:
        c = input(" ")
        if c != 'q':
            if c == 'a':
                list = Operation.addition()
                print(" Cevap = {}   Numara girildi: {}".format(list[0],list[1]))
            elif c == 's':
                list = Operation.substraction()
                print(" Cevap = {}   Numara girildi: {}".format(list[0],list[1]))
            elif c == 'm':
                list = Operation.multiplication()
                print(" Cevap = {}   Numara girildi: {}".format(list[0],list[1]))
            elif c == 'v':
                list = Operation.average()
                print(" Cevap = {}   Numara girildi: {}".format(list[0],list[1]))
            else:
                print(' Yanlis rakam girdiniz')
        else:
            break
    except:
        print('_________ BIR HATA OLDU BAGLANTI KURAMADIK ______')
          
    
    
