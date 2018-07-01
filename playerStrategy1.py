#strategy stats come from the chart created by seblau @github
countA = 0
playerResult = 0
Count = 0

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
	
def RecursiveDecision(str)
	#Surrender
	if str == "Sr":
		playerResult = 22
		supposeWin = 0.5
	#Stand
	if str == "S":
		playerResult = playerC1 + playerC2
		supposeWin = 1
	#DoubleDown
	if str == "D":
		Count = playerC1 + playerC2
		playerResult = Count.Hit()
		supposeWin = 2
	#Hit
	if str == "H":
		Count = playerC1 + playerC2
		Hitted = Count.Hit()
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
		countA1 = 0
		countA2 = 0
		playerResult1 = 0
		playerResult2 = 0
#		Count1 = playerC1
#		Count2 = playerC2
		Count = playerC1
		playerResult1 = Count.Hit()

	

#soft case
elif playerC1 == "A":
	strategyChoice = softStrategyList[playerC2 - 2][dealerC1 - 2]
elif playerC2 == "A":
	strategyChoice = softStrategyList[playerC1 - 2][dealerC1 - 2]

#hard case
else:
	strategyChoice = hardStrategyList[19 - playerC1 - playerC2][dealerC1 - 2]

	
	
	
