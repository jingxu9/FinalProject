from random import random
from math import floor

# Random Walk.py

def main():
    printlntro ()
    n = getlnputs()
    steps = simNSteps(n)
    printSummary(n,steps)

def printlntro():
    print("This program simulates random walk.")
    print('At each step, player can take a step further or backward.')
    print("How many steps away from the starting point is calculated at the end.")

def getlnputs():
    n = int(input("How many steps to simulate: "))
    return n

def simNSteps(n):
    steps = 0
    for i in range(n):
        step = simOneStep()
        steps = steps + step
    return steps

def simOneStep():
    flip = floor (2 * random())
    if flip == 1:
        step = 1
    elif flip == 0:
        step = -1
    return step

def printSummary(n,steps):
    print("\nSteps simulated: ", n)
    print("How many steps away from the starting point:{0} ({1: 0.1%})".format(steps,steps/n))

main()
