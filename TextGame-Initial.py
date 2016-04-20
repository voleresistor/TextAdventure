f = open('levels.txt', 'r')

def getAreaText(file, index):
	file.seek(0,0)
	lineIndex = file.readline(3)
	lineText = file.readline()
	
	while lineIndex != index:
		lineIndex = file.readline(3)
		lineText = file.readline()
	
	if lineIndex == index:
		print lineText

location = '03N'
getAreaText(f, location)
location = '05N'
getAreaText(f, location)

#	Contents of levels.txt:
#	01NYou are facing North. There is a thing here.
#	02NYou are facing North. The thing is right behind you.
#	03NYou are facing North. That thing is still nearby, you can feel it.
#	04NYou are facing North. You find yourself wondering how that thing is now that you've moved away.
#	05NYou are facing North. You've temporarily forgotten the thing and become obsessed with the new wonders before you.
#	06NYou are facing North. You find the thing creeping back into your mind on occasion, slyly peeking out from behind old memories.
#	07NYou are facing North. You realize that you miss the thing and you want to return to it.

#	Sample output:
#	>python .\TextGame.py
#	You are facing North. That thing is still nearby, you can feel it.
#	
#	You are facing North. You've temporarily forgotten the thing and become obsessed with the new wonders before you.
#	>