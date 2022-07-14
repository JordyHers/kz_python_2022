"""
File Handling
"r" - Чтение - Значение по умолчанию.
 Открывает файл для чтения, ошибка, если файл не существует
"a" - Append - 
открывает файл для добавления, создает файл, если он не существует
"w" - Write - открывает файл для записи, создает файл, если он не существует
"x" - Создать - Создает указанный файл, возвращает ошибку, если файл существует
"""

import os 
# #1. open('')
# f = open('test.rtf')

# #2. f.read(). file okumak icin
# #print(f.read())

# #3. read lines
# print(f.readlines())

# #4. close file
# f.close()
# f = open('demofile.txt','w')
# f.write('Bu benim not dosyam. Bu dosya iceresinde kendimden bahsediyorum')
# f.close()

# #Dosyaya fazla bilgi eklemek istersin
# f = open('demofile.txt','a')
# f.write(' \n Kirmizi gul cok muhtesem. Yarin benim dersim var')
# f.close()

# #Dosyayi okumak isterim
# f = open('demofile.txt','r')
# #print(f.readlines())
# f.close()

# try:
#     #Once [x] modu ile dosyayi var olup olmadigini kontrol ediyor.
#     #eger dosya ismi varsa bi daha olusturulmayacak
#     f = open('demofile2.txt','x')
#     f.write('Bu file 2 dir.')
#     f.close()
# except:
#     print('********* HATA *********')
#     print('Bu dosya zaten var.')
#     print('************************')

#Dosyayi silmek icin bu yontemi kullanin
os.remove('demofile2.txt')
