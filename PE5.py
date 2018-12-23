from random import random

# volleyball.py
# this time we compare two scoring: regular and rally scoring

def main():
    printlntro ()
    probA, probB, n = getlnputs()
    winsA, winsB, winsA_r, winsB_r = simNGames(n, probA, probB)
    printSummary(winsA, winsB, winsA_r, winsB_r)

def printlntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. Team A always")
    print("has the first serve.")
    print("This program also compare regular scoring to rally scoring rules.")

def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. Team A wins a serve? "))
    b = float(input("What is the prob. Team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    winsA_r = winsB_r = 0
    for i in range(n):
        scoreA, scoreB, scoreA_r, scoreB_r = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1

        if scoreA_r > scoreB_r:
            winsA_r = winsA_r + 1
        else:
            winsB_r = winsB_r + 1

    return winsA, winsB, winsA_r, winsB_r

def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    scoreA_r = 0
    scoreB_r = 0

    while not gameOver(scoreA, scoreB):
        if serving == "A" :
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"

    while not gameOver(scoreA_r, scoreB_r):
        if serving == "A" :
            if random() < probA:
                scoreA_r = scoreA_r + 1
            else:
                serving = "B"
                scoreB_r = scoreB_r + 1
        else:
            if random() < probB:
                scoreB_r = scoreB_r + 1
            else:
                serving = "A"
                scoreA_r = scoreA_r + 1

    return scoreA, scoreB, scoreA_r, scoreB_r

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a>= 25 or b>= 25) and ((a-b > 2) or (b-a > 2))

def printSummary(winsA, winsB, winsA_r, winsB_r):
    # Prints a summary of wins for each team, using two scoring system
    n1 = winsA + winsB
    n2 = winsA_r + winsB_r
    print("\nGames simulated: ", n1)
    print("For regular scoring:")
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n1))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n1))
    print("For rally scoring:")
    print("Wins for A: {0} ({1: 0.1%})".format(winsA_r, winsA_r/n2))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB_r, winsB_r/n2))

main()
