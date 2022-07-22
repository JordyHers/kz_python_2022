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
import datetime

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
#print(df_data)

#2. CSV file kaydetmek.
# try:
#     df_data.to_csv('/Users/jordyhers/Desktop/PC/kz_python_2022/CSV/test.csv',
#     encoding='utf-8',index=False)
#     print('Csv file olusturuldu')
# except:
#     print(' Bir hata oldu lutfen daha sonra deneyin.')

#3. CSV file okumak
# try:
#     df_read = pd.read_csv('/Users/jordyhers/Desktop/PC/kz_python_2022/CSV/test.csv')
#    #print(df_read)
# except:
#     print('Bir hata oldu lutfen daha sonra deneyin')

#4. CSV file temizlemek
"""
Drop duplicated rows and keep the first.
• Replace empty values with the mean value in columns 1 and 2.
• Replace empty values with the median value in column 3.
• Replace empty values with the “club” string in column 4.
• Replace empty values with the true boolean in column 5.
• Replace empty values with the current date in column 6.
• Replace empty values with the $0.0 in column 7.
• Remove the first character (English dollar symbol $) in column 7.
• Substitute the abbreviation in column 8.
• Define x column labels.
• Define y column target.
• Save the final file as “output_data.csv”. File location path must be defined.

"""

try:
    df_read = pd.read_csv('/Users/jordyhers/Desktop/PC/kz_python_2022/CSV/test.csv')
    #1. Adim Dosyanin Detaylari almak.
    # print('1 - test.csv de Satir ve Sutun Sayisi {}'.format(df_read.shape))
    # print('2 - test.csv de info: {}'.format(df_read.info()))
    # print('3 - test.csv de tanimi: {}'.format(df_read.describe()))

    # 2. Replace empty values with the “club” string in column 4.
    #Kac veri var - sutun four icinde
    sayi = df_read['four'].value_counts()
    #FillNa funksiyonu otomatik olarak bos yerleri dolduruyor.
    df_read['four'] = df_read['four'].fillna('club')
    #print(df_read)

    # 3. Drop duplicated rows and keep the first.
    #Отбросьте повторяющиеся строки и сохраните первую.
    tekrarEden =df_read.duplicated()
    #print(tekrarEden)
    df_read = df_read.drop_duplicates(keep='first')
    #print(df_read)
    
    #4. Replace empty values with the mean value in columns 1 and 2
    #• Замените пустые значения средним значением в столбцах 1 и 2.
    ortama_one_two = df_read.mean()['one':'two']
    df_read = df_read.fillna(ortama_one_two)
    #print(df_read)

    #5. Replace empty values with the median value in column 3.
    median_three = df_read.median()[:'three']
    df_read = df_read.fillna(median_three)
    #print(df_read)

    #6. Replace empty values with the true boolean in column 5.
    df_read['five'] = df_read['five'].fillna(True)
    #print(df_read)

    #7. Replace empty values with the current date in column 6.
    bugun = datetime.datetime.now().strftime("%m/%d/%Y") #22/07/2022
    df_read['six']= df_read['six'].fillna(str(bugun))
    # tarihi str => datetime cevrilmek
    df_read['six']= pd.to_datetime(df_read['six'])
    #print(df_read)

    #8. Replace empty values with the $0.0 in column 7.
    df_read['seven'] = df_read['seven'].fillna('$0.0')
    #print(df_read)
    
    #9. Remove the first character (English dollar symbol $) in column 7.
    #map tekrar etmek icin
    df_read['seven'] = df_read['seven'].map(lambda x: str(x)[1:])
    print(df_read)

    #10 
    df_read["eight"].replace(to_replace=dict(BMC="BioMed Central",
         ACS="American Chemical Society",
         BPS="Biophysical Society",
         CJS="Cadmus Journal Services",
         FM="Frontiers Media"), inplace=True)
    #11
    x = df_read.drop(labels="eight", axis=1)
    x = df_read.iloc[:, 0:6].values
    #12
    y = df_read["eight"]
    y = df_read.iloc[:, 7].values

    #13 Save the final file as “output_data.csv”. File location path must be defined.
    df_read.to_csv('/Users/jordyhers/Desktop/PC/kz_python_2022/CSV/finished_test.csv',encoding='utf-8')
    print('Dosya Kaydedildi  Islem Bitti')
except:
    print('**Temizleme isleminde bir hata oldu **')