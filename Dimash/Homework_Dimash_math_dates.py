

"""
ODEV
15/04/1979
4h 15min 34sec
"""
import datetime 


gun = datetime.datetime(1997,4,15,4,15,34)
print(gun)
day = gun.strftime("%d")
month = gun.strftime("%B")
year = gun.strftime("%Y")
hours = gun.strftime("%H") 
minute = gun.strftime("%M")
second = gun.strftime("%S")
print('{} {} {}. {}:{}:{}'.format(day,month,year,hours,minute,second))

