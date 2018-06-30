import random

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
usedDeck = []

#Start Game

random.shuffle(deck)    

dealerC1 = deck.pop(0)	#visible to player
dealerC2 = deck.pop(0)	#not visible
playerC1 = deck.pop(0)
playerC2 = deck.pop(0)

#player's turn
	import function
	
	
	
#dealer's turn
dcountA = 0
dealerResult = 0
if dealerC1 == "A":
	#ask player for insurance

	dealerCount = 0
if dealerC1 == "A":
	dealerC1 = 11
	dcountA += 1

if dealerC2 == "A":
	dealerC2 = 11
	dcountA += 1
	
dealerCount = dealerC1 + dealerC2

#avoid two A
if dealerCount > 21:
	dealerCount -= 10
	dcountA -= 1


if dealerCount <= 21 and dealerCount > 16:
	dealerResult = dealerCount

if dealerCount <= 16:
	dealerCount.hit()
	
	
	

	
	
	
		else:
		print ("Player Win!")
		playerWinCount += supposeWin #depends on player's previous choice;
