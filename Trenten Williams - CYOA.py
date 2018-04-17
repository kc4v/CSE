def fight(enemy):
    print("A wild %s appears!" % enemy.name)
    while player.health > 0 and enemy.health > 0:
        if "attack" == enemy.health 


class Item(object):
    def __init__(self, name, weight, value, durability, damage):
        self.name = name
        self.weight = weight
        self.value = value
        self.durability = durability
        self.max_durability = durability
        self.damage = damage

    def picked_up(self):
        print("You picked up %s" % self.name)

    def drop(self):
        print("You dropped %s." % self.name)


class Weapons(Item):
    def __init__(self, name, weight, value, durability, damage):
        super(Weapons, self).__init__(name, weight, value, durability, damage)
        self.damage = damage

    def attack(self):
        print("You attacked the target and did %s" % self.damage)


class Consumable(Item):
    def __init__(self, name, weight, value, durability, damage):
        super(Consumable, self).__init__(name, weight, value, durability, damage)

    def eat(self):
        print("You are able to eat the %s" % self.name)


class Clothing(Item):
    def __init__(self, name, weight, value, durability, damage_resistant, damage):
        super(Clothing, self).__init__(name, weight, value, durability, damage)
        self.damage_resistant = damage_resistant

    def wear(self):
        print("The clothing protected you and it did %s" % self.damage_resistant)


class Potion(Item):
    def __init__(self, name, weight, value, durability, heal, damage):
        super(Potion, self).__init__(name, weight, value, durability, damage)
        self.heal = heal

    def drink(self):
        print("You can drink the %s potion" % self.name)


class Backpack(Item):
    def __init__(self, name, weight, value, durability, stored_items):
        super(Backpack, self).__init__(name, weight, value, durability, [])
        self.stored_items = stored_items

    def open(self):
        print("Shows every %s" % self.stored_items)


class Throwable(Item):
    def __init__(self, name, weight, value, durability, damage):
        super(Throwable, self).__init__(name, weight, value, durability, damage)

    def throw(self):
        print("If u want to, you can throw this %s" % self.name)


class Drop(Item):
    def __init__(self, name, weight, value, durability):
        super(Drop, self).__init__(name, weight, value, durability, None)

    def discard(self):
        print("You have dropped %s" % self.name)


class Combination(Item):
    def __init__(self, name, weight, value, durability, damage):
        super(Combination, self).__init__(name, weight, value, durability, damage)

    def combine(self):
        print("You have created %s" % self.name)


class Axe(Item):
    def __init__(self, name, weight, value, durability):
        super(Axe, self).__init__("Huntress Axe", "86 pounds", "$500,900", 55, 86)

    def axe(self):
        print("You have the %s" % self.name)


class Chainsaw(Item):
    def __init__(self, name, weight, value, durability):
        super(Chainsaw, self).__init__("Hillbilly's Chainsaw", "134 pounds", "$690,040", 87, 100)

    def chainsaw(self):
        print("You have the %s" % self.name)


class Knife(Item):
    def __init__(self, name, weight, value, durability):
        super(Knife, self).__init__("Michel Myers Knife", "45 pounds", "$4,002", 69, 58)


class Bow(Item):
    def __init__(self, name, weight, value, durability):
        super(Bow, self).__init__("Farcry 4 Bow", "20 pounds", "$2,430", 70, 80)


class NinjaStars(Item):
    def __init__(self, name, weight, value, durability):
        super(NinjaStars, self).__init__("Genji's Ninja Stars", "5 pounds", "$6,000", 2, 60)


class Headphones(Item):
    def __init__(self, name, weight, value, durability):
        super(Headphones, self).__init__("My headphones", "2 pounds", "$70", 50, 77)
        

class Character(object):
    def __init__(self, name, talk, limit, inventory, armor, abilities, health, attack, uses, description):
        self.name = name
        self.inventory = inventory  # List
        self.health = health
        self.abilities_max = abilities
        self.attack_amt = attack
        self.description = description
        self.talk_others = talk
        self.limit_have = limit
        self.armor_reduction = armor
        self.uses = uses

    def talk(self):
        print("Hello")

    def attack(self, target):
        target.health -= self.attack_amt

    def limit(self, inventory):
        inventory.limit = 8

    def abilities(self, limit):
        limit.abilities = 5

    def take_damage(self, dmg):
        total_dmg = dmg - self.armor_reduction
        if total_dmg < 0:
            total_dmg = 0
        self.health -= total_dmg

    def inventory_use(self, item):
        self.inventory.remove(item)


class Room(object):
    def __init__(self, name, north, south, east, west, description, enemies=None, items=None):
        if items is None:
            items = []
        if enemies is None:
            enemies = []
        self.name = name
        self.east = east
        self.north = north
        self.south = south
        self.west = west
        self.description = description
        self.enemies = enemies
        self.item = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


axe = Axe("Huntress Axe", "86", "$500,900", 55)

player = Character("Eren Jaeger", "Hello", 5, [], "Protection", 5, 100, "Depends on the power of the weapon", 3,
                   "Has been born inside of walls created by mankind, a colossal titan has broken down the wall \n"
                   "where his family and himself lived and were, the debris got his mom stuck and broke her legs, \n"
                   "then a titan got to her since there was a guy that was to much a coward to fight it and ate her, \n"
                   "now he has to find a key in a house to save himself and others to fight back.")


