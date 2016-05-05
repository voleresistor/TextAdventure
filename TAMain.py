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
	print('Welcome to the fart zone, {0}! Muahahaha!'.format(PlayerObj.name))
	
	# The main loop of our game
	while True:
		if gameOver == True or playerVictory == True:
			break
		# Clear some variables that may be modified inside the loop
		roomItems		= TAFunc.getRoomItems(roomID)
		roomObjects		= TAFunc.getRoomObjects(roomID)
		roomKeywords 	= TAFunc.getKeywords(roomItems,roomObjects)
		command			= None
		
		# If player failed to move to a new grid, don't repeat the description
		if roomID != oldRoomID:
			logging.debug('Moved from {0} to {1}'.format(oldRoomID, roomID))
			print(TAFunc.getRoomDescription(roomID))
			oldRoomID = roomID
		else:
			logging.debug('No movement ocurred. Staying in {0}'.format(oldRoomID))

		# Get input from player and create a temporary object out of it
		logging.debug('Getting player command...')
		command = TAFunc.getPlayerCommand(roomKeywords, roomID)
		
		if command['actionType'] == 'move':
			logging.debug('Command actionType = move')
			roomID = TAFunc.playerMoved(command['things'][0], roomID)
		elif command['actionType'] == 'ui':
			logging.debug('Command actionType = ui')
			pass
			TAFunc.uiAction(command['action'], PlayerObj)
		elif command['actionType'] == 'action':
			logging.debug('Command actionType = action')
			pass
			TAFunc.playerAction(command, PlayerObj)
		elif command['actionType'] == 'look':
			logging.debug('Command actionType = look')
			pass
			TAFunc.playerLook(command)
		elif command['actionType'] == 'quit':
			print('Sick of this disgusting house, you decide that the only viable option is suicide.')
			gameOver = True
			logging.debug('GameOver now set to: {0}'.format(gameOver))

	# Self explanatory
	if gameOver == True:
		logging.info('{0} has lost the game. Quitting.'.format(PlayerObj.name))
		print('Game over. Better luck next time, fatso.')
		# MORE CODE: Some other ending sequence. Maybe a try again dialog 
		quit()
	elif playerVictory == True:
		logging.info('{0} has won the game. Quitting.'.format(PlayerObj.name))
		print('Looks like you won, smart guy.')
		# MORE CODE: Some credits or something here?
		quit()