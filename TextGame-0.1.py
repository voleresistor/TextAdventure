# **************************************
# A Text Adventure Game
# Version: 0.1
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/19/2016
# Last Edit: 04/19/2016
# **************************************
# CHANGELOG:
# 	v0.1:
# 		Add main function
# 		Add playerCommand function
# 		Add comments
# 		Add informational text at top
#		Move all the game setup into main function
#		Game is "playable" in the sense that it can take input. There is no input processing capability as of yet.
#	initial:
#		Add getAreaText function

# Set up game with some imports
import re # Regedit module

# Global "constants" to ease future editing
indexSize = 3
areaFileName = 'levels.txt'
initialLocation = '01N'

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
		getAreaText(areaFile, location)					# Get area description based on area index
		location = playerCommand(areaFile, location)	# Get command from player and update location if it changed
	
	# Self explanatory
	if gameOver == True:
		print('Game over. Better luck next time, fatso.')
		quit()
	if playerVictory == True:
		print('Looks like you won, smart guy.')
		quit()

# Get text description of current player area from file stored in memory and
# location index
# TODO: Error handling in case line index isn't matched
def getAreaText(file, index):
	# Set up file and vars for this iteration of the function
	file.seek(0,0)							# Return to top of file after each action
	lineIndex = file.readline(indexSize)	# Read first indexSize-byte index into index var
	
	# Iterate through lines until index is matched
	while lineIndex != index:
		lineDump = file.readline()				# Dump lines when previous index wasn't matched
		lineIndex = file.readline(indexSize)	# Get next index
	
	# Print the area description on screen
	if lineIndex == index:
		lineText = file.readline()	# Get line text of matching index
		print lineText				# Print the description to the console

# Get input from player and parse into a verb-noun pair
# Pass these into future functions for more detailed evaluation
def playerCommand(file, index):
	validCommand = False
	
	# Create a loop to validate player input
	# TODO: Allow verb only commands?
	while validCommand == False:
		playerInput = raw_input('> ')				# Present prompt to player and get input
		
		verb = re.search('^.*(?= )', playerInput)	# Verb should be everything before the first space
		verb = verb.group(0)						# Get our match
		
		noun = re.search('(?<= ).*$', playerInput)	# Noun should be everything after the first space
		noun = noun.group(0)						# Get that match
		
		# Pass noun-verb pair off to other functions for further processing
		if (verb == 'go') or (verb == 'move') or (verb == 'walk') or (verb == 'step'):
			validCommand = True
			# Invoke movement function
		elif (verb == 'turn'):
			validCommand = True
			# Invoke turn function
		elif (verb == 'look') or (verb == 'examine'):
			validCommand = True
			# Invoke examine function
		else:
			print('Input not recognized.\n')
	
	return index # Return new location index, even if unchanged

# That's enough functions. Time for some code.
main()
# Looks like the coding's all done!




#	Contents of levels.txt:
#	01NYou are facing North. There is a thing here.
#	02NYou are facing North. The thing is right behind you.
#	03NYou are facing North. That thing is still nearby, you can feel it.
#	04NYou are facing North. You find yourself wondering how that thing is now that you've moved away.
#	05NYou are facing North. You've temporarily forgotten the thing and become obsessed with the new wonders before you.
#	06NYou are facing North. You find the thing creeping back into your mind on occasion, slyly peeking out from behind old memories.
#	07NYou are facing North. You realize that you miss the thing and you want to return to it.

#	Sample output:
#	>python .\TextGame.py
#	You are facing North. That thing is still nearby, you can feel it.
#	
#	You are facing North. You've temporarily forgotten the thing and become obsessed with the new wonders before you.
#	>