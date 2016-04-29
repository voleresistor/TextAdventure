# **************************************
# A Text Adventure Game
# File: TAMain.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 04/29/2016
# **************************************

# Import our new files
import TAClass
import TAFunc

# Main function to control the whole game
def main():
	rooms = TAClass.RoomsFile('rooms.csv')	# Create a new object containing the contents of the room file
	#items = TAClass.ItemsFile('items.csv')	# Create a new object containing the contents of the items file
	
	location = '005252A'			 		# Set initial location at start of game
	gameOver = False 						# Game is NOT over just yet
	playerVictory = False 					# Player can't win this easily
	
	# The main loop of our game
	while (gameOver != True) or (playerVictory != True):
		rooms.getRoomDescription(location)			# Get area description based on area index
		command = TAFunc.playerCommand()			# Get input from player and create object out of it
		#command.describeSelf()
		
		if command.nounType == 'movement':
			location = TAFunc.playerMoved(command, location, rooms.getRoomExits(location))
		elif command.nounType == 'action':
			# Eventually add a function to handle this
			# TAFunc.playerAction()
			pass

	# Self explanatory
	if gameOver == True:
		print('Game over. Better luck next time, fatso.')
		quit()
	elif playerVictory == True:
		print('Looks like you won, smart guy.')
		quit()