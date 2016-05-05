# **************************************
# A Text Adventure Game
# File: TAData.py
# Version: 0.1.2
# Author: FogOgg
# Email: NotMyPersonalEmail@gmail.com
# Initial: 05/01/2016
# Last Edit: 05/03/2016
# **************************************
#
# Game Rooms
# Attribute template:
#
#'xxxxx':{
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

gameRooms = {
    '005050':{
        'ROOMID': '005050',
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
        'OBJECTS': []
    },
    
    '005150':{
        'ROOMID': '005150',
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
        'OBJECTS': []
    },
    
    '005051':{
        'ROOMID': '005051',
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
        'OBJECTS': []
    },
    
    '004950':{
        'ROOMID': '004950',
        'ROOMNAME': 'The Bathroom',
        'SHORTDESC': 'You found a toilet!',
        'LONGDESC': '',
        'NORTHEXIT': False,
        'SOUTHEXIT': False,
        'WESTEXIT': False,
        'EASTEXIT': True,
        'STAIRSUP': False,
        'STAIRSDOWN': False,
        'ITEMS': ['004'],
        'OBJECTS': ['AB']
    },
    
    '005052':{
        'ROOMID': '005052',
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
        'OBJECTS': []
    },
    
    '005152':{
        'ROOMID': '005152',
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
        'OBJECTS': []
    },
    
    '005252':{
        'ROOMID': '005252',
        'ROOMNAME': 'The Grand Entry Hall',
        'SHORTDESC': 'A locked door dominates the North wall. You think you hear a fart from the West.',
        'LONGDESC': 'This bare room holds little of interest. You can hear faint sounds from the portal to the North, but can\'t quite make out their source. That was definitely a fart from the West.',
        'NORTHEXIT': False,
        'SOUTHEXIT': False,
        'WESTEXIT': True,
        'EASTEXIT': False,
        'STAIRSUP': False,
        'STAIRSDOWN': False,
        'ITEMS': ['003'],
        'OBJECTS': ['AA']
    },
    
    '005151':{
        'ROOMID': '005151',
        'ROOMNAME': 'Winners Circle',
        'SHORTDESC': 'Googratutions you habe win de gaem.',
        'LONGDESC': '',
        'NORTHEXIT': False,
        'SOUTHEXIT': True,
        'WESTEXIT': False,
        'EASTEXIT': False,
        'STAIRSUP': False,
        'STAIRSDOWN': False,
        'ITEMS': [],
        'OBJECTS': []
    },
    
    '004951':{
        'ROOMID': '004951',
        'ROOMNAME': 'The Sewer',
        'SHORTDESC': 'Eww, you got the poo on you!',
        'LONGDESC': '',
        'NORTHEXIT': False,
        'SOUTHEXIT': False,
        'WESTEXIT': True,
        'EASTEXIT': False,
        'STAIRSUP': False,
        'STAIRSDOWN': False,
        'ITEMS': [],
        'OBJECTS': []
    }
}

# Game Items
# Attribute template:
#
#    'xxx':{
#        'ITEMNAME': '',
#        'ROOMID': '',
#        'ITEMID': '',
#        'ROOMTEXT': '',
#        'ROOMEXAMINE':'',
#        'ITEMDESC': '',
#        'USEOBJECT': '',
#        'ONEUSE': True,
#        'PRESENT': True,
#        'KEYWORDS': []
#    }

