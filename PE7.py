from random import random
from math import floor

# Craps.py
# roll a pair of dices:
# Win if roll is 7 or 11
# Lose if roll is 2, 3 or 12
# Pend if otherwise, and make a second roll
# until get the same summation, win
# until get 7 before the same summation, lose

def main():
    printlntro ()
    n = getlnputs()
    wins = simNGame(n)
    printSummary(wins,n)

def printlntro():
    print("This program simulates a game craps.")
    print('The player keeps rolling a pair of dices ')
    print('until certain criterion is met.')
    print("In each game, the player could win or lose")
    print("We simulate a number of games and calculate the probability of winning")
    print("under current rules")

def getlnputs():
    n = int(input("How many games to simulate? "))
    return n

def simNGame(n):
    wins = 0
    for i in range(n):
        win = simNRound()
        wins = wins + win
    return wins

def simNRound():
    a,b = simOneRound()
    if firstlose(a,b):
        win = 0
    elif firstwin(a,b):
        win = 1
    elif neutral(a,b):
        c,d = simOneRound()
        # print(c,d)
        while not gameOver(a,b,c,d):
            c,d = simOneRound()
            # print(c,d)
        if (c+d == 7) and (c+d != a+b):
            win = 0
        elif (c+d == a+b) :
            win = 1
    return win

def gameOver(a,b,c,d):
    return (c+d==7) or (a+b==c+d)

def simOneRound():
    a = floor(random() * 6 + 1)
    b = floor(random() * 6 + 1)
    return a,b

def firstlose(a,b):
    # a and b represent results of two dices
    # Returns True if the the sum is 2,3 or 12 False otherwise.
    return (a+b==2) or (a+b==3) or (a+b==12)

def firstwin(a,b):
    # a and b represent results of two dices
    # Returns True if the the sum is 7 or 11 False otherwise.
    return (a+b==7) or (a+b==11)

def neutral(a,b):
    return (a+b != 7) and (a+b != 11) and (a+b != 2) and (a+b != 3) and (a+b != 12)

def printSummary(wins,n):
    # Prints a summary of player's probability of winning the craps games
    print("\nGames simulated: ", n)
    print("The times and probability of winning the craps games: {0} ({1: 0.1%})".format(wins, wins/n))

main()
