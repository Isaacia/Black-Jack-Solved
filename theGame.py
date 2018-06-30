import random

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

#Start Game

random.shuffle(deck)    #

dealerC1 = deck.pop(0)
dealerC2 = deck.pop(0)
playerC1 = deck.pop(0)
playerC2 = deck.pop(0)
