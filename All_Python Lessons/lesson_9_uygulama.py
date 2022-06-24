"""
-----------------------

Uygulama1

Есть список номеров. пожалуйста, найдите все числа, которые можно разделить на 3 и 5, и сохраните их в двух отдельных списках, называемых списками и списком 5. После этого объедините два списка в один список, а затем соедините список в набор.
3, 6 = 0
11 % 3 = 0
25 % 5 = 0 
"""
numara_listesi = [373545,436833,85559,66120,178956,85831,755619,897445,89,81,30,25,71,892327,98209,497210]

List_3 = []
List_5 = []

for num in numara_listesi:
    if num%3 ==0:
        List_3.append(num)
    elif num%5 ==0:
        List_5.append(num)
    else:
        print('5 ve 3 ile bolunmez')
print(List_3)
print(List_5)
List_5.extend(List_3)
print(set(List_5))

"""
-----------------------

UYGULAMA 2
В компании, где вы работаете, вас просят закодировать сообщение. 
Вы должны создать ключ, который является переменной DICTIONARY. 
затем отправьте ключ своему коллеге для расшифровки вашего сообщения.
"""
text = """
There are many variations of passages of Lorem Ipsum available, 
but the majority have suffered alteration in some form, by injected humour, 
or randomised words which don't look even slightly believable. If you are going 
to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing 
hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat
predefined chunks as necessary, making this the first true generator on the Internet. 
It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures,
to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore 
always free from repetition, injected humour, or non-characteristic words etc.
"""
text = """
Th⌘r⌘ 4r⌘ m4⇣^ ➤4r⎇4*⎇❡⇣s ❡f p4ss4g⌘s ❡f L❡r⌘m Ipsum 4➤4⎇l4%l⌘, %u* *h⌘ m4j❡r⎇*^ h4➤⌘ suff⌘r⌘d 4l*⌘r4*⎇❡⇣ ⎇⇣ s❡m⌘ f❡rm, %^ ⎇⇣j⌘#*⌘d hum❡ur, ❡r r4⇣d❡m⎇s⌘d w❡rds wh⎇#h d❡⇣'* l❡❡k ⌘➤⌘⇣ sl⎇gh*l^ %⌘l⎇⌘➤4%l⌘. If ^❡u 4r⌘ g❡⎇⇣g *❡ us⌘ 4 p4ss4g⌘ ❡f L❡r⌘m Ipsum, ^❡u ⇣⌘⌘d *❡ %⌘ sur⌘ *h⌘r⌘ ⎇s⇣'* 4⇣^*h⎇⇣g ⌘m%4rr4ss⎇⇣g h⎇dd⌘⇣ ⎇⇣ *h⌘ m⎇ddl⌘ ❡f *⌘x*. All *h⌘ L❡r⌘m Ipsum g⌘⇣⌘r4*❡rs ❡⇣ *h⌘ I⇣*⌘r⇣⌘* *⌘⇣d *❡ r⌘p⌘4* pr⌘d⌘f⎇⇣⌘d #hu⇣ks 4s ⇣⌘#⌘ss4r^, m4k⎇⇣g *h⎇s *h⌘ f⎇rs* *ru⌘ g⌘⇣⌘r4*❡r ❡⇣ *h⌘ I⇣*⌘r⇣⌘*. I* us⌘s 4 d⎇#*⎇❡⇣4r^ ❡f ❡➤⌘r 200 L4*⎇⇣ w❡rds, #❡m%⎇⇣⌘d w⎇*h 4 h4⇣dful ❡f m❡d⌘l s⌘⇣*⌘⇣#⌘ s*ru#*ur⌘s, *❡ g⌘⇣⌘r4*⌘ L❡r⌘m Ipsum wh⎇#h l❡❡ks r⌘4s❡⇣4%l⌘. Th⌘ g⌘⇣⌘r4*⌘d L❡r⌘m Ipsum ⎇s *h⌘r⌘f❡r⌘ 4lw4^s fr⌘⌘ fr❡m r⌘p⌘*⎇*⎇❡⇣, ⎇⇣j⌘#*⌘d hum❡ur, ❡r ⇣❡⇣-#h4r4#*⌘r⎇s*⎇# w❡rds ⌘*#.
"""
anahtar = {'a':'4',
'b':'%','c':'#',
'v':'➤','y':'^','o':'❡',
'n':'⇣','e':'⌘','i':'⎇','t':'*'}

for harf in anahtar:
    text = text.replace(harf,anahtar[harf])
print(text)
"""

-----------------------
UYGULAMA 3

Ситуации из реальной жизни. Компания продает товары в другие страны. 10% продуктов составляют кофе, 45% сахара, 25% муки и 20% соли. Цена продуктов составляет соответственно 25 TL, 32 TL, 40 TL и 8 TL. Зная, какая будет выручка, если предприятие произвело 1000,800 и 600кг продукции за 2019-2021гг.
"""
kahve = '%10 - 25TL/KG'
tuz = '%20 - 8TL/KG'
seker = '%45 - 32TL/KG'
un = '%25 - 40TL/KG'

#2019 miktar 1000KG 
def miktarHesaplamasi(miktar,yuzdesi):
    return (miktar * yuzdesi)/100

def paraHesaplamasi(miktar,fiyat):
    return (miktar * fiyat)


kahve = miktarHesaplamasi(1930,10)
seker = miktarHesaplamasi(1930,45)
tuz = miktarHesaplamasi(1930,20)
un = miktarHesaplamasi(1930,25)

kahve = paraHesaplamasi(kahve,25)
tuz = paraHesaplamasi(tuz,8)
seker = paraHesaplamasi(seker,32)
un = paraHesaplamasi(un,40)

print('Kahve {} TL, Seker {} TL,UN {} TL, Tuz {} TL'.format(kahve,seker,un,tuz))
print('Toplam : {} TL'.format(tuz+seker+un+kahve))


