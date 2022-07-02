class Havuz:
    def __init__(self,model,fiyat,renk ='mavi',boyut = {'height':'3.3m','width':'1.5m','depth':'1.80m'}):
        self.model = model
        self.renk = renk
        self.fiyat = fiyat
        self.boyut = boyut
        
    def detail_goster(self):
        print('Bu model : {} , fiyat : {} ,renk : {}, boyut: {}'.format(self.model,self.fiyat,self.renk,self.boyut))
        
    def hesaplama(self):
        pi=3.14
        r = 6
        height = 3.37
        s = pi * r * r
        print('area is : {}'.format(s))
        v = pi * r * height 
        print('volume : {}'.format(v))
        p = 2*pi*r
        print('perimeter :{}'.format(p))
         
         
BESWEY = Havuz(model='XXXL',fiyat = 529000,)
BESWEY.detail_goster()
BESWEY.hesaplama()
