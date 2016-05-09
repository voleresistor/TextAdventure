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
	logging.basicConfig(
		filename='Logs\TextAdventure.log',
		filemode='w',
		level=logging.DEBUG, 
		format='%(levelname)s: %(module)s\%(funcName)s - Line:%(lineno)s - %(asctime)s - %(message)s'
	)
	logging.info('Started')
	
	# Initialize some game values
	roomID 			= '005252'
	gameOver 		= False
	playerVictory 	= False
	oldRoomID		= None
	PlayerObj		= TAClass.TAPlayerClass(input('What be thy name? '))
	logging.debug('Starting roomID = {0}'.format(roomID))
	
	# Welcome to our stupid game
	print('Welcome to the fart zone, {0}! Muahahaha!'.format(PlayerObj.name))
	
	# The main loop of our game
	while True:
		if gameOver == True or playerVictory == True:
			break
			
		# Set up some variables for this iteration of the loop
		roomItems		= TAFunc.getRoomItems(roomID)
		roomObjects		= TAFunc.getRoomObjects(roomID)
		command			= False
		
		# If player failed to move to a new grid, don't repeat the description
		if roomID != oldRoomID:
			logging.debug('Moved from {0} to {1}'.format(oldRoomID, roomID))
			print(TAFunc.getRoomDescription(roomID))
			oldRoomID = roomID
		else:
			logging.debug('No movement ocurred. Staying in {0}'.format(oldRoomID))

		# Get input from player
		while not command:
			logging.debug('Getting player command...')
			command = TAFunc.getPlayerCommand(roomID, roomItems, roomObjects, PlayerObj.item_inv)
			
			if not command:
				logging.debug('Got bad command. Trying again.')
				print ('I don\'t know how to do that.')
		
		# Holy shit does this burn my eyes. Python could really use a switch. Any better ways to handle this?
		if command['actionType'] == 'move':
			logging.debug('Command actionType = move')
			roomID = TAFunc.playerMoved(command['things'][0], roomID)
			
		if command['actionType'] == 'ui':
			logging.debug('Command actionType = ui')
			print(TAFunc.uiAction(command['action'], PlayerObj))
			
		#if command['actionType'] == 'action':
		#	logging.debug('Command actionType = action')
		#	pass
		#	TAFunc.playerAction(command, PlayerObj)
			
		if command['actionType'] == 'get':
			logging.debug('Command actionType = get')
			print(TAFunc.playerGet(command['things'][0], PlayerObj))
			
		if command['actionType'] == 'use':
			logging.debug('Command actionType = use')
			print(TAFunc.playerUse(command['things'][0], command['things'][1], roomID, PlayerObj.item_inv))
			
		if command['actionType'] == 'attack':
			logging.debug('Command actionType = attack')
			pass
			TAFunc.playerAttack()
			
		if command['actionType'] == 'look':
			logging.debug('Command actionType = look')
			print(TAFunc.playerLook(command))
			
		if command['actionType'] == 'quit':
			logging.debug('Player thinks they can quit MY fucking game?')
			gameOver = TAFunc.playerQuit()
			logging.debug('GameOver now set to: {0}'.format(gameOver))

	# Self explanatory
	if gameOver == True:
		logging.info('{0} has lost the game. Quitting.'.format(PlayerObj.name))
		print('Game over. Better luck next time, fatso.')
		# TODO: Some other ending sequence. Maybe a try again dialog 
		quit()
	elif playerVictory == True:
		logging.info('{0} has won the game. Quitting.'.format(PlayerObj.name))
		print('Looks like you won, smart guy.')
		# TODO: Some credits or something here?
		quit()