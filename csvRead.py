import csv

with open('levelFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    indexes = []
    descriptions = []
    for row in readCSV:
        index = row[0]
        description = row[1]
        
        indexes.append(index)
        descriptions.append(description)
        
    print(indexes)
    
roomID = input('Get description for what room index: ')
roomIndex = indexes.index(roomID)
roomDesc = descriptions[roomIndex]

print('Description for room index: ', roomID, '\r\n', roomDesc)