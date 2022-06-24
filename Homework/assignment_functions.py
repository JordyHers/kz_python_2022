"""
Самолеты ждут посадки в аэропорту. Но линии и аэропорт не совпадают.
В помощь диспетчерской вышке нам необходимо привести в порядок следующую информацию. 
Список аэропортов [JFK,IST,ANT,BKT,OPT,GHY] цвета [синий, зеленый, белый, желтый, оранжевый]. 
Все рейсы из Африки должны приземляться на желтой линии, все рейсы из Азии - на оранжевой линии, 
из Америки - в белую, из Австралии - в зеленую, а из Европы - в синюю.
"""

# List_air = [AGW,AID,JFK,LIB,OBF,KIX,NQZ,LAD,LOS,ADB,BER,SZX]
Colors = {'America':'white','Africa':'yellow','Asia':'orange','Australia':'green','Europe':'blue'}

List ={'AGW':'Australia','AID':'America','JFK':'America','LIB':'America','OBF':'Europe','KIX':'Asia','NQZ':'Kazakhstan','LAD':'Africa'}

for code in List:
    print(Colors[code])