gameItems = {
    '000':{
        'ITEMNAME': 'phial of farts',
        'ROOMID': '005050',
        'ITEMID': '000',
        'ROOMTEXT': 'As you look around the room the light glints off something hidden under some rags in the corner.',
        'ROOMEXAMINE':'',
        'ITEMDESC': 'Farts and EVERYWHERE!',
        'USEOBJECT': 'AB',
        'ONEUSE': True,
        'PRESENT': True,
        'KEYWORDS': ['vial','phial','glass','jar']
    },
    
    '001':{
        'ITEMNAME': 'Poopscalibur',
        'ROOMID': '005150',
        'ITEMID': '001',
        'ROOMTEXT': 'An exceptionally long turd is laying in the corner.',
        'ROOMEXAMINE':'',
        'ITEMDESC': 'Here is poop!',
        'USEOBJECT': '',
        'ONEUSE': True,
        'PRESENT': True,
        'KEYWORDS': ['poop','turd','poo']
    },
    
    '002':{
        'ITEMNAME': 'Tickle Me Elmo',
        'ROOMID': '005052',
        'ITEMID': '002',
        'ROOMTEXT': 'A naked cat statue stands in the NorthWest corner.',
        'ROOMEXAMINE':'',
        'ITEMDESC': 'Hee hee hee! Elmo LOVE tickles!',
        'USEOBJECT': '',
        'ONEUSE': True,
        'PRESENT': True,
        'KEYWORDS': ['cat','statue']
    },
    
    '003':{
        'ITEMNAME': 'dirty underwear',
        'ROOMID': '005252',
        'ITEMID': '003',
        'ROOMTEXT': 'A ragged scrap of discolored cloth clings to the door handle, suspended by some unknown force.',
        'ROOMEXAMINE':'',
        'ITEMDESC': 'These tattered underpants have seen better days. The remaining fabric is stained and streaked with every shade of brown and yellow imaginable.',
        'USEOBJECT': 'AA',
        'ONEUSE': True,
        'PRESENT': True,
        'KEYWORDS': ['cloth','underwear','underpants']
    },
    
    '004':{
        'ITEMNAME': 'wad of wet TP',
        'ROOMID': '004950',
        'ITEMID': '004',
        'ROOMTEXT': 'The toilet is clogged.',
        'ROOMEXAMINE':'',
        'ITEMDESC': 'A soggy wad of wet toilet paper. It might be Charmin. Luckily the room is too dark for you to discern its state of use.',
        'USEOBJECT': '',
        'ONEUSE': True,
        'PRESENT': True,
        'KEYWORDS': ['wad','clog','tp','toiletpaper','paper']
    },
    
    '005':{
        'ITEMNAME': 'used condom',
        'ROOMID': None,
        'ITEMID': '005',
        'ROOMTEXT': None,
        'ROOMEXAMINE': None,
        'ITEMDESC': 'Ugh, why would you be hanging onto this, you monster?',
        'USEOBJECT': None,
        'ONEUSE': True,
        'PRESENT': False,
        'KEYWORDS': []
    }
}

# Game Objects
# Attribute Template
#'yy':{
#    'ROOMID': '',
#    'USEITEM': '',
#    'REWARDITEM': None,
#    'OBJECTNAME': None,
#    'OBJECTDESC': '',
#    'OBJECTID': '',
#    'LOCKED': True,
#    'PORTALDIR': '',
#    'EVENTTRIGGER': None,
#    'KEYWORDS': []
#},

gameObjects = {
    'AA':{
        'ROOMID': '005252',
        'USEITEM': '003',
        'REWARDITEM': None,
        'OBJECTNAME': None,
        'OBJECTDESC': 'A tall, plain, heavy door made of solid wood. There doesn\'t appear to be a way to break through.',
        'OBJECTID': 'AA',
        'LOCKED': True,
        'PORTALDIR': 'NORTH',
        'EVENTTRIGGER': None,
        'KEYWORDS': ['door','doorway','portal']
    },
    
    'AB':{
        'ROOMID': '004950',
        'USEITEM': '000',
        'REWARDITEM': '004',
        'OBJECTNAME': 'disgusting toilet',
        'OBJECTDESC': 'At one time, this must have been a nice toilet. Now, it is encrusted with any number of foul substances and sharing the room with it repulses you.',
        'OBJECTID': 'AB',
        'LOCKED': False,
        'PORTALDIR': None,
        'EVENTTRIGGER': None,
        'KEYWORDS': ['toilet','commode','wc','john','crapper']
    }
}

# Action verbs
# Attribute Template
    
gameActions={
    'move':'move',
    'go':'move',
    'walk':'move',
    'inventory':'ui',
    'health':'ui',
    'state':'ui',
    'look':'look',
    'examine':'look',
    'fart':'action',
    'lick':'action',
    'take':'action',
    'get':'action',
    'touch':'action',
    'poke':'action',
    'attack':'action',
    'use':'action',
    'on':'modifier',
    'in':'modifier',
    'quit':'quit',
    'exit':'quit'
}

# Movement words
# Attribute Template

gameMoves=[
    'north',
    'south',
    'east',
    'west',
    'up',
    'upstairs',
    'down',
    'downstairs'
]