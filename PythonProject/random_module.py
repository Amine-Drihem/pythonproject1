import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9","10", "J", "Q", "K", "A"]

#number = random.randint(low, high)
# il donne un float entre 0 et 1 le .random()
#number = random.random()
#option = random.choice(options)
random.shuffle(cards)
print(cards)

