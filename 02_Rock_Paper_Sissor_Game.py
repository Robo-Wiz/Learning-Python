# Robo-wiz is here with another project
# This time it is a rock paper sissors game

# This first line of code imports the random module
import random

# This line of code initalizes the win count variable
win = 0

# this is a dictionary and a list for robot and human choices
gameDictionary = {'r':'rock', 'p':'paper', 's':'sissor'}
gameList = ['rock','paper','sissor']

# asks user how many times do they want to play
t = int(input("how many times do you want to play? : "))

# this loop ensures that the code runs for the amount the user asked for
for i in range(t):

    # this is the computers choice
    computer = random.choice(gameList)

    # this part asks user to make a choice
    human = input("What do you want to choose. Type r for Rock, p for Paper and s for Sissor : ")

    # these next few loops checks for the possibility of winning losing or it being a tie
    if gameDictionary[human]=='rock' and computer == 'sissor':
        # win
        print("you chose rock and computer chose sissors")
        print("you win")
        win = win+1
    elif gameDictionary[human] == 'rock' and computer == 'paper': 
        #lose
        print("you chose rock and computer chose paper")
        print("you lose")
    elif gameDictionary[human] == 'paper' and computer == 'rock':
        # win
        print("you chose paper computer chose rock")
        print("you win")
        win+=1
    elif gameDictionary[human] == 'paper' and computer == 'sissor':
        # lose
        print("you chose paper and the computer chose sissors")
        print("you lose")
    elif gameDictionary[human] == 'sissor' and computer == 'paper':
        # win
        print("you chose sissor and the computer chose paper")
        print("you win")
        win+=1
    elif gameDictionary[human] == 'sissor' and computer == 'rock':
        # lose
        print("the computer chose rock and you chose sissor")
        print("you lose")
    else:
        # tie
        print("you both chose the same options")
        print("it was a tie!")

# these final lines of code prints the final score and persuades the user to come back again
print("you won", str(win), "out of", str(t), "time(s)")
print("thank you for playing")
print("please visit again")
