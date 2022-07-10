

#main.py


from market import *
Shop = shop(['Banana , coca cola , sut'],[100 , 200 , 150],{'15.7.2021','25.07.2022','12.07.2022'})
Shop.shop()
print(shop)
print(validity)
print(price)


#market.py
class shop:
    def __init__ (self,name,price,validity):
        self.name=name
        self.price=price
        self.validity=validity

    def shop(self):
        return('name {} , price {} , validity {} '.format(self.name,self.price,self.validity))
        
class validity:
    def validity(self):
        global validity
        if validity == "%d" "%A" "%B" "%Y":
            print('tamam bugun son gun yaaaa '.format(self.validity))
        elif validity < "%d" "%A" "%B" "%Y":
            print('iyiyi daha alabilirsin '.format(self.validity))
        else :
            print('yok bunu alma kutu artik burada hic bir sey almam'.format(self.validity))
        
class price:
    def price(self):
        global price
        return(price * 0,22) 
        