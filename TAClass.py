# **************************************
# A Text Adventure Game
# File: TAClass.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 04/30/2016
# **************************************

from csv import reader # Just to read CSVs into memory

# Load data from rooms file into memory and provide functions to ease accessing that data
class TARoomClass:
    def __init__(self, roomFile):
        with open(roomFile, 'rt') as roomCSV:
            roomObj = reader(roomCSV, delimiter=',')
            self.roomIndex  = []
            self.roomDesc   = []
            self.roomExit   = []
            self.roomStair  = []
            self.hasItem    = []

            for row in roomObj:
                self.roomIndex.append(row[0])
                self.roomDesc.append(row[1])
                self.roomExit.append(row[2])
                self.roomStair.append(row[3])
                self.hasItem.append(row[4])

    def getRoomDescription(self,index,itemObj):
        roomIndex   = self.roomIndex.index(index)
        roomDesc    = self.roomDesc[roomIndex]
        
        if self.hasItem[roomIndex] == 'Y':
            itemDesc = itemObj.getRoomText(index)
            print('{0} {1}'.format(roomDesc, itemDesc))
        else:
            print (roomDesc)

    def getRoomExits(self,index):
        roomIndex = self.roomIndex.index(index)
        return self.roomExit[roomIndex]
        
# Load data from items file into memory and provide functions for interacting with these items
class TAItemClass:
    def __init__(self,itemFile):
        with open(itemFile, 'rt') as itemCSV:
            itemObj = reader(itemCSV, delimiter=',')
            self.roomIndex  = []
            self.itemIndex  = []
            self.itemName   = []
            self.roomText   = []
            self.itemDesc   = []
            self.oneUse     = []
            self.keyword    = []
            self.used       = []

            for row in itemObj:
                self.roomIndex.append(row[0])
                self.itemIndex.append(row[1])
                self.itemName.append(row[2])
                self.roomText.append(row[3])
                self.itemDesc.append(row[4])
                self.oneUse.append(row[5])
                self.keyword.append(row[6])
                self.used.append('N')
                
    def getItemDescription(self,index):
        itemIndex = self.roomIndex.index(index)
        return self.itemDesc[itemIndex]
        
    def getItemName(self,index):
        itemIndex = self.roomIndex.index(index)
        return self.itemName[itemIndex]
        
    def getRoomText(self,index):
        itemIndex = self.roomIndex.index(index)
        return self.roomText[itemIndex]
        
    def useItem(self,index):
        itemIndex = self.roomIndex.index(index)
        if self.oneUse[itemIndex] == 'Y':
            self.used[itemIndex] = 'Y'
            TAPlayerClass.removeItem(index)
            if self.used[itemIndex] == 'Y':
                return True
            else:
                return False
        else:
            return True
            
    def getKeyword(self,index):
        for room in self.roomIndex:
            if room == index:
                itemIndex = self.roomIndex.index(index)
                return self.keyword[itemIndex]
        return None
        

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
        
    def takeItem(self, index):
        self.item_inv.append(index)
        itemIndex = self.item_inv.index(index)
        
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