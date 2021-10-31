import random


def start():
    print("Hello, would you like to roll the dice?\n")
    answer = input("Yes or No\n").lower()
    if "y" in answer:
        diceroll()
    else:
        exit()


def play_again():
    print("Would you  like to roll again? (yes or no)\n")
    answer = input(">").lower()

    if "y" in answer:
        diceroll()
    else:
        exit()

def diceroll():
    x = random.choice([1,2,3,4,5,6])
    print("\nThe dice rolled : " + str(x))
    play_again()

start()
