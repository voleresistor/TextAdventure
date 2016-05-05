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
from TAClass import TACommandClass
import TAData
import logging

# Update location index
# TODO: Error handling in case line index isn't matched
def playerMoved(direction, room_index):
	# Break out currentIndex
	floorNum 	= room_index[0] + room_index[1]	# Read floor number
	xCoord 		= room_index[2] + room_index[3]	# Read X coordinate
	yCoord 		= room_index[4] + room_index[5]	# Read Y coordinate
	logging.debug('Current room coords: Floor - {0} X - {1} Y - {2}'.format(floorNum, xCoord, yCoord))
	
	canMove		= True
	northExit 	= TAData.gameRooms[room_index]['NORTHEXIT']
	southExit 	= TAData.gameRooms[room_index]['SOUTHEXIT']
	westExit 	= TAData.gameRooms[room_index]['WESTEXIT']
	eastExit 	= TAData.gameRooms[room_index]['EASTEXIT']
	stairsDown	= TAData.gameRooms[room_index]['STAIRSDOWN']
	stairsUp	= TAData.gameRooms[room_index]['STAIRSUP']
	
	# Build new index from currentIndex
	if (direction.lower() == 'west') and (westExit == True):
		xCoord = str(int(xCoord) - 1)
	elif (direction.lower() == 'west') and (westExit == False):
		canMove = False
		
	if (direction.lower() == 'east') and (eastExit == True):
		xCoord = str(int(xCoord) + 1)
	elif (direction.lower() == 'east') and (eastExit == False):
		canMove = False
		
	if (direction.lower() == 'north') and (northExit == True):
		yCoord = str(int(yCoord) + 1)
	elif (direction.lower() == 'north') and (northExit == False):
		canMove = False
		
	if (direction.lower() == 'south') and (southExit == True):
		yCoord = str(int(yCoord) - 1)
	elif (direction.lower() == 'south') and (southExit == False):
		canMove = False
		
	if ((direction.lower() == 'up') or (direction.lower() == 'upstairs')) and (stairsUp == True):
		floorNum = str(int(floorNum) + 1)
	elif ((direction.lower() == 'up') or (direction.lower() == 'upstairs')) and (stairsUp == False):
		canMove = False
	
	if ((direction.lower() == 'down') or (direction.lower() == 'downstairs')) and (stairsDown == True):
		floorNum = str(int(floorNum) + 1)
	elif ((direction.lower() == 'down') or (direction.lower() == 'downstairs')) and (stairsDown == False):
		canMove = False
	
	if canMove == True:
		logging.debug('New room coords: Floor - {0} X - {1} Y - {2}'.format(floorNum, xCoord, yCoord))
		return floorNum + xCoord + yCoord # Reassemble and return new index
	else:
		print('The way is blocked!')
		return room_index

# Get input from player and parse into a verb-noun pair
def getPlayerCommand(keywords, room_index):
	command = { 'action':'', 'actionType':'', 'things':[], 'thingType':[], 'roomID':room_index }
	keywords += TAData.gameMoves
	
	playerInput = input('\r\n> ')			# Present prompt to player and get input
	inputWords 	= playerInput.split()		# Separate input into array of words
	
	for iWord in inputWords:
		iWord = iWord.lower()
		for aWord in TAData.gameActions:
			if iWord == aWord:
				logging.debug('{0} matches {1}. Adding to action.'.format(iWord,aWord))
				command['action'] = iWord
				logging.debug('Adding actionType {0} for keyword {1}'.format(TAData.gameActions[iWord], iWord))
				command['actionType'] = TAData.gameActions[iWord]
		for kWord in keywords:
			if iWord == kWord:
				logging.debug('{0} matches {1}. Adding to things.'.format(iWord,kWord))
				command['things'].append(iWord)
	
	logging.debug('Command Action: {0}'.format(command['action']))
	logging.debug('Command type: {0}'.format(command['actionType']))
	logging.debug('Command Things: {0}'.format(command['things']))
	return command					 	# Return new object containing command decryption
	
# Return description of room identified by room_index. Supplemented by possible item_index from itemObj
def getRoomDescription(room_index, detail=False):
	itemRoomText = []
	
	if detail == True:
		roomDesc = TAData.gameRooms[room_index]['LONGDESC']
	else:
		roomDesc = TAData.gameRooms[room_index]['SHORTDESC']
		
	if TAData.gameRooms[room_index]['ITEMS']:
		for itemIndex in TAData.gameRooms[room_index]['ITEMS']:
			logging.debug('Items in room {0}: {1}'.format(TAData.gameRooms[room_index]['ROOMID'], TAData.gameRooms[room_index]['ITEMS']))
			itemRoomText.append(TAData.gameItems[itemIndex]['ROOMTEXT'])

	if itemRoomText:
		for description in itemRoomText:
			roomDesc += ' '
			roomDesc += description
	logging.debug('Full description for room {0}: {1}'.format(room_index, roomDesc))
	return (roomDesc)
	
def getKeywords(items,objects):
	keywords = []
	for item in items:
		logging.debug('Getting keywords for item {0}'.format(item))
		for word in TAData.gameItems[item]['KEYWORDS']:
			logging.debug('Adding keyword {0} for item {1}'.format(word,item))
			keywords.append(word)
	for thing in objects:
		logging.debug('Getting keywords for object {0}'.format(thing))
		for word in TAData.gameObjects[thing]['KEYWORDS']:
			logging.debug('Adding keyword {0} for object {1}'.format(word,thing))
			keywords.append(word)
				
	return keywords
	
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
		print ('Player health: \r\n\t{0}'.format(playerObj.health))
		
	if action == 'state':
		logging.debug('Player state: {0}'.format(playerObj.state))
		print ('Player state: \r\n\t{0}'.format(playerObj.state))
		
	if action == 'inventory':
		print ('Digging in your pockets, you find:')
		logging.debug('Items in inventory: {0}'.format(playerObj.item_inv))
		for item in playerObj.item_inv:
			print ('\t{0}'.format(TAData.gameItems[item]['ITEMNAME']))
			
def playerLook(command):
	if not command['things']:
		logging.debug('No item or object specified. Printing long room description.')
		print(getRoomDescription(command['roomID'], detail=True))
	else:
		pass

def playerAction(command, playerObj):
	pass

