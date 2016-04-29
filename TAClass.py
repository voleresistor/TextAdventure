# **************************************
# A Text Adventure Game
# File: TAClass.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/29/2016
# Last Edit: 04/29/2016
# **************************************

from csv import reader # Just to read CSVs into memory

# Load data from rooms file into memory and provide functions to ease accessing that data
class RoomsFile:
    def __init__(self, roomFile):
        with open(roomFile, 'rt') as roomCSV:
            roomObj = reader(roomCSV, delimiter=',')
            self.roomIndex  = []
            self.roomDesc   = []
            self.roomExit   = []
            self.roomStair  = []

            for row in roomObj:
                self.roomIndex.append(row[0])
                self.roomDesc.append(row[1])
                self.roomExit.append(row[2])
                self.roomStair.append(row[3])

    def getRoomDescription(self,index):
        roomIndex = self.roomIndex.index(index)
        description = self.roomDesc[roomIndex]
        print(description)

    def getRoomExits(self,index):
        roomIndex = self.roomIndex.index(index)
        return self.roomExit[roomIndex]

# PlayerCommand class stores information about the last successfully parsed command
class PlayerCommandObj:
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