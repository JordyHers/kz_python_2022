"""
DATETIME
"""
import datetime
"""
Когда мы выполним код из приведенного выше примера, результатом будет:
2022-07-07 14:03:20.077373
Дата содержит год, месяц, день, час, минуту, секунду и микросекунду.
"""
today = datetime.datetime.now()
print(today.year)
print(today.strftime("%W")) #Wednesday, Thursday

dogum_gunu = datetime.datetime(2003,1,15)
print(dogum_gunu)
day = dogum_gunu.strftime("%d")
month = dogum_gunu.strftime("%B")
year = dogum_gunu.strftime("%Y")
print('{} {} {}'.format(day,month,year))

"""
ODEV
15/04/1979
4h 15min 34sec
"""


"""
MATH

# 1.min() max()
x = min(34,23,79,11)
y = max(8,54,91,24)
print(x*y)

# 2.abs() |x| = x
num = abs(-7.25)
print(num)

# 3. pow() 2*2*2*2 = 2**4
num = pow(2,4)
print(num)

Математический модуль
В Python также есть встроенный модуль math, который расширяет список математических функций.

Чтобы использовать его, вы должны импортировать математический модуль:
"""
import math

# x = √20
x = math.sqrt(36)
print(x)

x = math.ceil(7.01) #8
y = math.floor(18.99999) #18
print(x,y)

pi = math.pi
print(pi)


