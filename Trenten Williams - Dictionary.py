world_map = {
    'DOOR': {
        'NAME': "The door of the house",
        'DESCRIPTION': "Just ran inside after being chased from some zombies, *clank*, are you serious there are some\n"
                       "zombies already in the house, but i can't fight them with nothing so before I fight them  I\n"
                       "need to find a weapon and close all the windows so this place can be safe again, for now I \n"
                       "have to dodge them.",
        'PATHS': {
            'WEST': 'HALLWAY',
            'W': 'HALLWAY'
        }
    },
    'HALLWAY': {
        'NAME': 'Hallway',
        'DESCRIPTION': "I can go to the closet to the West or go to the Kitchen to the South, or just go back to the "
                       "door.",
        'PATHS': {
            'WEST': 'CLOSET',
            'W': 'CLOSET',
            'E': 'DOOR',
            'EAST': 'DOOR',
            'SOUTH': 'KITCHEN',
            'S': 'KITCHEN'
        }
    },
    'STAIRS': {
        'NAME': 'Stairs',
        'DESCRIPTION': "We need to go upstairs to get the key to the shed(South) but we can get a weapon before "
                       "we go, there's a Den to the East.",
        'PATHS': {
            'EAST': 'DEN',
            'E': 'DEN',
            'S': 'HALLWAY2',
            'SOUTH': 'HALLWAY2',
            'W': 'LIVING ROOM',
            'WEST': 'LIVING ROOM'


        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "Nice, there is still a knife here.",
        'PATHS': {
            'EAST': 'DEN',
            'E': 'DEN',
            'NORTH': 'HALLWAY',
            'N': 'HALLWAY'
        }
    },
    'DEN': {
        'NAME': 'Den',
        'DESCRIPTION': "Another window, need to close it.",
        'PATHS': {
            'NORTH-WEST': 'KITCHEN',
            'NW': 'KITCHEN',
            'EAST': 'STAIRS',
            'E': 'STAIRS'
        }
    },
    'HALLWAY2': {
        'NAME': 'Hallway2',
        'DESCRIPTION': "I can go to the bathroom to the West but I hear sound in there, or just go to the master \n "
                       "bedroom to the south, there is another hallway to the East.",

        'PATHS': {
            'WEST': 'BATHROOM',
            'W': 'BATHROOM',
            'SOUTH': 'MASTER BEDROOM',
            'S': 'MASTER BEDROOM',
            'EAST': 'HALLWAY3',
            'E': 'HALLWAY3'
        }
    },
    'HALLWAY3': {
        'NAME': 'Hallway3',
        'DESCRIPTION': "I can go back to the second hallway to the West, or go to room3 to the North, \n"
                       "room2 to the South or room1 to the east.",

        'PATHS': {
            'WEST': 'HALLWAY2',
            'W': 'HALLWAY2',
            'SOUTH': 'ROOM2',
            'S': 'ROOM2',
            'EAST': 'ROOM1',
            'E': 'ROOM1',
            'NORTH': 'ROOM3',
            'N': 'ROOM3'
        }
    },
    'CLOSET': {
        'NAME': 'Closet',
        'DESCRIPTION': "I'm at the closet.",
        'PATHS': {
            'SOUTH': 'LIVING ROOM',
            'S': 'LIVING ROOM',
            'EAST': 'HALLWAY',
            'E': 'HALLWAY'
        }
    },

    'ROOM1': {
        'NAME': 'Room1',
        'DESCRIPTION': "The key is not in here, but there is a window so I better close it.",
        'PATHS': {
            'SOUTH': 'HALLWAY3',
            'S': 'HALLWAY3'
        }
    },
    'BATHROOM': {
        'NAME': 'Bathroom',
        'DESCRIPTION': "",
        'PATHS': {
            'EAST': 'HALLWAY2',
            'E': 'HALLWAY2'
        }
    },
    'SHED': {
        'NAME': 'Shed',
        'DESCRIPTION': "I finally got in the shed, now I have to get a gun.",
        'PATHS': {
            'WEST': 'HALLWAY4',
            'W': 'HALLWAY4'
        }
    },
    'SNIPER ROOM': {
        'NAME': 'Sniper Room',
        'DESCRIPTION': "ok, seems like going with the snipers rifles.",
        'PATHS': {
            'SOUTH': 'HALLWAY4',
            'S': 'HALLWAY4'
        }
    },
    'ASSAULT ROOM': {
        'NAME': 'ASSAULT ROOM',
        'DESCRIPTION': "ok, It looks like i'm going to go with the assault rifles.",
        'PATHS': {
            'NORTH': 'HALLWAY4',
            'N': 'HALLWAY4'
        }
    },
    'HALLWAY4': {
        'NAME': 'Hallway4',
        'DESCRIPTION': "There is snipers to the North and some assault rifles to the South.",
        'PATHS': {
            'NORTH': 'SNIPER ROOM',
            'N': 'SNIPER ROOM',
            'SOUTH': 'ASSAULT ROOM',
            'S': 'ASSAULT ROOM'
        }
    },
    'LIVING ROOM': {
        'NAME': 'Living Room',
        'DESCRIPTION': "There are 2 windows in here, I better close them before zombies crawl through.",
        'PATHS': {
            'NORTH': 'CLOSET',
            'N': 'CLOSET',
            'EAST': 'STAIRS',
            'E': 'STAIRS'
        }
    },
    'ROOM2': {
        'NAME': 'Room2',
        'DESCRIPTION': "The key is not in here, but there is a window so I better close it.",
        'PATHS': {
            'SOUTH': 'HALLWAY3',
            'S': 'HALLWAY3'
        }
    },
    'ROOM3': {
        'NAME': 'Room1',
        'DESCRIPTION': "The key is not in here, but there is a window so I better close it.",
        'PATHS': {
            'SOUTH': 'HALLWAY3',
            'S': 'HALLWAY3'
        }
    },
    'MASTER BEDROOM': {
        'NAME': 'Master Bedroom',
        'DESCRIPTION': "The key is not in here also, but there is a window so I better close it.",
        'PATHS': {
            'SOUTH': 'HALLWAY3',
            'S': 'HALLWAY3'
        }
    }
}

current_node = world_map['DOOR']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NW', 'N', 'S', 'E', 'W']


while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not recognized")
    print()

# Defining function
