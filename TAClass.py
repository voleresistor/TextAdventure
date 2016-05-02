# **************************************
# A Text Adventure Game
# File: TAClass.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 05/01/2016
# **************************************

# Load the game data and logging
import logging
import TAData

# Store and manipulate game data 
class TARoomClass:
    def __init__(self):
        logging.debug('Creating new rooms object.')
        self.roomName   = []
        self.roomIndex  = []
        self.shortDesc  = []
        self.longDesc   = []
        self.northExit  = []
        self.southExit  = []
        self.westExit   = []
        self.eastExit   = []
        self.stairsUp   = []
        self.stairsDown = []
        self.items      = []

        logging.debug('Loading gameRooms data...')
        gameRooms = TAData.getGameRooms()
        for room in gameRooms:
            logging.debug('Adding {0} to TARoomClass.roomIndex'.format(gameRooms[room]['ROOMID']))
            self.roomIndex.append(gameRooms[room]['ROOMID'])
            logging.debug('Adding {0} to TARoomClass.roomName'.format(gameRooms[room]['ROOMNAME']))
            self.roomName.append(gameRooms[room]['ROOMNAME'])
            logging.debug('Adding {0} to TARoomClass.shortDesc'.format(gameRooms[room]['SHORTDESC']))
            self.shortDesc.append(gameRooms[room]['SHORTDESC'])
            logging.debug('Adding {0} to TARoomClass.longDesc'.format(gameRooms[room]['LONGDESC']))
            self.longDesc.append(gameRooms[room]['LONGDESC'])
            logging.debug('Adding {0} to TARoomClass.northExit'.format(gameRooms[room]['NORTHEXIT']))
            self.northExit.append(gameRooms[room]['NORTHEXIT'])
            logging.debug('Adding {0} to TARoomClass.southExit'.format(gameRooms[room]['SOUTHEXIT']))
            self.southExit.append(gameRooms[room]['SOUTHEXIT'])
            logging.debug('Adding {0} to TARoomClass.westExit'.format(gameRooms[room]['WESTEXIT']))
            self.westExit.append(gameRooms[room]['WESTEXIT'])
            logging.debug('Adding {0} to TARoomClass.eastExit'.format(gameRooms[room]['EASTEXIT']))
            self.eastExit.append(gameRooms[room]['EASTEXIT'])
            logging.debug('Adding {0} to TARoomClass.stairsUp'.format(gameRooms[room]['STAIRSUP']))
            self.stairsUp.append(gameRooms[room]['STAIRSUP'])
            logging.debug('Adding {0} to TARoomClass.stairsDown'.format(gameRooms[room]['STAIRSDOWN']))
            self.stairsDown.append(gameRooms[room]['STAIRSDOWN'])
            logging.debug('Adding {0} to TARoomClass.items'.format(gameRooms[room]['ITEMS']))
            self.items.append(gameRooms[room]['ITEMS'])
            
        logging.debug('Clearing gameRooms variable...')
        gameRooms = None

    # Return description of room identified by room_index. Supplemented by possible item_index from itemObj
    def getRoomDescription(self,room_index,itemObj):
        roomIndex       = self.roomIndex.index(room_index)
        roomDesc        = self.shortDesc[roomIndex]
        itemRoomText    = []
        
        if self.items[roomIndex]:
            for itemIndex in self.items[roomIndex]:
                logging.debug('Items in room {0}: {1}'.format(self.roomIndex[roomIndex], itemIndex))
                itemRoomText.append(itemObj.getRoomText(itemIndex))

        if itemRoomText:
            for description in itemRoomText:
                roomDesc += ' '
                roomDesc += description
        logging.debug('Full description for room {0}: {1}'.format(self.roomIndex[roomIndex], roomDesc))
        return (roomDesc)

    # Is there and exit to the North? (True/False)
    def getNorthExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        logging.debug('Exit room {0} to North is {1}'.format(self.roomIndex[roomIndex], self.northExit[roomIndex]))
        return self.northExit[roomIndex]
        
    # Is there and exit to the South? (True/False)
    def getSouthExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        logging.debug('Exit room {0} to South is {1}'.format(self.roomIndex[roomIndex], self.southExit[roomIndex]))
        return self.southExit[roomIndex]
        
    # Is there and exit to the West? (True/False)
    def getWestExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        logging.debug('Exit room {0} to West is {1}'.format(self.roomIndex[roomIndex], self.westExit[roomIndex]))
        return self.westExit[roomIndex]
        
    # Is there and exit to the East? (True/False)
    def getEastExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        logging.debug('Exit room {0} to East is {1}'.format(self.roomIndex[roomIndex], self.eastExit[roomIndex]))
        return self.eastExit[roomIndex]
        
