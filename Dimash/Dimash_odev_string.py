#odev  
#1
email_1= '    Yetinat@@gmail.COM   '
EX1=(email_1.strip())
EX2=(EX1.lower())
EX3=(EX2.replace("@","",1))
print(EX3)
#2
email_2='Ainur45@hotMAIL.com'
EX4=(email_2.lower())
print(EX4)
#3 
email_3=' aruzhan$2@icloud.com '
EX5=(email_3.strip())
EX6=(EX5.replace("$",""))
print(EX6)
#4 
email_4='OSCARWHITE@outlook.com'
EX7=(email_4.lower())
print(EX7)
#5 
email_5='feliciaweber@gmail.com'
print(email_5)
#6 
email_6='levi,Marco @ gmail., Com'
EX8=(email_6.lower())
EX9=(EX8.replace(',',''))
EX10=(EX9.replace(' ',''))
print(EX10)
#7 
email_7='@hotmail.com.james Horton' 
EX11=(email_7[13:])
EX12=(email_7[:12])
EX13=(EX11+EX12)
EX14=(EX13.lower())
EX15=(EX14.replace(' ',''))
print(EX15)






