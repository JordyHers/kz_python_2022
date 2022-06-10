"""
Odev 1:
Эта программа содержит ошибки. 
Найди ошибки, чтобы пробежать успешно.
"""

name = 'Payton
age = 25
country = float('USA')
job = 'Doctor'

print(" This is ", name, 'He is ',age ,' years old, and I am a ', job)



####################################################################################
"""
Odev 2. 

You have 4 hotels. Each one has its values.
Location, Price, Comfort, Visitors note, Distance from the beach, Number of rooms, 
if they have a Swimming pool (yes or no).
After, print which hotel's name is the longest 
and how many letters it has. Print each letter using [0],[1].... n,
Then print the average of all the hotel prices. Sum up all the prices and 
print which hotel is more expensive than the average.
Then you create a hotel. Write all its values and print it.


У вас есть 4 гостиницы. У каждого свои значения.
Местоположение, Цена, Комфорт, Внимание посетителей, Удаленность от пляжа, Количество комнат,
есть ли у них бассейн (да или нет).
После печати название какого отеля самое длинное
и сколько в нем букв. Выведите каждую букву, используя [0],[1].... n,
Затем выведите среднее значение всех цен на отели. Суммируйте все цены и
выведите какой отель дороже среднего.
Затем вы создаете отель. Запишите все его значения и распечатайте.

Цена будет в строке, вы должны использовать кастинг, чтобы преобразовать ее в значение с плавающей запятой.
Затем выведите лучший отель с учетом соотношения цены и качества, комфорта и удаленности от пляжа.
"""


#These are all dictionaries

LevingtonHotel = {'location' : 'Antalya', 'price':'2000', 'confort':'Very confortable','vistitors_note':'★★★★','distance':300, 'number_of_rooms':54,'swimming_pool': True}

AlmatyHotel = {'location' : 'Almaty', 'price':'5000', 'confort':'Not confortable','vistitors_note':'★★★','distance':100, 'number_of_rooms':14,'swimming_pool': False}

MevlanaHotel = {'location' : 'Istanbul', 'price':'2400', 'confort':'Best confortable','vistitors_note':'★★★★★','distance':200, 'number_of_rooms':32,'swimming_pool': True}

DoubletreeHotel = {'location' : 'Izmir', 'price':'1400', 'confort':'Very confortable','vistitors_note':'★','distance':700, 'number_of_rooms':27,'swimming_pool': True}



####################################################################################
"""
Odev 3:

Найдите, существуют ли в тексте слова из следующего списка. Если слово существует, добавьте 3 к его длине, если слово не существует, вычтите 3. Затем выведите только окончательный результат. конечным результатом является сумма всех существующих слов, умноженная на сумму всех слов, которых нет в списке.

               [admitting, Projecting, leverage, apartements, circumstances , physicality, perpetual, resolution,visitors, savage,literature,himself,carriage, vascular, ashamed, prestigious]

            ##______. print('The final result is ' + str(result)) ______##

Find if the words in the following list exist in the text. If the word exists add 3 to its length if the word does not exist subtract 3. Then only print the final result. the final result is the sum of all the words that exist multiplied by the sum of all the words which are not on the list.

"""

text = """

Turned it up should no valley cousin he. Speaking numerous ask did horrible packages set. Ashamed herself has distant can studied mrs. Led therefore its middleton perpetual fulfilled provision frankness. Small he drawn after among every three no. All having but you edward genius though remark one.

Yourself off its pleasant ecstatic now law. Ye their mirth seems of songs. Prospect out bed contempt separate. Her inquietude our shy yet sentiments collecting. Cottage fat beloved himself arrived old. Grave widow hours among him .no you led. Power had these met least nor young. Yet match drift wrong his our.

We diminution preference thoroughly if. Joy deal pain view much her time. Led young gay would now state. Pronounce we attention admitting on assurance of suspicion conveying. That his west quit had met till. Of advantage he attending household at do perceived. Middleton in objection discovery as agreeable. Edward thrown dining so he my around to.

Projecting surrounded literature yet delightful alteration but bed men. Open are from long why cold. If must snug by upon sang loud left. As me do preference entreaties compliment motionless ye literature. Day behaviour explained law remainder. Produce can cousins account you pasture. Peculiar delicate an pleasant provided do perceive.

May musical arrival beloved luckily adapted him. Shyness mention married son she his started now. Rose if as past near were. To graceful he elegance oh moderate attended entrance pleasure. Vulgar saw fat sudden edward way played either. Thoughts smallest at or peculiar relation breeding produced an. At depart spirit on stairs. She the either are wisdom praise things she before. Be mother itself vanity favour do me of. Begin sex was power joy after had walls miles.

Seen you eyes son show. Far two unaffected one alteration apartments celebrated but middletons interested. Described deficient applauded consisted my me do. Passed edward two talent effect seemed engage six. On ye great do child sorry lived. Proceed cottage far letters ashamed get clothes day. Stairs regret at if matter to. On as needed almost at basket remain. By improved sensible servants children striking in surprise.

Meant balls it if up doubt small purse. Required his you put the outlived answered position. An pleasure exertion if believed provided to. All led out world these music while asked. Paid mind even sons does he door no. Attended overcame repeated it is perceive marianne in. In am think on style child of. Servants moreover in sensible he it ye possible.

Ye on properly handsome returned throwing am no whatever. In without wishing he of picture no exposed talking minutes. Curiosity continual belonging offending so explained it exquisite. Do remember to followed yourself material mr recurred carriage. High drew west we no or at john. About or given on witty event. Or sociable up material bachelor bringing landlord confined. Busy so many in hung easy find well up. So of exquisite my an explained remainder. Dashwood denoting securing be on perceive my laughing so.

Contented get distrusts certainty nay are frankness concealed ham. On unaffected resolution on considered of. No thought me husband or colonel forming effects. End sitting shewing who saw besides son musical adapted. Contrasted interested eat alteration pianoforte sympathize was. He families believed if no elegance interest surprise an. It abode wrong miles an so delay plate. She relation own put outlived may disposed.

Am no an listening depending up believing. Enough around remove to barton agreed regret in or it. Advantage mr estimable be commanded provision. Year well shot deny shew come now had. Shall downs stand marry taken his for out. Do related mr account brandon an up. Wrong for never ready ham these witty him. Our compass see age uncivil matters weather forbade her minutes. Ready how but truth son new under.
"""

print(text)





