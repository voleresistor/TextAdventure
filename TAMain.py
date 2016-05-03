# **************************************
# A Text Adventure Game
# File: TAMain.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 05/01/2016
# **************************************

# Import logging module
import logging

# Import our new files
import TAClass
import TAFunc

# Main function to control the whole game
def main():
	logging.basicConfig(filename='Logs\TextAdventure.log', filemode='w', level=logging.DEBUG, format='%(levelname)s: %(module)s\%(funcName)s - Line:%(lineno)s - %(asctime)s - %(message)s')
	logging.info('Started')
	
	# Initialize some game values
	roomID 			= '005252'
	logging.debug('Starting roomID = {0}'.format(roomID))
	gameOver 		= False
	playerVictory 	= False
	oldRoomID		= None
	PlayerObj		= TAClass.TAPlayerClass(input('What be thy name? '))
	
	# Welcome to our stupid game
	print('Welcome to the fart zone, {0}! Muahahaha'.format(PlayerObj.name))
	
	# The main loop of our game
	while (gameOver != True) or (playerVictory != True):
		# Clear some variables that may be modified inside the loop
		keyword		= None
		itemID		= None
		command		= None
		
		# If player failed to move to a new grid, don't repeat the description
		if roomID != oldRoomID:
			logging.debug('Moved from {0} to {1}'.format(oldRoomID, roomID))
			print(TAFunc.getRoomDescription(roomID))
		else:
			logging.debug('No movement ocurred. Staying in {0}'.format(oldRoomID))

		# Get input from player and create a temporary object out of it
		logging.info('Getting player command...')
		command = TAFunc.playerCommand(keyword)
		
		# Take action based on data returned in command object
		# TODO: Rewrite entire command function. Differentiating between different action types seems like a waste of time. Differentiation can be based on nounType 
		if command.nounType == 'movement':
			logging.debug('Command type: movement')
			oldRoomID = roomID
			roomID = TAFunc.playerMoved(command, roomID)
		elif command.nounType == 'action':
			logging.debug('command type: action')
			if command.noun == keyword:
				PlayerObj.takeItem(itemID, ItemObj)
				print('Picked up {0}'.format(ItemObj.getItemName(itemID)))
			pass

	# Self explanatory
	if gameOver == True:
		logging.info('{0} has won the game. Quitting.'.format(PlayerObj.name))
		print('Game over. Better luck next time, fatso.')
		# MORE CODE: Some other ending sequence. Maybe a try again dialog 
		quit()
	elif playerVictory == True:
		logging.info('{0} has lost the game. Quitting.'.format(PlayerObj.name))
		print('Looks like you won, smart guy.')
		# MORE CODE: Some credits or something here?
		quit()