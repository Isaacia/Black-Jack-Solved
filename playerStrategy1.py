#strategy stats come from the chart created by seblau @github
countA = 0
playerResult = 0
Count = 0
supposeWin1 = 0
strategyChoice = "S"
playerResult1 = 0
playerResult2 = 0

doubleStrategyList = [["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"],
	["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"], 
	["H", "H", "H", "P", "P", "H", "H", "H", "H", "H"], 
	["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
	["P", "P", "P", "P", "P", "H", "H", "H", "H", "H"], 
	["P", "P", "P", "P", "P", "P", "H", "H", "H", "H"], 
	["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"], 
	["P", "P", "P", "P", "P", "S", "P", "P", "S", "S"], 
	["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	["P", "P", "P", "P", "P", "P", "P", "P", "P", "P"]] 

softStrategyList = [["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"], 
	["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"], 
	["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"], 
	["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"], 
	["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"], 
	["S", "D", "D", "D", "D", "S", "S", "H", "H", "H"], 
	["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"], 
	["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"], 
	["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]]

hardStrategyList = [["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
	["S", "S", "S", "S", "S", "H", "H", "Sr", "Sr", "H"],
	["S", "S", "S", "S", "S", "H", "H", "H", "Sr", "H"],
	["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
	["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
	["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
	["D", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
	["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
	["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
	["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
	["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
	["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
	["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"]]

if playerC1 == "A":
	playerC1 = 11
	countA += 1

if playerC2 == "A":
	playerC2 = 11
	countA += 1
	
if dealerC1 == "A":
	dealerC1 = 11

playerResult = playerC1 + playerC2
def RecursiveDecision(str)
	#Surrender
	if str == "Sr":
		playerResult = 22
		supposeWin = 0.5
	#Stand
	if str == "S":
		supposeWin = 1
	#DoubleDown
	if str == "D":
		Count = playerResult
		playerResult = Hit()
		supposeWin = 2
	#Hit
	if str == "H":
		Count = playerResult
		Hitted = Hit()
		playerResult = Hitted
		if countA > 0:
			strategyChoice = softStrategyList[Count - 13][dealerC1 - 2]
		if countA == 0:
			strategyChoice = hardStrategyList[19 - Count][dealerC1 - 2]
		RecursiveDecision(strategyChoice)
	return playerResult
	
	

#########################################################################
	
#double case
if playerC1 == playerC2:	
 	strategyChoice = doubleStrategyList[playerC1 - 2][dealerC1 - 2]
	if strategyChoice == "P"
		countA = 0
		playerResult1 = 0
		playerResult2 = 0
#First Hand
		Count = playerC1
		playerResult1 = Hit()
		if playerC1 == "A":
			countA += 1
		if countA > 0:
			strategyChoice = softStrategyList[Count - 13][dealerC1 - 2]
		else:
			strategyChoice = hardStrategyList[19 - playerC1 - playerC2][dealerC1 - 2]
		playerResult1 = RecursiveDecision(str)
		supposeWin1 = supposeWin
#Second Hand
		supposeWin = 0
		countA = 0
		Count = playerC2
		playerResult2 = Hit()
		if playerC2 == "A":
			countA += 1
		if countA > 0:
			strategyChoice = softStrategyList[Count - 13][dealerC1 - 2]
		else:
			strategyChoice = hardStrategyList[19 - playerC1 - playerC2][dealerC1 - 2]
		playerResult2 = RecursiveDecision(strategyChoice)
	else:
		playerResult = RecursiveDecision(strategyChoice)
		
			

	

####################### soft case #######################
elif playerC1 == "A" or playerC2 == "A":
	strategyChoice = softStrategyList[playerC2 + playerC1 - 13][dealerC1 - 2]
	playerResult = RecursiveDecision(strategyChoice)

####################### hard case #######################
else:
	strategyChoice = hardStrategyList[19 - playerC1 - playerC2][dealerC1 - 2]
	playerResult = RecursiveDecision(strategyChoice)




	
	
	
