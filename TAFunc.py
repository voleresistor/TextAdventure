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
import TAData
import logging
import re

# Update location index
# TODO: Error handling in case line index isn't matched
def playerMoved(direction, room_index):
	# Break out currentIndex
	floorNum 	= room_index[0] + room_index[1]	# Read floor number
	xCoord 		= room_index[2] + room_index[3]	# Read X coordinate
	yCoord 		= room_index[4] + room_index[5]	# Read Y coordinate
	logging.debug('Current room coords: Floor - {0} X - {1} Y - {2}'.format(floorNum, xCoord, yCoord))
	
	canMove		= False
	northExit 	= TAData.gameRooms[room_index]['NORTHEXIT']
	southExit 	= TAData.gameRooms[room_index]['SOUTHEXIT']
	westExit 	= TAData.gameRooms[room_index]['WESTEXIT']
	eastExit 	= TAData.gameRooms[room_index]['EASTEXIT']
	stairsDown	= TAData.gameRooms[room_index]['STAIRSDOWN']
	stairsUp	= TAData.gameRooms[room_index]['STAIRSUP']
	
	# Build new index from currentIndex
	if (direction.lower() == 'west') and (westExit == True):
		xCoord = str(int(xCoord) - 1)
		canMove = True
		
	if (direction.lower() == 'east') and (eastExit == True):
		xCoord = str(int(xCoord) + 1)
		canMove = True
		
	if (direction.lower() == 'north') and (northExit == True):
		yCoord = str(int(yCoord) + 1)
		canMove = True
		
	if (direction.lower() == 'south') and (southExit == True):
		yCoord = str(int(yCoord) - 1)
		canMove = True
		
	if (direction.lower() == 'upstairs') and (stairsUp == True):
		floorNum = str(int(floorNum) + 1)
		canMove = True
	
	if (direction.lower() == 'downstairs') and (stairsDown == True):
		floorNum = str(int(floorNum) + 1)
		canMove = True
	
	if canMove == True:
		logging.debug('New room coords: Floor - {0} X - {1} Y - {2}'.format(floorNum, xCoord, yCoord))
		return floorNum + xCoord + yCoord # Reassemble and return new index
	else:
		print('The way is blocked!')
		return room_index

# Get input from player and parse into a verb-noun pair
# TODO: Don't let a command get out of here without making sure nothing silly is in it.
# ex. Trying to use an item the player doesn't have yet, or on an object not present in the room.
def getPlayerCommand(room_index, roomItems, roomObjects, playerItems):
	command = { 'action':'', 'actionType':'', 'things':[], 'roomID':room_index }
	
	validCommand = False
	logging.debug('Adding items from player inventory: {0}'.format(playerItems))
	playerInput = input('\r\n> ')			# Present prompt to player and get input
	inputWords 	= playerInput.split()		# Separate input into array of words
	logging.debug('Got words from player: {0}'.format(inputWords))
	
	for iWord in inputWords:
		iWord = iWord.lower()
	
	# I find this pretty ugly too. There's got to be a better way
	for aWord in TAData.gameActions:
		logging.debug('Compare {0} to {1} from gameActions for action match'.format(inputWords[0], aWord))
		if inputWords[0] == aWord:
			logging.debug('{0} matches {1}. Appending to action.'.format(inputWords[0],aWord))
			command['action'] = inputWords[0]
			logging.debug('Adding actionType {0} for keyword {1}'.format(TAData.gameActions[inputWords[0]], inputWords[0]))
			command['actionType'] = TAData.gameActions[inputWords[0]]
			inputWords.remove(inputWords[0])
			break
				
	for iWord in inputWords:
		for pItem in playerItems:
			for kWord in TAData.gameItems[pItem]['KEYWORDS']:
				logging.debug('Compare {0} to {1} from playerItems for item inventory match'.format(iWord, kWord))
				if iWord == kWord:
					logging.debug('{0} matches {1}. Appending to things.'.format(iWord,kWord))
					command['things'].append(pItem)
					continue
					
		for item in roomItems:
			for kWord in TAData.gameItems[item]['KEYWORDS']:
				logging.debug('Compare {0} to {1} from gameItems for item match'.format(iWord, kWord))
				if iWord == kWord and TAData.gameItems[item]['PRESENT']:
					logging.debug('{0} matches {1}. Appending to things.'.format(iWord,kWord))
					command['things'].append(item)
					break
					
		for thing in roomObjects:
			for kWord in TAData.gameObjects[thing]['KEYWORDS']:
				logging.debug('Compare {0} to {1} from gameObjects for object match'.format(iWord, kWord))
				if iWord == kWord:
					logging.debug('{0} matches {1}. Appending to things.'.format(iWord,kWord))
					command['things'].append(thing)
					break
					
		for direction in TAData.gameMoves:
			logging.debug('Compare {0} to {1} from gameMoves for direction match'.format(iWord, direction))
			if iWord == direction:
				logging.debug('{0} matches {1}. Appending to things.'.format(iWord,direction))
				command['things'].append(iWord)
				break
	
	logging.debug('Command Action: {0}'.format(command['action']))
	logging.debug('Command Type: {0}'.format(command['actionType']))
	logging.debug('Command Things: {0}'.format(command['things']))
	
	if not command['actionType'] == 'look' and not command['actionType'] == 'ui' and not command['actionType'] == 'quit':
		if command['action'] and command['things'] and command['actionType']:
			return command
		else:
			return False
	else:
		return command
	
