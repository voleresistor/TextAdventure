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
        
# Store data about the player character
class TAPlayerClass:
    def __init__(self, name):
        self.item_inv       = ['005']
        self.used_items     = []
        self.changed_rooms  = []
        self.health         = 10
        self.state          = 'Alive'
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