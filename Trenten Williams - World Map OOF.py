class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.east = east
        self.north = north
        self.south = south
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
door = Room("Door", None, None, "hallway", None, "Just ran inside after being chased from some zombies, \n"
                                                 "*check pockets for keys*, are"
                                                 " you serious, now I have to search the house for the keys to the \n"
                                                 "shed since I forgot to take them, but \n"
                                                 "I got to be ready for anything, \n"
                                                 "I still don't know if there inside, \n"
                                                 "I need to find a weapon and close all the windows so this place can\n"
                                                 "be safe again, for now I have to is go unarmed.")
hallway = Room("Hallway", None, "kitchen", "closet", "door", "I can go to the closet to the West or go to the \n"
                                                             "Kitchen to the South, or just go back to the door."
                                                             "We need to go upstairs to get the key to the \n"
                                                             "shed but we can get a weapon before we go, \n"
                                                             "there's a Den to the East.")
closet = Room("Closet", None, "living_room", None, "hallway", "I'm at the closet, there might be something inside, \n"
                                                              "if not I can go to the living room to the south.")
living_room = Room("Living Room", "closet", None, None, "stairs", "There are 2 windows in here, I better close \n"
                                                                  "them before zombies crawl through.")
stairs = Room("Stairs", None, "hallway2", "living_Room", "den", "We need to go upstairs to get the key to the \n"
                                                                "shed(South) but we can get a weapon before \n"
                                                                "we go, there's a Den to the East.")
den = Room("Den", "kitchen", None, "stairs", None, "Another window, need to close it.")
kitchen = Room("Kitchen", "hallway", "den", None, None, "Nice, there is still a knife here.")
hallway2 = Room("Hallway2", "stairs", "master_Bedroom", "bathroom", "hallway3", "I can go to the bathroom to the \n"
                                                                                "east but I hear sound in there, or \n"
                                                                                "just go to the master bedroom to \n"
                                                                                "the south, there is another \n"
                                                                                "hallway to the East.")
hallway3 = Room("Hallway3", "room1", "room3", "hallway2", "room2", "I can go back to the second hallway to the \n"
                                                                   "West, or go to room3 to the North, \n"
                                                                   "room2 to the South or room1 to the east.")
bathroom = Room("Bathroom", None, None, None, "hallway2", None)
room1 = Room("Room1", None, "hallway3", None, None, "The key is not in here, but there is a window \n"
                                                    "so I better close it.")
room2 = Room("Room2", None, None, "hallway3", None, "The key is not in here, but there is a window \n"
                                                    "so I better close it.")
room3 = Room("Room3", "hallway3", None, None, None, "The key is not in here, but there is a window \n"
                                                    "so I better close it.")
master_bedroom = Room("Master_Bedroom", "hallway2", None, None, None, "The key is not in here also, \n"
                                                                      "but there is a window so I better close it.")
shed_door = Room("Shed_Door", None, None, None, "hallway4", "I finally got in the shed, now I have to grab a gun.")
hallway4 = Room("Hallway4", "sniper Room", "assault Room", "shed_door", None, "There is snipers to the North \n"
                                                                              "and some assault rifles to the South.")
assault_room = Room("Assault_Room", "hallway", None, None, None, "ok, seems like going with the assault rifles.")
sniper_room = Room("Sniper_Room", None, "hallway4", None, None, "ok, seems like going with the snipers rifles.")

directions = ['north', 'south', 'east', 'west']
current_node = door
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not recognized")
    print()