# Return description of room identified by room_index.
def getRoomDescription(room_index, detail=False):
	itemRoomText = []
	
	if detail == True:
		roomDesc = TAData.gameRooms[room_index]['LONGDESC']
	else:
		roomDesc = TAData.gameRooms[room_index]['SHORTDESC']
		
	if TAData.gameRooms[room_index]['OBJECTS']:
		for objIndex in TAData.gameRooms[room_index]['OBJECTS']:
			logging.debug('Objects in room {0}: {1}'.format(TAData.gameRooms[room_index]['ROOMID'], TAData.gameRooms[room_index]['OBJECTS']))
			if detail == False:
				logging.debug('{0} is present. Adding ROOMTEXT'.format(TAData.gameObjects[objIndex]['OBJECTNAME']))
				itemRoomText.append(TAData.gameObjects[objIndex]['ROOMTEXT'])
			else:
				logging.debug('{0} is present. Adding ROOMEXAMINE'.format(TAData.gameObjects[objIndex]['OBJECTNAME']))
				itemRoomText.append(TAData.gameObjects[objIndex]['ROOMEXAMINE'])
		
	if TAData.gameRooms[room_index]['ITEMS']:
		for itemIndex in TAData.gameRooms[room_index]['ITEMS']:
			logging.debug('Items in room {0}: {1}'.format(TAData.gameRooms[room_index]['ROOMID'], TAData.gameRooms[room_index]['ITEMS']))
			if TAData.gameItems[itemIndex]['PRESENT']:
				if detail == False:
					logging.debug('{0} is present. Adding ROOMTEXT'.format(TAData.gameItems[itemIndex]['ITEMNAME']))
					itemRoomText.append(TAData.gameItems[itemIndex]['ROOMTEXT'])
				else:
					logging.debug('{0} is present. Adding ROOMEXAMINE'.format(TAData.gameItems[itemIndex]['ITEMNAME']))
					itemRoomText.append(TAData.gameItems[itemIndex]['ROOMEXAMINE'])
			else:
				logging.debug('{0} is not present'.format(TAData.gameItems[itemIndex]['ITEMNAME']))

	if itemRoomText:
		for description in itemRoomText:
			roomDesc += ' '
			roomDesc += description
	logging.debug('Full description for room {0}: {1}'.format(room_index, roomDesc))
	return (roomDesc)
	
def getRoomItems(roomID):
	items = []
	for item in TAData.gameRooms[roomID]['ITEMS']:
		logging.debug('Adding - {0} - to items for room {1}'.format(item,roomID))
		items.append(item)
	
	return items
	
