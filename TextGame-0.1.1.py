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

# *******************************
# Some indispensable imports
# *******************************
import csv
import sys
import os

# *******************************
# Pre-Game setup
# *******************************
assert sys.version_info >= (3,5)
os.system('cls' if os.name=='nt' else 'clear')

# *******************************
# Some great global "constants"
# *******************************
indexSize 		= 7
areaFileName 	= 'rooms.csv'
initialLocation = '005252A'
moveVerbs 		= ['go','move','walk','step']
moveNouns 		= ['west','north','east','south','door','stairs']
itemVerbs 		= ['look','examine','fart','lick','take','get','touch','poke','attack']
itemNouns 		= ['thing','water','door','butt']

# *******************************
# Some custom classes
# *******************************
# Load data from rooms file into memory and provide functions to ease accessing that data
class RoomFile:
    def __init__(self, roomFile):
        with open(roomFile, 'rt') as roomCSV:
            roomObj = csv.reader(roomCSV, delimiter=',')
            self.roomIndex  = []
            self.roomDesc   = []
            self.roomExit   = []
            self.roomStair  = []

            for row in roomObj:
                self.roomIndex.append(row[0])
                self.roomDesc.append(row[1])
                self.roomExit.append(row[2])
                self.roomStair.append(row[3])

    def getRoomDescription(self,index):
        roomIndex = self.roomIndex.index(index)
        description = self.roomDesc[roomIndex]
        print(description)

    def getRoomExits(self,index):
        roomIndex = self.roomIndex.index(index)
        return self.roomExit[roomIndex]

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

# *******************************	
# Some fancy functions
# *******************************
# Main function to control the whole game
def main():
	Rooms = RoomFile(areaFileName)		# Create a new object containing the contents of the room file 
	
	location = initialLocation 			# Set initial location at start of game
	gameOver = False 					# Game is NOT over just yet
	playerVictory = False 				# Player can't win this easily
	
	# The main loop of our game
	while (gameOver != True) or (playerVictory != True):
		Rooms.getRoomDescription(location)			# Get area description based on area index
		command = playerCommand()					# Get input from player and create object out of it
		#command.describeSelf()
		
		if command.nounType == 'movement':
			location = playerMoved(command, location, Rooms.getRoomExits(location))
		elif command.nounType == 'action':
			playerAction()
			
	
	# Self explanatory
	if gameOver == True:
		print('Game over. Better luck next time, fatso.')
		quit()
	elif playerVictory == True:
		print('Looks like you won, smart guy.')
		quit()

# Update location index
# TODO: Error handling in case line index isn't matched
def playerMoved(command, currentIndex, currentExits):
	# Break out currentIndex
	floorNum 	= currentIndex[0] + currentIndex[1]		# Read floor number
	xCoord 		= currentIndex[2] + currentIndex[3]		# Read X coordinate
	yCoord 		= currentIndex[4] + currentIndex[5]		# Read Y coordinate
	roomIter 	= currentIndex[6]						# Read room version
	
	canMove		= True
	northExit 	= False
	southExit 	= False
	westExit 	= False
	eastExit 	= False
	
	if currentExits[0] == 'Y':
		northExit 	= True
	if currentExits[1] == 'Y':
		southExit 	= True
	if currentExits[2] == 'Y':
		westExit 	= True
	if currentExits[3] == 'Y':
		eastExit 	= True
	
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
		return floorNum + xCoord + yCoord + roomIter # Reassemble new index and return it
	else:
		print('The way is blocked!')
		return currentIndex

# Get input from player and parse into a verb-noun pair
# Pass these into future functions for more detailed evaluation
def playerCommand():
	validCommand 	= False
	verbType 		= 'a very bad verb'
	nounType 		= 'a naughty noun'
	
	# Create a loop to validate player input
	# TODO: Allow verb only commands?
	while validCommand == False:
		playerInput = input('\r\n> ')				# Present prompt to player and get input
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