import time
import random

botscore = 0
userscore = 0
gift = ["🧸", "🎀", "💐", "🍫", "🎫"]

print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("enter your choice: "))
    if choice == 1:
        choicename = "Rock"
    elif choice == 2:
        choicename = "Paper"
    else:
        choicename = "Scissors"
    print()
    print("user🙍 choice is " + choicename)
    print()
    time.sleep(1)
    
    botchoice = random.randint(1,3)
    if botchoice == 1:
        botchoicename = "Rock"
    elif botchoice == 2:
        botchoicename = "Paper"
    else:
        botchoicename = "Scissors"
    print("the bot🤖 chose " + botchoicename)
    print()
    time.sleep(1)
    print(choicename + " 🆚 " + botchoicename)
    print()
    time.sleep(1)
    if choice == 1 and botchoice == 2:
        winner = "bot"
    elif choice == 1 and botchoice == 3:
        winner = "user"
    elif choice == 2 and botchoice == 1:
        winner = "user"
    elif choice == 2 and botchoice == 3:
        winner = "bot"
    elif choice == 3 and botchoice == 1:
        winner = "bot"
    elif choice == 3 and botchoice == 2:
        winner = "user"
    else:
        winner = "draw"
   

    if winner == "draw":
        print("🤷🤷🤷 😶it's a draw!😶 🤷🤷🤷")
    elif winner == "user":
        print("🎉🎉🎉 🥳you got a point🥳 🎉🎉🎉")
        userscore = userscore + 1
    else:
        print("💔💔💔 😿the bot got a point😿 💔💔💔")
        botscore = botscore + 1
    print()
    print("🤖:" + str(botscore) + " 🙍:" + str(userscore))
    print()


    if botscore == 5:
        print("the bot has won the game")
        print()
        break

    if userscore == 5:
        print("the user has won the game")
        print()
        print("you have won " + gift[random.randint(0,len(gift)- 1)] + "!")
        break
