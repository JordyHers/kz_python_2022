email_1= '    Yetinat@@gmail.COM   '
step1_1 = (email_1.strip())
step1_2 = (step1_1.lower())
step1_3 = (step1_2.replace('@','', 1))
print(step1_3)

email_2= 'Ainura45@hotMAIL.com'
step2_1 = (email_2.lower())
print(step2_1)

email_3= '  aruzhan$2@icloud.com   '
step3_1 = (email_3.strip())
step3_2 = (step3_1.replace('$',''))
print(step3_2)

email_4='feliciaweber@gmail.com'
print(email_4)

email_5=' OSCARWHITE@outlook.com'
step5_1 = (email_5.strip())
step5_2 = (step5_1.lower())
print(step5_2)

email_6='Levi, Marco @ gmail., Com'
step6_1 = (email_6.lower())
step6_2 = (step6_1.replace(',',''))
step6_3 = (step6_2.replace(' ', ''))
print(step6_3)

email_7='@hotmail.com.james Horton'
step7_1 = (email_7[13:])
step7_2 = (step7_1.lower())
step7_3 = (step7_2.replace(' ',''))
step7_4 = (email_7[:12])
step7_5 = ('{}{}')
step7_6 = (step7_5.format(step7_3,step7_4))
print(step7_6)