# Load data from items file into memory and provide functions for interacting with these items
class TAItemClass:
    def __init__(self):
        self.roomIndex  = []
        self.itemIndex  = []
        self.itemName   = []
        self.roomText   = []
        self.itemDesc   = []
        self.oneUse     = []
        self.keywords   = []
        self.present    = []

        logging.debug('Loading gameItems data...')
        gameItems = TAData.getGameItems()
        for room in gameItems:
            logging.debug('Adding {0} to TAItemClass.roomIndex'.format(gameItems[room]['ROOMID']))
            self.roomIndex.append(gameItems[room]['ROOMID'])
            logging.debug('Adding {0} to TAItemClass.itemIndex'.format(gameItems[room]['ITEMID']))
            self.itemIndex.append(gameItems[room]['ITEMID'])
            logging.debug('Adding {0} to TAItemClass.itemName'.format(gameItems[room]['ITEMNAME']))
            self.itemName.append(gameItems[room]['ITEMNAME'])
            logging.debug('Adding {0} to TAItemClass.roomText'.format(gameItems[room]['ROOMTEXT']))
            self.roomText.append(gameItems[room]['ROOMTEXT'])
            logging.debug('Adding {0} to TAItemClass.itemDesc'.format(gameItems[room]['ITEMDESC']))
            self.itemDesc.append(gameItems[room]['ITEMDESC'])
            logging.debug('Adding {0} to TAItemClass.oneUse'.format(gameItems[room]['ONEUSE']))
            self.oneUse.append(gameItems[room]['ONEUSE'])
            logging.debug('Adding {0} to TAItemClass.keywords'.format(gameItems[room]['KEYWORDS']))
            self.keywords.append(gameItems[room]['KEYWORDS'])
            logging.debug('Adding {0} to TAItemClass.present'.format(True))
            self.present.append(True)

        logging.debug('Clearing gameItems variable...')
        gameItems = None
    
    # Return Item ID from a room index. This is the only time an item should be referred to by room index
    # TODO: I think this will be going away.
    def getItemIndex(self,room_index):
        for room in self.roomIndex:
            if room == room_index:
                roomIndex = self.roomIndex.index(room_index)
                return self.itemIndex[roomIndex]
        return None
    
    # Return keyword for item identified by item_index
    def getKeyword(self,item_index):
        for item in self.itemIndex:
            if item == item_index:
                itemIndex = self.itemIndex.index(item_index)
                logging.debug('Got keywords for item {0}: {1}'.format(self.itemIndex[itemIndex], self.keywords[itemIndex]))
                return self.keywords[itemIndex]
        return None
    
    # Get description of item identified by item_index
    def getItemDescription(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        logging.debug('Got itemIndex for item {0}: {1}'.format(self.itemIndex[itemIndex], self.itemDesc[itemIndex]))
        return self.itemDesc[itemIndex]
    
    # Get name of item identified by item_index
    def getItemName(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        logging.debug('Got itemName for item {0}: {1}'.format(self.itemIndex[itemIndex], self.itemName[itemIndex]))
        return self.itemName[itemIndex]
    
    # Return presence state of item identified by item_index
    def getItemPresent(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        logging.debug('Got present for item {0}: {1}'.format(self.itemIndex[itemIndex], self.present[itemIndex]))
        return self.present[itemIndex]
    
    # Return room text of item identified by item_index
    def getRoomText(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        logging.debug('Got roomText for item {0}: {1}'.format(self.itemIndex[itemIndex], self.roomText[itemIndex]))
        return self.roomText[itemIndex]
    
    # If player takes item identified by item_index and it's a one time pickup, set self.present attribute to False for the item
    # TODO: What is happening here?
    def takeItem(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        if self.oneUse[itemIndex] == True:
            logging.debug('Setting item {0} presence to: {1}'.format(self.itemIndex[itemIndex], False))
            self.present[itemIndex] = False

# PlayerCommand class stores information about the last successfully parsed command
class TACommandClass:
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
        
# Store data about the player character
class TAPlayerClass:
    def __init__(self, name):
        self.item_inv       = []
        self.used_items     = []
        self.changed_rooms  = []
        self.health         = 10
        self.state          = None
        self.name           = name
        
    def takeItem(self, index, itemObj):
        self.item_inv.append(index)
        itemIndex = self.item_inv.index(index)
        itemObj.takeItem(index)
        
        if self.item_inv[itemIndex]:
            return True
        else:
            return False
        
    def removeItem(self, index):
        self.item_inv.remove(index)
        self.used_items.append(index)
        invIndex = self.item_inv.index(index)
        useIndex = self.used_items.index(index) 
        
        if (self.item_inv[invIndex] != True) and (self.used_items[useIndex]):
            return True
        else:
            return False
    
    def listItemsHeld(self):
        print('List of held item indexes: ')
        for item in self.item_inv:
            print(item)
            
    def listItemsUsed(self):
        print('List of items that have been used: ')
        for item in self.used_items:
            print(item)