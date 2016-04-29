# **************************************
# A Text Adventure Game
# Version: 0.1.1
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/19/2016
# Last Edit: 04/27/2016
# **************************************
# CHANGELOG:
#	v0.1.1:
#		Create PlayerCommand class
#		Break out keywords into move or item type
#		Make getPlayerCommand use new PlayerCommand class
#		Create playerMoved function
# 	v0.1:
# 		Add main function
# 		Add playerCommand function
# 		Add comments
# 		Add informational text at top
#		Move all the game setup into main function
#		Game is "playable" in the sense that it can take input. There is no input processing capability as of yet.
#	initial:
#		Add getAreaText function

# Some indispensable imports

# Some great global "constants"
indexSize 		= 7
areaFileName 	= 'levels.txt'
initialLocation = '005050A'
moveVerbs 		= ['go','move','walk','step']
moveNouns 		= ['West','North','East','South','door','stairs']
itemVerbs 		= ['look','examine','fart','lick','take','get','touch','poke','attack']
itemNouns 		= ['thing','water','door','butt']

# Some custom classes
# Define interactable objects

# PlayerCommand class simply stores information about the last successfully parsed command
class PlayerCommandObj:
	def __init__(self, verb, verbType, noun, nounType):
		self.verb 		= verb
		self.verbType 	= verbType
		self.noun 		= noun
		self.nounType 	= nounType
		
	def describeSelf(self):
		print('Verb: {0}'.format(self.verb))
		print('Noun: {0}'.format(self.noun))
		print('VerbType: {0}'.format(self.verbType))
		print('NounType: {0}'.format(self.nounType))
	
class GridLocation:
	def __init__(self,index):
		self.index = index
		
	def getRoomDesc(self, index):
		pass

# Some fancy functions
# Main function to control the whole game
def main():
	areaFile = open(areaFileName, 'r') 	# Read our file into memory. It's a text based game so I don't think
										# storing the whole thing in memory will be an issue in 2016.
										# TODO: Find a more professional method of loading and verifying
										# this file.
	location = initialLocation 			# Set initial location at start of game
	gameOver = False 					# Game is NOT over just yet
	playerVictory = False 				# Player can't win this easily
	
	# The main loop of our game
	while (gameOver != True) or (playerVictory != True):
		getAreaText(areaFile, location)		# Get area description based on area index
		command = playerCommand()			# Get input from player and create object out of it
		#command.describeSelf()
		
		if command.nounType == 'movement':
			location = playerMoved(areaFile, command, location)
		elif command.nounType == 'action':
			playerAction()
			
	
	# Self explanatory
	if gameOver == True:
		print('Game over. Better luck next time, fatso.')
		quit()
	elif playerVictory == True:
		print('Looks like you won, smart guy.')
		quit()


# Get area text
def getAreaText(file, index):
	# Set up file and vars for this iteration of the function
	file.seek(0,0)							# Return to top of file
	lineIndex 	= file.readline(indexSize)	# Read first indexSize-bytes into index var
	
	# Iterate through lines until index is matched
	while lineIndex != index:
		lineDump 	= file.readline()				# Dump lines when previous index wasn't matched
		lineIndex 	= file.readline(indexSize)		# Get next index
	
	# Print the area description on screen
	if lineIndex == index:
		lineText = file.readline()	# Get line text of matching index
		print(lineText)				# Print the description to the console

# Update location index
# TODO: Error handling in case line index isn't matched
def playerMoved(file, command, currentIndex):
	# Break out currentIndex
	floorNum 	= currentIndex[0] + currentIndex[1]		# Read floor number
	xCoord 		= currentIndex[2] + currentIndex[3]		# Read X coordinate
	yCoord 		= currentIndex[4] + currentIndex[5]		# Read Y coordinate
	roomIter 	= currentIndex[6]						# Read room version
	
	# Build new index from currentIndex
	if (command.noun == 'West') or (command.noun == 'left'):
		xCoord = str(int(xCoord) - 1)
	if (command.noun == 'East') or (command.noun == 'right'):
		xCoord = str(int(xCoord) + 1)
	if (command.noun == 'North') or (command.noun == 'forward') or (command.noun == 'up'):
		yCoord = str(int(yCoord) + 1)
	if (command.noun == 'South') or (command.noun == 'back') or (command.noun == 'down'):
		yCoord = str(int(yCoord) - 1)
	
	# Reassemble new index and return it
	return floorNum + xCoord + yCoord + roomIter

# Get input from player and parse into a verb-noun pair
# Pass these into future functions for more detailed evaluation
def playerCommand():
	validCommand 	= False
	verbType 		= None
	nounType 		= None
	
	# Create a loop to validate player input
	# TODO: Allow verb only commands?
	while validCommand == False:
		playerInput = input('> ')				# Present prompt to player and get input
		inputWords 	= playerInput.split()		# Separate input into array of words
		
		#print('Now get verbs from: {0}'.format(inputWords))
		for word in inputWords:
			for move in moveVerbs:
				if word == move:
					verb = word
					verbType = 'movement'
					inputWords.remove(word)
					#print('Adding {0} to verb with type {1}'.format(verb, verbType))
			for action in itemVerbs:
				if word == action:
					verb = word
					verbType = 'action'
					inputWords.remove(word)
					#print('Adding {0} to verb with type {1}'.format(verb, verbType))
		
		#print('Now compare words from: {0} To words in: {1}'.format(inputWords,moveNouns))
		for word in inputWords:
			for dir in moveNouns:
				if word == dir:
					noun = word
					nounType = 'movement'
					inputWords.remove(word)
					#print('Adding {0} to noun with type {1}'.format(noun, nounType))
			for item in itemNouns:
				if word == item:
					noun = word
					nounType = 'action'
					inputWords.remove(word)
					#print('Adding {0} to noun with type {1}'.format(noun, nounType))
				
		if verbType == nounType:
			validCommand = True
			#print('Types match, returning command with following attributes:\r\nverb: {0}\r\nnoun: {1}'. format(command.verb, command.noun))
	
	return PlayerCommandObj(verb, verbType, noun, nounType) 	# Return new object containing command decryption

# That's enough functions. Time for some code.
main()
# Looks like the coding's all done!

#	Sample output:
#	>python .\TextGame.py
#	You are facing North. That thing is still nearby, you can feel it.
#	
#	You are facing North. You've temporarily forgotten the thing and become obsessed with the new wonders before you.
#	>