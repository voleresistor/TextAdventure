# **************************************
# A Text Adventure Game
# File: TAMain.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 04/30/2016
# **************************************

# Import our new files
import TAClass
import TAFunc

# Main function to control the whole game
def main():
	location 		= '005252A'			# Set initial location at start of game
	gameOver 		= False 			# Game is NOT over just yet
	playerVictory 	= False 			# Player can't win this easily
	oldLocation 	= None				# Store old location so we can avoid repeating room descriptions
	itemFile		= 'items.csv'		# Name of item file
	roomFile		= 'rooms.csv'		# Name of room file
	keyword			= None
	
	rooms 	= TAClass.TARoomClass(roomFile)	# Create a new object containing the contents of the room file
	player 	= TAClass.TAPlayerClass(input('What be thy name? ')) # Name your stupid character
	print('Welcome to the fart zone, {0}! Muahahaha'.format(player.name))
	items 	= TAClass.TAItemClass(itemFile)	# Create a new object containing the contents of the items file
	
	# The main loop of our game
	while (gameOver != True) or (playerVictory != True):
		# If player failed to move to a new grid, don't repeat the description
		if location != oldLocation:
			rooms.getRoomDescription(location, items)		# Get area description based on area index
			keyword = items.getKeyword(location)
		command = TAFunc.playerCommand(keyword)				# Get input from player and create object out of it
		#command.describeSelf()
		
		if command.nounType == 'movement':
			oldLocation = location
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