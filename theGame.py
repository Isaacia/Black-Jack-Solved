import random

###### Start of the game
points = 0
numGames = 0

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
		"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

pendingDeck = []

usedDeck = []

playerWincount = 0

supposeWin = 0

def Hit()
	checkRunout()
	newCard = deck.pop(0)
	pendingDeck += [newCard]
	if newCard == "A":
		countA += 1
		Count += 11
	else:
		Count += newCard
	return Count
		
	
def RecursiveHit(sum)
	if sum >= 21 and countA > 0
		sum -= 10
		countA -= 1
	if sum >= 17:
		return sum
	else:
		return RecursiveHit(Hit())

def checkRunout()
	if deck == []:
		deck = usedDeck
		usedDeck = []
		random.shuffle(deck) 

#Start Game###################################

random.shuffle(deck)    

checkRunout()
dealerC1 = deck.pop(0)	#visible to player
checkRunout()
dealerC2 = deck.pop(0)	#not visible
checkRunout()
playerC1 = deck.pop(0)
checkRunout()
playerC2 = deck.pop(0)
pendingDeck += [dealerC1, dealerC2, playerC1, playerC2]

#player's turn#############################
	import function
	
	
	
#dealer's turn##############################
countA = 0
dealerResult = 0
Count = 0

if dealerC1 == 11:
	countA += 1

if dealerC2 == "A":
	dealerC2 = 11
	countA += 1
	
Count = dealerC1 + dealerC2

#avoid two A
if Count > 21:
	Count -= 10
	countA -= 1


if Count <= 21 and Count > 16:
	dealerResult = Count

else: 
	dealerResult = RecursiveHit(Count)

	
	
	
#Compare
if playerResult > 21:
	print("Player Lose!")
	playerWinCount -= supposeWin #depends on player's previous choice;

elif dealerResult >21:
	print ("Player Win!")
	playerWinCount += supposeWin
	
else:
	if playerResult > dealerResult:
		print ("Player Win!")
		playerWinCount += supposeWin
	elif playerResult < dealerResult:
		print("Player Lose!")
		playerWinCount -= supposeWin
	else:
		print("Push!")
		
usedDeck += pendingDeck
pendingDeck = []
		
	
	
	

	
