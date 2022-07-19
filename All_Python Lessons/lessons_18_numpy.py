
"""
Modules 
math/json/re/urllib/camelcase;
NUMPY
"""

import numpy as np
#1. Version sorabiliriz
print('Numpy version {}'.format(np.__version__))

#2. kolayca array olusturmak 3 satir 4 sutun bir matrix
np_array = a  = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#print(a)

#3. Matrix form (kac satir ve kac sutun)
np_formu = np_array.shape
matrix = np.array([[1,2],[1,2]])
""" 1 2
    1 2 """
#print(' Bu matrix formu : {}'.format(matrix.shape))

#4. Bir rakam listesi matrix olarak sekillendirmek
matrix = np.array((1,2,3,4,5,6,7,8,9,10))
sekillendirdi = matrix.reshape(5,2)
#print(sekillendirdi)

#5.Dimensiyon sorgulamak
matrix = np.array(([1,2,3,4],[3,4,5,6]))
#print(matrix.ndim) #2

#6. Matrix boyutlari sorgulamak (kac rakam var)
matrix = np.array(([1,2,3,4],[3.0,4,5,6],[8,9,6,7]))
#print('Matrix icinde toplamda {} rakam var'.format(matrix.size))

#7. Matrix icindeki verilerin tipini sorgulamak
#print('Matrix type() : {}'.format(matrix.dtype))

#8. Matrix verilerin бит памяти
#print('Her veri бит памяти : {} bit'.format(matrix.itemsize))

#9. Iki matrix hesaplamasi
matrix1 = np.array([1,2,3,4,5])
matrix2 = np.array([3,5,6,8,6])
#____ ([1+3],[2+5],[3+6],[4+8],[5+0]])
#          [4,7,9,12,5]              
toplam = matrix1 + matrix2
eksi = matrix2 - matrix1
carpi = matrix1 * matrix2
bolu = matrix1 / matrix2
print(' Matrixlerin toplami : {}'.format(toplam))
print(' Matrixlerin eksi : {}'.format(eksi))

#10 corrcoef sorgulama
matrix1 = np.array([1,2,3,4,5])
matrix2 = np.array([3,5,6,8,0])
corrcoef = np.corrcoef(matrix1,matrix2)
#print(corrcoef)

#11 Matrix ortalamasi burada [mean = ortalama]
ortalama = np.mean(matrix1) # 1+2+3+4+5 / 5
print(' Matrix ortalamasi : {}'.format(ortalama))

# 12. Average = Ortalama
#print(np.average(matrix1))

# 13. Min ve Max 
minimum = np.min(matrix1)
maximum = np.max(matrix1)
print(' Minimum : {} ve Maximum : {} '.format(minimum,maximum))

# 14. Martrix kendisinin Toplami
print(' Matrix toplam : {}'.format(np.sum(matrix1)))
