# **************************************
# A Text Adventure Game
# File: TAData.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 05/01/2016
# Last Edit: 05/01/2016
# **************************************
#
# Game Rooms
# Attribute template:
#
#'xxxxxx':{
#    'ROOMNAME': '',
#    'SHORTDESC': '',
#    'LONGDESC': '',
#    'NORTHEXIT': True,
#    'SOUTHEXIT': True,
#    'WESTEXIT': True,
#    'EASTEXIT': True,
#    'STAIRSUP': True,
#    'STAIRSDOWN': True,
#    'ITEMS': [],
#},

def getGameRooms():
    gameRooms = {
        '005050A':{
            'ROOMID': '005050A',
            'ROOMNAME': '',
            'SHORTDESC': 'This room is a mess! Where is your mother?',
            'LONGDESC': '',
            'NORTHEXIT': True,
            'SOUTHEXIT': False,
            'WESTEXIT': True,
            'EASTEXIT': True,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': ['000'],
        },
        
        '005150A':{
            'ROOMID': '005150A',
            'ROOMNAME': 'Your Bedroom',
            'SHORTDESC': 'And I thought the LAST room was bad!',
            'LONGDESC': '',
            'NORTHEXIT': False,
            'SOUTHEXIT': False,
            'WESTEXIT': True,
            'EASTEXIT': False,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': ['001'],
        },
        
        '005051A':{
            'ROOMID': '005051A',
            'ROOMNAME': '',
            'SHORTDESC': 'What a delightful hallway. An odor wafts from the South.',
            'LONGDESC': '',
            'NORTHEXIT': True,
            'SOUTHEXIT': True,
            'WESTEXIT': False,
            'EASTEXIT': False,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': [],
        },
        
        '004950A':{
            'ROOMID': '004950A',
            'ROOMNAME': 'The Bathroom',
            'SHORTDESC': 'You found a toilet!',
            'LONGDESC': '',
            'NORTHEXIT': False,
            'SOUTHEXIT': False,
            'WESTEXIT': False,
            'EASTEXIT': True,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': [],
        },
        
        '005052A':{
            'ROOMID': '005052A',
            'ROOMNAME': 'Art Corner',
            'SHORTDESC': 'You don\'t want to know what you just stepped in.',
            'LONGDESC': '',
            'NORTHEXIT': False,
            'SOUTHEXIT': True,
            'WESTEXIT': False,
            'EASTEXIT': True,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': ['002'],
        },
        
        '005152A':{
            'ROOMID': '005152A',
            'ROOMNAME': 'Breakfast Nook',
            'SHORTDESC': 'A tapestry depicting a bowl of Cheerios is jauntily draped on the North wall.',
            'LONGDESC': '',
            'NORTHEXIT': False,
            'SOUTHEXIT': False,
            'WESTEXIT': True,
            'EASTEXIT': True,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': [],
        },
        
        '005252A':{
            'ROOMID': '005252A',
            'ROOMNAME': 'The Grand Entry Hall',
            'SHORTDESC': 'A locked door dominates the North wall. You think you hear a fart from the West.',
            'LONGDESC': '',
            'NORTHEXIT': False,
            'SOUTHEXIT': False,
            'WESTEXIT': True,
            'EASTEXIT': False,
            'STAIRSUP': False,
            'STAIRSDOWN': False,
            'ITEMS': ['003'],
        }
    }
    
    return gameRooms

# Game Items
# Attribute template:
#
#    'xxx':{
#        'ROOMID': '',
#        'ITEMID': '',
#        'ROOMTEXT': '',
#        'ITEMDESC': '',
#        'ONEUSE': True,
#        'KEYWORDS': []
#    }
    
def getGameItems():
    gameItems = {
        'phial of farts':{
            'ITEMNAME': 'phial of farts',
            'ROOMID': '005050A',
            'ITEMID': '000',
            'ROOMTEXT': 'As you look around the room the light glints off something hidden under some rags in the corner.',
            'ITEMDESC': 'Farts and EVERYWHERE!',
            'ONEUSE': True,
            'KEYWORDS': ['vial','phial','glass','jar']
        },
        
        'Poopscalibur':{
            'ITEMNAME': 'Poopscalibur',
            'ROOMID': '005150A',
            'ITEMID': '001',
            'ROOMTEXT': 'An exceptionally long turd is laying in the corner.',
            'ITEMDESC': 'Here is poop!',
            'ONEUSE': True,
            'KEYWORDS': ['poop','turd','poo']
        },
        
        'Tickle Me Elmo':{
            'ITEMNAME': 'Tickle Me Elmo',
            'ROOMID': '005052A',
            'ITEMID': '002',
            'ROOMTEXT': 'A naked cat statue stands in the NorthWest corner.',
            'ITEMDESC': 'Hee hee hee! Elmo LOVE tickles!',
            'ONEUSE': True,
            'KEYWORDS': ['cat','statue']
        },
        
        'dirty underwear':{
            'ITEMNAME': 'dirty underwear',
            'ROOMID': '005252A',
            'ITEMID': '003',
            'ROOMTEXT': 'A scrap of ragged cloth hangs from the door handle.',
            'ITEMDESC': 'These tattered underpants have seen better days. The remaining fabric is stained and streaked with every shade of brown and yellow imaginable.',
            'ONEUSE': True,
            'KEYWORDS': ['cloth','underwear','underpants']
        }
    }
    
    return gameItems