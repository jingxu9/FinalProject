from random import random
from math import floor
from math import sqrt

# Random Walk.py

def main():
    printlntro ()
    n = getlnputs()
    distance = simNSteps(n)
    printSummary(n,distance)

def printlntro():
    print("This program simulates random walk.")
    print('At each step, player can take a step further or backward or left or right.')
    print("Distance away from the starting point is calculated at the end.")

def getlnputs():
    n = int(input("How many steps to simulate: "))
    return n

def simNSteps(n):
    horizontals = 0
    verticals = 0
    for i in range(n):
        horizontal,vertical = simOneStep()
        horizontals = horizontals + horizontal
        verticals = verticals + vertical
    distance = sqrt(horizontals * horizontals + verticals * verticals)
    return distance

def simOneStep():
    flip = floor (4 * random()+1)
    if flip == 1:
        horizontal = 0
        vertical = 1
    elif flip == 2:
        horizontal = 1
        vertical = 0
    elif flip == 3:
        horizontal = 0
        vertical = -1
    elif flip == 4:
        horizontal = -1
        vertical = 0
    return horizontal,vertical

def printSummary(n,distance):
    print("\nSteps simulated: ", n)
    print("Distance away from the starting point:", distance)

main()
