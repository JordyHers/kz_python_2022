"""
JSON

"""
import json

"""
JSOn to Dict
"""
# some JSON formati str diye geciyor
x = '{ "name": "Peter","age":31,"city":"Adana"}'

# Bu bir dict
w = {'name':'Jordy','surname':'Hershel'}
 
naruto = {'url':'https//-0000','name':'naruto'}
# parse x:
y = json.loads(x)
print(y['age'])

"""
Dict to JSON
"""
w = {'name':'Jordy','surname':'Hershel'}
# degistirmek icin 
y = json.dumps(w)
print(y)


"""
REgEx
"""
import re 

txt = 'Jordy is my best friend'
x = re.search("^Jordy.*friend$",txt)
print(x)

txt2 = 'Ahmet ve metin birlikte metroya gidiyor'
x = re.findall('met',txt2)
print(x)

txt3 = 'Benim evim cok uzak degildir'
x = re.split("\s",txt3)
print(x)


