"""
PANDAS
CSV file
"""
import pandas as pd
import numpy as np



print("pandas version: {}".format(pd.__version__))

# Pandas icin Series kelimesi kullaniyoruz (Sutun)
data = pd.Series(np.random.randn(5))
#print(data)


#2. Pandas ile cok Series olusturabiliriz bunun adi DATAFRAME
dictionary = {"Isim":['Laura','Gulnara','Ainur','Dimash','Abduvaris','Sanzhar'],"Arasinav":[89,93,98,98,76,50],"Final":[100,100,100,100,100,50]}
df_data = pd.DataFrame(data = dictionary)


#3. Indeks olusturmak
i = 1 
index=[]
while(i<len(dictionary['Isim']) + 1):
    index.append(i)
    i+=1
df_data = pd.DataFrame(data = dictionary, index = index)
print(df_data)

#4. Dataframe den CSV format kaydetmek
"""
        Isim  Arasinav  Final
1      Laura        89    100
2    Gulnara        93    100
3      Ainur        98    100
4     Dimash        98    100
5  Abduvaris        76    100
6    Sanzhar        50     50
"""
try:
    df_data.to_csv('/Users/jordyhers/python_lessons/kz_python_2022/CSV/data.csv',encoding='utf-8')
    print('Sizin dosyaniz kaydedildi.')
    #print(output)
except:
    print(' ** Hata oldu dosya kaydedilmedi **')
  
   