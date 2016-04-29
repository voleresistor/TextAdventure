import csv
RoomsIndexFile = 'levelFile.csv'
testIndex = '005050A'

class RoomFile:
    def __init__(self, roomFile):
        with open(roomFile, 'rb') as roomCSV:
            roomObj = csv.reader(roomCSV, delimiter=',')
            self.roomIndex  = []
            self.roomDesc   = []
            self.roomExit   = []
            self.roomStair  = []
        
            for row in roomObj:
                self.roomIndex.append(row[0])
                self.roomDesc.append(row[1])
                self.roomExit.append(row[2])
                self.roomStair.append(row[3])
            
    def getDesc(self,index):
        roomIndex = self.roomIndex.index(index)
        description = self.roomDesc[roomIndex]
        print(description)

rooms = RoomFile(RoomsIndexFile)
rooms.getDesc(testIndex)