# **************************************
# A Text Adventure Game
# File: TAFunc.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 04/30/2016
# **************************************

# Needed to create the object to return to main function
# TODO: Is splitting into multiple files likely to get messy?
from TAClass import TACommandClass

# Update location index
# TODO: Error handling in case line index isn't matched
def playerMoved(command, room_index, roomObj):
	# Break out currentIndex
	floorNum 	= room_index[0] + room_index[1]	# Read floor number
	xCoord 		= room_index[2] + room_index[3]	# Read X coordinate
	yCoord 		= room_index[4] + room_index[5]	# Read Y coordinate
	roomIter 	= room_index[6]				# Read room version
	
	canMove		= True
	northExit 	= roomObj.getNorthExit(room_index)
	southExit 	= roomObj.getSouthExit(room_index)
	westExit 	= roomObj.getWestExit(room_index)
	eastExit 	= roomObj.getEastExit(room_index)
	
	# Build new index from currentIndex
	if (command.noun.lower() == 'west') and (westExit == True):
		xCoord = str(int(xCoord) - 1)
	elif (command.noun.lower() == 'west') and (westExit == False):
		canMove = False
		
	if (command.noun.lower() == 'east') and (eastExit == True):
		xCoord = str(int(xCoord) + 1)
	elif (command.noun.lower() == 'east') and (eastExit == False):
		canMove = False
		
	if (command.noun.lower() == 'north') and (northExit == True):
		yCoord = str(int(yCoord) + 1)
	elif (command.noun.lower() == 'north') and (northExit == False):
		canMove = False
		
	if (command.noun.lower() == 'south') and (southExit == True):
		yCoord = str(int(yCoord) - 1)
	elif (command.noun.lower() == 'south') and (southExit == False):
		canMove = False
	
	if canMove == True:
		return floorNum + xCoord + yCoord + roomIter # Reassemble and return new index
	else:
		print('The way is blocked!')
		return room_index

# Get input from player and parse into a verb-noun pair
def playerCommand(keyword):
	moveVerbs 		= ['go','move','walk','step']
	moveNouns 		= ['west','north','east','south','door','stairs']
	itemVerbs 		= ['look','examine','fart','lick','take','get','touch','poke','attack','do']
	itemNouns 		= ['room','water','door','yes','turd']
	
	validCommand 	= False
	verbType 		= 'a very bad verb'
	nounType 		= 'a naughty noun'
	
	# Create a loop to validate player input
	# TODO: Allow verb only commands?
	while validCommand == False:
		playerInput = input('\r\n> ')			# Present prompt to player and get input
		inputWords 	= playerInput.split()		# Separate input into array of words
		
		#print('Now get verbs from: {0}'.format(inputWords))
		for word in inputWords:
			for move in moveVerbs:
				if word.lower() == move:
					verb = word
					verbType = 'movement'
					inputWords.remove(word)
					#print('Adding {0} to verb with type {1}'.format(verb, verbType))
			for action in itemVerbs:
				if word.lower() == action:
					verb = word
					verbType = 'action'
					inputWords.remove(word)
					#print('Adding {0} to verb with type {1}'.format(verb, verbType))
		
		#print('Now compare words from: {0} To words in: {1}'.format(inputWords,moveNouns))
		if verbType == 'movement':
			for word in inputWords:
				for dir in moveNouns:
					if word.lower() == dir:
						noun = word
						nounType = 'movement'
						inputWords.remove(word)
						#print('Adding {0} to noun with type {1}'.format(noun, nounType))
		elif verbType == 'action':
			for word in inputWords:
				if word == keyword:
					noun = word
					nounType = 'action'
					inputWords.remove(word)
				else:
					for item in itemNouns:
						if word.lower() == item:
							noun = word
							nounType = 'action'
							inputWords.remove(word)
							#print('Adding {0} to noun with type {1}'.format(noun, nounType))
				
		if verbType == nounType:
			validCommand = True
		else:
			print('How does one {0}?'.format(playerInput))
	
	return TACommandClass(verb, verbType, noun, nounType) 	# Return new object containing command decryption