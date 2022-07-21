"""
CSV olusturmak
CSV okumak
data analysis
1. Clean Data
2. Store Data
3. Check Data
4. Interpret Data

"""

import numpy as np
import pandas as pd

#1. CSV file olusturmak.
dictionary = {'one':[' ',' ','3','5',' ','6','2','3'],
              'two':['2.1',' ','2.3','2.4','2.5',' ','2.5','2.3'],
              'three':['3.1','3.2','3.3',' ','3.5','3.3',' ','3.3'],
              'four':['bar',' ','club','bar','bar','club','house','club'],
              'five':['True','False','True',' ','False','True',' ','True'],
              'six':[' ','1/1/2017','2/1/2017','3/1/2017',' ','2/1/2017','4/1/2017','2/1/2017'],
              'seven':['$200.45','$650.38','$85.07',' ','$230.22','$650.96',' ','$85.07'],
              'eight':['BMC','ACS','ACS','BPS','BMC','CJS','FM','ACS']}

df_data = pd.DataFrame(data = dictionary)
print(df_data)

#2. CSV file kaydetmek.
try:
    df_data.to_csv('/Users/jordyhers/python_lessons/kz_python_2022/CSV/test.csv',
    encoding='utf-8',index=False)
    print('Csv file olusturuldu')
except:
    print(' Bir hata oldu lutfen daha sonra deneyin.')

#3. CSV file okumak
try:
    df_read = pd.read_csv('/Users/jordyhers/python_lessons/kz_python_2022/CSV/test.csv')
    print(df_read)
except:
    print('Bir hata oldu lutfen daha sonra deneyin')