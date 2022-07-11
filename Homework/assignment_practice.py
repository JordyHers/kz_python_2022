"""
Create a Python programme.
The program will have a main.py and another Python file. 
(You will choose the name you wish)

The class will get 3 parameters
String name fruit
Price of fruit
Expiration date. 

The class will have has a function to calculate the expiration date of the fruits.
To calculate The expiration date add the number of letters that the fruit's name has 
to the month we are at the moment. The function will then print the expiration date of each fruit. 

The second function will calculate the tax on each fruit. 
The tax will be calculated by adding 22% of the price. 
The function will then print the result.
"""

#main.py function



#models.py function
import datetime

class Fruits:
    def __init__(self,name,price,startingDate):
        self.name = name
        self.price = price
        self.startingDate = startingDate 

    def calculateExpirationDate(self):
        letters  = len(self.name) 
        month = self.startingDate.strftime('%m')
        day = self.startingDate.strftime('%w')
        month = letters + int(month)
        expirationDate = datetime.datetime(2022,month,int(day))
        print('This {} will expire in {}'.format(self.name,expirationDate))

    def calculatePrice(self):
        price = self.price + (self.price * 0.22)
        print(' The final price is: {} TL'.format(price))
        
muz = Fruits('Muz',13.0,datetime.datetime.now())
muz.calculateExpirationDate()