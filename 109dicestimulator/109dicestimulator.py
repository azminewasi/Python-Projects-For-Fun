import random
print("This is a dice stimulator")

Player1=list()
Player2=list()
Player3=list()
Player4=list()
def dice(player):
    number = random.randint(1,6)
    if player=="1":
        Player1.append(number)
    elif player=="2":
        Player2.append(number)
    elif player=="3":
        Player3.append(number)
    elif player=="4":
        Player4.append(number)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")


while True:
    x=input("\n\n\nPlayer?(1/2/3/4)\n==>")
    if x!="n":
        dice(x)
    else:
        print("Player1 : ",Player1,"\nPlayer2 : ",Player2,"\nPlayer3 : ",Player3,"\nPlayer4 : ",Player4)
        break


