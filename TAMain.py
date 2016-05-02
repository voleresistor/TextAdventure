# **************************************
# A Text Adventure Game
# File: TAMain.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 05/01/2016
# **************************************

# Import our new files
import TAClass
import TAFunc

# Main function to control the whole game
def main():
	# Store our keywords here and pass them into the command parser
	# TODO: Rebuild entire command parser. It sucks.
	envVerbs 		= ['go','move','walk','step','look','fart','lick','take','get','touch','poke','attack','do','search']
	envNouns 		= ['west','north','east','south','door','stairs','room','water','door','yes','turd']
	controlWords	= ['examine','inventory','health','state']
	
	# Initialize some game values
	roomID 			= '005252A'
	gameOver 		= False
	playerVictory 	= False
	oldRoomID		= None
	
	# Initialize our permanent classes
	RoomObj 	= TAClass.TARoomClass()
	ItemObj 	= TAClass.TAItemClass()
	PlayerObj 	= TAClass.TAPlayerClass(input('What be thy name? '))
	
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
			print(RoomObj.getRoomDescription(roomID, ItemObj))

		# Get input from player and create a temporary object out of it
		command = TAFunc.playerCommand(keyword)
		
		# Take action based on data returned in command object
		# TODO: Rewrite entire command function. Differentiating between different action types seems like a waste of time. Differentiation can be based on nounType 
		if command.nounType == 'movement':
			oldRoomID = roomID
			roomID = TAFunc.playerMoved(command, roomID, RoomObj)
		elif command.nounType == 'action':
			if command.noun == keyword:
				PlayerObj.takeItem(itemID, ItemObj)
				print('Picked up {0}'.format(ItemObj.getItemName(itemID)))
			pass

	# Self explanatory
	if gameOver == True:
		print('Game over. Better luck next time, fatso.')
		# MORE CODE: Some other ending sequence. Maybe a try again dialog 
		quit()
	elif playerVictory == True:
		print('Looks like you won, smart guy.')
		# MORE CODE: Some credits or something here?
		quit()