def getRoomObjects(roomID):
	objects = []
	for thing in TAData.gameRooms[roomID]['OBJECTS']:
		logging.debug('Adding - {0} - to objects for room {1}'.format(thing,roomID))
		objects.append(thing)
		
	return objects
	
def uiAction(action, playerObj):
	if action == 'health':
		logging.debug('Player health: {0}'.format(playerObj.health))
		return ('Player health: \r\n\t{0}'.format(playerObj.health))
		
	if action == 'state':
		logging.debug('Player state: {0}'.format(playerObj.state))
		return ('Player state: \r\n\t{0}'.format(playerObj.state))
		
	if action == 'inventory':
		inventory = 'Digging in your pockets, you find:'
		logging.debug('Items in inventory: {0}'.format(playerObj.item_inv))
		if playerObj.item_inv:
			for item in playerObj.item_inv:
				inventory += '\r\n\t'
				inventory += ('\t{0}'.format(TAData.gameItems[item]['ITEMNAME']))
		else:
			inventory += '\r\n\tNothing!'
		return inventory
			
def playerLook(command):
	if not command['things']:
		logging.debug('No item or object specified. Printing long room description.')
		return getRoomDescription(command['roomID'], detail=True)
	else:
		for thing in command['things']:
			if re.match('[A-Z]{2}', thing):
				return TAData.gameObjects[thing]['OBJECTDESC']
			elif re.match('[0-9]{3}', thing):
				return TAData.gameItems[thing]['ITEMDESC']
			else:
				return 'What on Earth are you looking at?'

def playerAction(command, playerObj):
	pass

def playerQuit():
	confirm = input('Are you sure you\'re tired of skulking about in here?\r\n> ')
	
	if confirm == 'yes':
		logging.debug('Player typed the magic word: yes')
		print('Sick of this disgusting house, you decide that the only viable option is suicide. The end comes slowly as you choke yourself to death with a long, greasy turd.')
		return True
	else:
		logging.debug('Player came to their senses and decided to try some more.')
		print('You harden your resolve and pledge to trudge though the filth a little longer...')
		return False
		
def playerGet(item, playerObj):
	if TAData.gameItems[item]['PRESENT']:
		playerObj.item_inv.append(item)
		TAData.gameItems[item]['PRESENT'] = False
		return 'Picked up {0}.'.format(TAData.gameItems[item]['ITEMNAME'])
	else:
		return 'You look all around, but don\'t see a {0} anywhere.'.format(TAData.gameItems[item]['ITEMNAME'])
		
def playerUse(useItem, useOn, roomID, playerInv):
	playerHasItem	= False
	targetInRoom	= False
	hasReward		= False
	rewardItem		= False
	openPortal		= False
	portalDirection = False
	logging.debug('useItem: {0}'.format(useItem))
	logging.debug('useOn: {0}'.format(useOn))
	
	# Make sure player has the item
	for item in playerInv:
		if useItem == item:
			logging.debug('Player has {0} in inventory.'.format(TAData.gameItems[item]['ITEMNAME']))
			playerHasItem = True
			logging.debug('playerHasItem: {0}'.format(playerHasItem))
			
	# Make sure player is in the right room
	if TAData.gameObjects[useOn]['ROOMID'] == roomID:
		logging.debug('Player is in the correct room.')
		targetInRoom = True
		logging.debug('targetInRoom is {0}'.format(targetInRoom))
	
	if playerHasItem and targetInRoom:
		logging.debug('Activating object {0}.'.format(TAData.gameObjects[useOn]['OBJECTNAME']))
		return ('You did a thing with that thing.')
	elif playerHasItem and not targetInRoom:
		logging.debug('Object {0} is not in current room.'.format(TAData.gameObjects[useOn]['OBJECTNAME']))
		return ('That\'s not in this room.')
	elif not playerHasItem and targetInRoom:
		logging.debug('Item {0} is not in player inventory.'.format(TAData.gameItems[useItem]['ITEMNAME']))
		return ('You can\'t use and item you don\'t have.')
	else:
		return ('I dunno what just happened.')