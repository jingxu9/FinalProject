from random import random

# tabletennis.py
# simulate table tennis: 11 scores to win a game given the winner has at least 2 scores higher
# this time use rally scoring: both server or non-server get the score when win the rally
# also, first serve in each game alternates, starting from A

def main():
    printlntro ()
    probA, probB, n = getlnputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printlntro():
    print("This program simulates a game of table tennis between two")
    print('teams called "A" and "B", using rally scoring. ')
    print('The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. Team A always")
    print("has the first serve.")

def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. Team A wins a serve? "))
    b = float(input("What is the prob. Team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB= simOneGame(probA, probB,i)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB,i):
    if i % 2==1:
        serving = "A"
        scoreA = 0
        scoreB = 0
        while not gameOver(scoreA, scoreB):
            if serving == "A" :
                if random() < probA:
                    scoreA = scoreA + 1
                else:
                    serving = "B"
                    scoreB = scoreB + 1
            else:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    serving = "A"
                    scoreA = scoreA + 1
    elif i % 2 ==0:
        serving = "B"
        scoreA = 0
        scoreB = 0
        while not gameOver(scoreA, scoreB):
            if serving == "A" :
                if random() < probA:
                    scoreA = scoreA + 1
                else:
                    serving = "B"
                    scoreB = scoreB + 1
            else:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    serving = "A"
                    scoreA = scoreA + 1
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a>= 11 or b>= 11) and ((a-b > 2) or (b-a > 2))

def printSummary(winsA, winsB):
    # Prints a summary of wins for each team, using two scoring system
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Table Tennis Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Table Tennis Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))

main()
