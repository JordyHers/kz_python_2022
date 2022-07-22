import pandas as pd
import numpy as np

#Instructions

# You are supposed to clean the data using to make the data more readable.
# To accomplish this you can use the librairies learned during the lessons.


# 1. Drop Duplicated Rows and Only keep unique ones.
# 2. All Names Should Start with a [C]apital Letter  Alexender for example
# 3. All First Names Should Be written in Capital Letters
#   3.a  If name is null a name replace it by writing False
# 4. All SSN should be unique. can not be the same.
#   4.a If SSN does not exist write 000-00-0000
# 5. Remove all negative signs from the Test3 Column
#   5.a If test value is equal to Nan replace by Test Column mean.
# 6. The new file should be saved as CSV in the path folder


#Инструкции

# Вы должны очистить данные с помощью, чтобы сделать данные более читабельными.
# Для этого вы можете использовать библиотеки, изученные на уроках.


# 1. Удалите повторяющиеся строки и оставьте только уникальные.
# 2. Все имена должны начинаться с заглавной буквы, например, Alexender.
# 3. Все имена должны быть написаны заглавными буквами
# 3.a Если имя равно null, замените его, написав False
# 4. Все SSN должны быть уникальными. не может быть одинаковым.
# 4.a Если SSN не существует, напишите 000-00-0000
# 5. Удалите все отрицательные знаки из столбца Test3
# 5.a Если тестовое значение равно Nan, замените на Test Column mean.
# 6. Новый файл должен быть сохранен как CSV в папке пути
