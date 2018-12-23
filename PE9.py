from random import random
from math import floor

# Blackjack.py
# calculate the probability that dealer busts given the starting card value

def main():
    printlntro ()
    n, starting_value = getlnputs()
    busts = simNGame(starting_value,n)
    printSummary(busts,starting_value,n)

def printlntro():
    print("This program simulates blackjack games.")
    print("The game is played by one dealer and one player")
    print("The probability that the dealer get a bust given the starting value will be shown in the results")

def getlnputs():
    n = int(input("How many games to simulate? "))
    starting_value = int(input("At which card does the dealer start? (from ace to 10)"))
    return n, starting_value

def simNGame(starting_value,n):
    busts = 0
    for i in range(n):
        bust = simOneGame(starting_value)
        busts = busts + bust
    return busts

def simOneGame(starting_value):
    d1 = starting_value
    d2 = simOneCard()
    d_list = [d1,d2]
    d_sum = sum(d_list)
    while not GameOver(d_sum):
        if hasAce(d_list):
            if d1 == d2:
                d_sum = d_sum + 20
            elif d1 != d2:
                if (d_sum >= 7) and (d_sum <= 11):
                    d_sum = d_sum + 10
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
    return d_sum >=17

def printSummary(busts,starting_value,n):
    # Prints a summary of dealer's bust
    print("\nGames simulated: ", n)
    print("The starting value: ",starting_value)
    print("The times and probability that dealer busts given the fixed starting value: {0} ({1: 0.1%})".format(busts, busts/n))

main()
