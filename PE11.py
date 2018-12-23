from random import random
from math import floor

# Dice Rolling.py

def main():
    printlntro ()
    n = getlnputs()
    wins = simNGames(n)
    printSummary(n,wins)

def printlntro():
    print("This program simulates a dice rolling game.")
    print('Rolling five dices, if all five show the same number, it counts as a win.')

def getlnputs():
    n = int(input("How many games to simulate: "))
    return n

def simNGames(n):
    wins = 0
    for i in range(n):
        win = simOneGame()
        wins = wins + win
    return wins

def simOneGame():
    d1 = floor(random()*6+1)
    d2 = floor(random()*6+1)
    d3 = floor(random()*6+1)
    d4 = floor(random()*6+1)
    d5 = floor(random()*6+1)
    if d1==d2==d3==d4==d5:
        win = 1
    else:
        win = 0
    return win

def printSummary(n,wins):
    print("\nGamess simulated: ", n)
    print("The probability the five dices show the same number:",wins/n)

main()
