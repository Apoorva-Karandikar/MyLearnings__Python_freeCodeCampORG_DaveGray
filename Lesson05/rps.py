print()
print('***  New Game    ***')

print()
playerchoice = input("Enter... \n 1 for Rock, \n 2 for Paper, or \n 3 for Scissors:\n\n")

player = int(playerchoice)

print()

import sys

if player < 1 or player > 3 :
    print("You chose : " + playerchoice)
    sys.exit('You must enter 1, 2 or 3. \n')

import random

computerchoice = random.choice("123")
computer = int(computerchoice)

print("You chose : " + playerchoice)
print("Python chose : " + computerchoice + "\n")


""" if player == 1 and computer == 3 :
    print("!!!  🎉🎉🎉  You win 🎉🎉🎉  !!!")
elif player == 2 and computer == 1 :
    print("!!!  🎉🎉🎉  You win 🎉🎉🎉  !!!")
elif player == 3 and computer == 2 :
    print("!!!  🎉🎉🎉  You win 🎉🎉🎉  !!!") """


if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("!!!  🎉🎉🎉  You win 🎉🎉🎉  !!!")
elif player == computer :
    print("XXX  ❌❌❌  Tie game    ❌❌❌  XXX")
else :
    print("💻💻💻   Python wins!    💻💻💻")

print()


from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print('\n ***   New Game (Using Enum)   *** \n')

""" print(RPS(2))
print(RPS.ROCK)
print(RPS['PAPER'])
print(RPS.SCISSORS.value) """

print("You chose : " + str(RPS(player)).replace('RPS.',''))
print("Python chose : " + str(RPS(computer)).replace('RPS.','') + "\n")


print()
