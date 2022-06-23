
"""
BOOLEANS
TRUE ve FALSE
"""
# print(bool(None))
# print(bool(False))
# print(bool(0))
# print(bool([]))
# print(bool({}))
# print(bool('Ture'))



"""
OPERATORS

Arithmetic operators
Assignment operators
Comparison operators
Logical operators

"""
# print(56 + 67)
# print(56 - 67)
# print(7 * 8)
# print(45 / 9)

#Modulus
#print(79 % 4)

#Exponentiation
#print(3**3)  3x3x3

#Floor division
print(25//2)
#2.9999909 = 2.0
#4. Assignment operators
x = 25

# x = x + 3
#x+=3

# x = x * 9 
#x *=9

#x = x / 5
x /=5
#print(x)

"""
COMPARISON operators
 
"""
#1. ==
x = 5
y = 5
print(x == y)


#2. != 
x = 7
y = 5
#print(x != y)

#3. >dan buyuk  < dan Kucuk
x = 7
y = 5
#print(x < y)

#4. >= daha buyuk yada esit
x = 7
y = 5
#print(x >= y)

#5. <= daha kucuk yada esit
x = 7
y = 5
#print(x <= y)


"""
Logical operators
and / or / not 
"""
#Возвращает True, если оба утверждения верны
# print(5>3 and 6<18)
# print(56>89 and 90>30)

#Возвращает True, если одно из утверждений верно
# print()
# print(5>3 or 6<18)
# print(56>89 or 90>30)

#not Обратный результат, возвращает False, если результат истинный
# print(not(-2))
# print(not(False))

"""
IDENTITY and MEMBERSHIP
is / is not 
in /not in 
"""
#is Возвращает True, если обе переменные являются одним и тем же объектом

iPhone13 = {'color':'blue','memory':'256GB','Camera':'12mpx','price':'14.000TL'}
iPhone12ProMax = {'color':'blue','memory':'256GB','Camera':'12mpx','price':'14.000TL'}

print(iPhone13 is not iPhone12ProMax)

#in ve not in Возвращает True, если в объекте присутствует последовательность с указанным значением
text = 'This is my name Jordy.'
print('Jordy' not in text)




