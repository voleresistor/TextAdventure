# **************************************
# A Text Adventure Game
# File: TextAdventure.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 04/19/2016
# Last Edit: 04/29/2016
# **************************************
# CHANGELOG:
#   v0.1.3(04/30/16):
#       Implement items class
#       Implement player class
#	v0.1.2(04/29/16):
#		Break out classes and functions into modules
#		Integrate csv usage into RoomFile class
#		Movement is fully fleshed out with obstructions
#	v0.1.1:
#		Create PlayerCommand class
#		Break out keywords into move or item type
#		Make getPlayerCommand use new PlayerCommand class
#		Create playerMoved function
# 	v0.1:
# 		Add main function
# 		Add playerCommand function
# 		Add comments
# 		Add informational text at top
#		Move all the game setup into main function
#		Game is "playable" in the sense that it can take input. There is no input processing capability as of yet.
#	initial:
#		Add getAreaText function

# *******************************
# Pre-Game setup
# *******************************

# Make sure the Python version meets requirements
import sys
assert sys.version_info >= (3,5)

# Clear the console
import os
os.system('cls' if os.name=='nt' else 'clear')

# *******************************
# Some indispensable imports
# *******************************
import TAMain

# *******************************
# Run Game
# *******************************
TAMain.main()





#	Sample output:
#	>python .\TextAdventure.py
#	A locked door dominates the North wall. You think you hear a fart from the West.
#	
#	> move west
#	A tapestry depicting a bowl of Cheerios is jauntily draped on the North wall.
#	
#	> move west
#	A statue of a naked cat is in the NW corner. You don't want to know what you just stepped in.
#	
#	> yes i do
#	How does one yes i do?
#	
#	> move south
#	What a delightful hallway. An odor wafts from the South.
#	
#	> move south
#	Farts are EVERYWHERE!
#	
#	> move south
#	The way is blocked!
#	Farts are EVERYWHERE!
#	
#	> move west
#	You found a toilet!
#	
#	> move east
#	Farts are EVERYWHERE!
#	
#	> move east
#	Here is poop!