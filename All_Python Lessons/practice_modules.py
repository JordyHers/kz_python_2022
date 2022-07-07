#_________________________
#main.py

#import models
#shop = models.Shop(['shoes,clothes,SCArf,WatCHES,TIE'],{'long':51.151438,'lat': 71.475238},4,'34PUT65MD')
from models import Shop

shop = Shop(['shoes,clothes,SCArf,WatCHES,TIE'],{'long':51.151438,'lat': 71.475238},4,'34PUT65MD')
shop.writeDetails()
shop.createStock()

#_________________
#models.py


class Shop:
    def __init__(self,products,location,age,license = 'AR45BT67'):
        self.products = products
        self.location = location
        self.age = age
        self.license = license
    
    
    def writeDetails(self):
        print('*****************************************************\n')
        print('products: {},location: {}, age: {}, license: {}'.format(self.products,self.location,self.age,self.license))
        
    
    def createStock(self,list_products):
        for product in list_products:
            product.capitalize()
        list_products.sort()
        if type(list_products) == list:
            new_list = set(list_products)
        print(new_list)
    
