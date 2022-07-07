#_________________________
main.py

#import models
#shop = models.Shop(['shoes,clothes,SCArf,WatCHES,TIE'],{'long':51.151438,'lat': 71.475238},4,'34PUT65MD')
from models import Shop

shop = Shop(['shoes,clothes,SCArf,WatCHES,TIE'],{'long':51.151438,'lat': 71.475238},4,'34PUT65MD')
shop.writeDetails()
shop.createStock()
