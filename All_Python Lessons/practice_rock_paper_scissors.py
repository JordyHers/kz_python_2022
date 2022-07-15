"""
Rock Paper Scissors
Rock:Камень
Paper:Бумага
Scissors:Ножницы:
Oppopent: противник
User: Пользователь
Random: случайный
Choice: Выбор
Tie match : Ничья.
"""
import random
import os #system
import re #RegEx split/match/replace

os.system('cls' if os.name=='nt' else 'clear')
print(" Welcome to my game ! ")

while(1 < 2):
    print(" Rock, Paper, Scissors - Shoot!")
    userChoice = input(" Choose your weapon [R]ock, [P]aper , [S]cissors :")
    
    try:
        # Kontrol yapiyorum sadece Rr,Ss Pp - Q F T felan olmaz
        if not re.match("[SsRrPp]",userChoice):
            print("Please choose a letter:")
            print("[R]ock [P]aper [S]cissors.")
            continue
        print("You chose: {}".format(userChoice.upper()))
        choices = ['R','P','S']
        opponentChoice = random.choice(choices)
        print('Computer chose: {}'.format(opponentChoice))
        if opponentChoice == str.upper(userChoice):
            print('Tie !')
        elif opponentChoice == 'R' and userChoice.upper() == 'S':
            print("Rock beats Scissors, Computer Win!")
            continue
        elif opponentChoice == 'S' and userChoice.upper() == 'P':
            print("Scissors beats Paper, Computer Win!")
            continue
        else:
            print('You Win')
    except:
        print(' ** Error Occured Please Run the Game again **')