enemy = Character("Zombie", None, None, None, None, None, 100, 87, "unlimited", "An undead person that goes \n"
                                                                                "for human brains.")


# Initialize Rooms
door = Room("Door", None, None, "hallway", None, "Just ran inside after being chased from some zombies, \n"
                                                 "*check pockets for keys*, are you serious!?, now I have to search \n"
                                                 "the house for the keys to the shed since I forgot to take \n"
                                                 "them, but I got to be ready for anything, I still don't know if \n"
                                                 "there inside, I need to find a weapon and close all the windows \n"
                                                 "so this place can be safe again, for now I have to find a weapon.")
hallway = Room("Hallway", None, "kitchen", "closet", "door", "I can go to the closet to the West or go to the \n"
                                                             "Kitchen to the South, or just go back to the door."
                                                             "We need to go upstairs to get the key to the \n"
                                                             "shed but we can get a weapon before we go, there's \n"
                                                             "a Den to the East.")
closet = Room("Closet", None, "living_room", None, "hallway", "I'm at the closet, there might be something inside, \n"
                                                              "if not I can go to the living room to the south.")
living_room = Room("Living Room", "closet", None, None, "stairs", "There are 2 windows in here, I better close \n"
                                                                  "them before zombies crawl through, OHH! One was \n"
                                                                  "hiding behind the couch", 1)
stairs = Room("Stairs", None, "hallway2", "living_Room", "den", "We need to go upstairs to get the key to the \n"
                                                                "shed(South) but we can get a weapon before \n"
                                                                "we go, there's a Den to the East.")
den = Room("Den", "kitchen", None, "stairs", None, "Another window, need to close it.")
kitchen = Room("Kitchen", "hallway", "den", None, None, "Nice, there is still a knife here.", None, 1)
hallway2 = Room("Hallway2", "stairs", "master_Bedroom", "bathroom", "hallway3", "I can go to the bathroom to the \n"
                                                                                "east but I hear sound in there, or \n"
                                                                                "just go to the master bedroom to \n"
                                                                                "the south, there is another \n"
                                                                                "hallway to the East.")
hallway3 = Room("Hallway3", "room1", "room3", "hallway2", "room2", "I can go back to the second hallway to the \n"
                                                                   "West, or go to room3 to the North, \n"
                                                                   "room2 to the South or room1 to the east.")
bathroom = Room("Bathroom", None, None, None, "hallway2", "Ahhh, why is there a zombie in the bathroom!?", 1, 1)
room1 = Room("Room1", None, "hallway3", None, None, "The key is not in here, but there is a window \n"
                                                    "so I better close it.")
room2 = Room("Room2", None, None, "hallway3", None, "The key is not in here, but there is a window \n"
                                                    "so I better close it.")
room3 = Room("Room3", "hallway3", None, None, None, "The key is not in here, but there is a window \n"
                                                    "so I better close it after I kill this zombie.", 1)
master_bedroom = Room("Master_Bedroom", "hallway2", None, None, None, "The key is not in here also, \n"
                                                                      "but there is a window so I better close it af\n"
                                                                      "ter I kill these 3 zombies.")
shed_door = Room("Shed_Door", None, None, None, "hallway4", "I finally got in the shed, now I have to grab a gun.")
hallway4 = Room("Hallway4", "sniper Room", "assault Room", "shed_door", None, "There is snipers to the North \n"
                                                                              "and some assault rifles to the South.")
assault_room = Room("Assault_Room", "hallway", None, None, None, "ok, seems like going with the assault rifles.")
sniper_room = Room("Sniper_Room", None, "hallway4", None, None, "ok, seems like going with the snipers rifles.")
outside = Room("Outside", None, "Shed2", "Shed_Door", None, "Ok, now I have to fights these5 zombies then choose a \n"
                                                            "shed to grab a weapon from", 5)
Shed_Door2 = Room("Shed_Door2", "Throwable_Room", "Hand_to_Hand", None, None, "To the north is some throwable it\n"
                                                                              "ems we can use against the zombies \n"
                                                                              "and to the south is some hand to hand \n"
                                                                              "weapons.")
Hand_to_Hand = Room("Hand_to_Hand", "Shed_Door2", None, None, None, "Now in this room there is nothing but hand to \n"
                                                                    "hand combat weapons")
Throwable_Room = Room("Throwable_Room", None, "Shed_Door2", None, None, "So in this room is items that I can throw \n"
                                                                        "at zombies.")
directions = ['north', 'south', 'east', 'west']
current_node = door
Items = []
while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_')
    if command == 'quit':
        quit(0)

    if "take" in command:
        item = command[5:]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    elif "attack" in command:
        if len(current_node.enemies) > 0:
            # Enemies exist
            while len(current_node.enemies) > 0:
                fight(current_node.enemies[0])
                current_node.enemies.pop(0)
        else:
            print("There is nothing to fight here")

    else:
        print("Command not recognized")
    print()
