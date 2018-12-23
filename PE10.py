from random import random

# Monte Carlo.py
# calculate pi, using darts throwing estimation
#

def main():
    printlntro ()
    n = getlnputs()
    wins = simNGames(n)
    printSummary(n,wins)

def printlntro():
    print("This program simulates pi using dart throwing game.")
    print('If the dart lands inside the circle board, it calls a win ')
    print("pi would equal 4 times the wins divided by overall throws")

def getlnputs():
    n = int(input("How many darts to throw "))
    return n

def simNGames(n):
    wins = 0
    for i in range(n):
        win = simOneGame()
        wins = wins + win
    return wins

def simOneGame():
    loc_x = 2 * random() - 1
    loc_y = 2 * random() - 1
    if loc_x * loc_x + loc_y * loc_y <= 1:
        win = 1
    else:
        win = 0
    return win

def printSummary(n,wins):
    print("\nThrows simulated: ", n)
    pi = 4 * (wins / n)
    print("The estimated pi: ",pi)

main()
