from random import random
from math import floor

# Blackjack.py
# Draw cards so that total approaches to but not exceeds 21.
# This is played against dealer, to get closer to 21 than dealer (while not bust)
# A is counted as 11 when this can help the total get between 17 and 21
# A is counted as 1 otherwise
# After both dealer and player get 2 cards each, they continue one by one until one thinks he can stop

def main():
    printlntro()
    n = getlnputs()
    busts = simNGame(n)
    printSummary(busts,n)

def printlntro():
    print("This program simulates blackjack games.")
    print("The game is played by one dealer and one player")
    print("The probability that the dealer get a bust will be shown in the results")

def getlnputs():
    n = int(input("How many games to simulate? "))
    return n

def simNGame(n):
    busts = 0
    for i in range(n):
        bust = simOneGame()
        busts = busts + bust
    return busts

def simOneGame():
    d1 = simOneCard()
    d2 = simOneCard()
    # print(d1,d2)
    d_list = [d1,d2]
    d_sum = sum(d_list)
    while not GameOver(d_sum):
        if hasAce(d_list):
            if d1 == d2:
                d_sum = d_sum + 18
            elif d1 != d2:
                if (d_sum >= 7) and (d_sum <= 11):
                    d_sum = d_sum + 9
                else:
                    d_list.append(simOneCard())
                    d_sum = sum(d_list)
            # print('Playing', d_sum, GameOver(d_sum))
        else:
            d_list.append(simOneCard())
            d_sum = sum(d_list)
    if d_sum > 21:
        bust = 1
    else:
        bust = 0
    return bust

def hasAce(list):
    if 1 in list:
        return True
    return False

def simOneCard():
    card=floor(random()*13 + 1)
    if (card == 11) or (card == 12) or (card == 13):
        card = 10
    else:
        card = card
    return card

def GameOver(d_sum):
    return d_sum >= 17

def printSummary(busts,n):
    # Prints a summary of dealer's bust
    print("\nGames simulated: ", n)
    print("The times and probability that dealer busts: {0} ({1: 0.1%})".format(busts, busts/n))

main()
