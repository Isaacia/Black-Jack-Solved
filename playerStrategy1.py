#strategy stats come from the chart created by seblau @github

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
	
	
if playerC1 == "A":
	playerC1 = 11
if playerC2 == "A":
	playerC2 = 11
if dealerC1 == "A":
	dealerC1 = 11

#double case
if playerC1 == playerC2:	
 	strategyChoice = doubleStrategyList[playerC1 - 2][dealerC1 - 2]
	
