#IMPORTS
import json
import os

#SETUP

#curdir = current directory
curdir = os.path.dirname(os.path.abspath(__file__))

#opens file
with open(curdir + "/actions.json", "r") as file:
    data = json.load(file)

possib = data.get("possib") # possib = possibilities

#FUNCS
def validateInput(UserInput):
    if UserInput in possib:
        return True
    else:
        return False
    
def checkDominance(action1, action2):
    if action2 in data.get(action1):
        return 1
    elif action1 == action2:
        return 0
    else:
        return 2

#MAIN CODE
while True:
    while True:
        player1 = input("Player 1: ").lower()
        if validateInput(player1) == True:
            break
        else:
            print("Action not valid. Please try again.")
            continue

    while True:
        player2 = input("Player 2: ").lower()
        if validateInput(player2) == True:
            break
        else:
            print("Action not valid. Please try again.")
            continue
    
    outcome = checkDominance(player1, player2)

    if outcome == 0:
        print("It's a draw!")
    elif outcome == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")