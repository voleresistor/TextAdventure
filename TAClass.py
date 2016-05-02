# **************************************
# A Text Adventure Game
# File: TAClass.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 05/01/2016
# **************************************

# Load the game data
import TAData

# Store and manipulate game data 
class TARoomClass:
    def __init__(self):
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

        gameRooms = TAData.getGameRooms()
        for room in gameRooms:
            self.roomIndex.append(gameRooms[room]['ROOMID'])
            self.roomName.append(gameRooms[room]['ROOMNAME'])
            self.shortDesc.append(gameRooms[room]['SHORTDESC'])
            self.longDesc.append(gameRooms[room]['LONGDESC'])
            self.northExit.append(gameRooms[room]['NORTHEXIT'])
            self.southExit.append(gameRooms[room]['SOUTHEXIT'])
            self.westExit.append(gameRooms[room]['WESTEXIT'])
            self.eastExit.append(gameRooms[room]['EASTEXIT'])
            self.stairsUp.append(gameRooms[room]['STAIRSUP'])
            self.stairsDown.append(gameRooms[room]['STAIRSDOWN'])
            self.items.append(gameRooms[room]['ITEMS'])
            
        gameRooms = None

    # Return description of room identified by room_index. Supplemented by possible item_index from itemObj
    def getRoomDescription(self,room_index,itemObj):
        roomIndex   = self.roomIndex.index(room_index)
        roomDesc    = self.shortDesc[roomIndex]
        itemDesc    = None
        
        if self.items[roomIndex] == True:
            for itemIndex in self.items[roomIndex]:
                itemPresent = itemObj.getItemPresent(itemIndex)
            if itemPresent == True:
                itemDesc = itemObj.getRoomText(itemIndex)

        if itemDesc:
            roomDesc += ' '
            roomDesc += itemDesc
        return (roomDesc)

    # Is there and exit to the North? (True/False)
    def getNorthExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        return self.northExit[roomIndex]
        
    # Is there and exit to the South? (True/False)
    def getSouthExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        return self.southExit[roomIndex]
        
    # Is there and exit to the West? (True/False)
    def getWestExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
        return self.westExit[roomIndex]
        
    # Is there and exit to the East? (True/False)
    def getEastExit(self,room_index):
        roomIndex = self.roomIndex.index(room_index)
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

        gameItems = TAData.getGameItems()
        for room in gameItems:
            self.roomIndex.append(gameItems[room]['ROOMID'])
            self.itemIndex.append(gameItems[room]['ITEMID'])
            self.itemName.append(gameItems[room]['ITEMNAME'])
            self.roomText.append(gameItems[room]['ROOMTEXT'])
            self.itemDesc.append(gameItems[room]['ITEMDESC'])
            self.oneUse.append(gameItems[room]['ONEUSE'])
            self.keywords.append(gameItems[room]['KEYWORDS'])
            self.present.append(True)
            
        gameItems = None
    
    # Return Item ID from a room index. This is the only time an item should be referred to by room index
    # TODO: Implement array of items so multiple items can be present in a single room
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
                return self.keywords[itemIndex]
        return None
    
    # Get description of item identified by item_index
    def getItemDescription(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        return self.itemDesc[itemIndex]
    
    # Get name of item identified by item_index
    def getItemName(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        return self.itemName[itemIndex]
    
    # Return presence state of item identified by item_index
    def getItemPresent(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        return self.present[itemIndex]
    
    # Return room text of item identified by item_index
    def getRoomText(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        return self.roomText[itemIndex]
    
    # If player takes item identified by item_index and it's a one time pickup, set self.present attribute to False for the item
    # TODO: 
    def takeItem(self,item_index):
        itemIndex = self.itemIndex.index(item_index)
        if self.oneUse[itemIndex] == True:
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