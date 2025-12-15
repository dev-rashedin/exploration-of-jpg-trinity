import random

low = 1
high = 100

options = ("rock", "paper", "scissors")
cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

diceNumber = random.randint(low, high) # return a random number, the first argument is for the lower bound and the second argument is for the upper bound

random.random() # return a random number between 0 and 1
random.choice(options) # return a random item from the list

randomChoice = random.choice(options)
randomCards = random.shuffle(cards)

print(randomCards)
