debug = 1  # Cheat Mode


def fight(enemy):
    print("A %s has appeared!" % enemy.name)
    while player.health > 0 and enemy.health > 0:
        print("What do you want to do?")
        cmd = input(">_ ")
        if cmd == 'attack':
            player.attack(enemy)
        else:
            print("You hesitate")
        if enemy.health > 0:
            enemy.attack(player)


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
    def __init__(self):
        super(Axe, self).__init__("Huntress Axe", 66, 568, 2, 87)

    def axe(self):
        print("You have the %s" % self.name)


class Chainsaw(Item):
    def __init__(self):
        super(Chainsaw, self).__init__("Hillbilly's Chainsaw", 134, 690, 3, 100)

    def chainsaw(self):
        print("You have the %s" % self.name)


class Sniper(Item):
    def __init__(self):
        super(Sniper, self).__init__("Glaz's Sniper", 86, 18028, 1000, 1000)


class AR(Item):
    def __init__(self):
        super(AR, self).__init__("Fortnite Lengendary Scar", 123, 8467, 10000, 100)


class Knife(Item):
    def __init__(self):
        super(Knife, self).__init__("Michel Myers Knife", 45, 700, 1, 58)


class Bow(Item):
    def __init__(self):
        super(Bow, self).__init__("Warframe Bow", 10, 267, 3, 80)


class NinjaStars(Item):
    def __init__(self):
        super(NinjaStars, self).__init__("Genji's Ninja Stars", 4, 409, 2, 60)


class Headphones(Item):
    def __init__(self):
        super(Headphones, self).__init__("My headphones", 2, 70, 1, 13)


class Key(Item):
    def __init__(self):
        super(Key, self).__init__("Key", 0, 58, 1, 0)

    @staticmethod
    def use():
        pass


class DoorKey(Key):
    def __init__(self):
        super(DoorKey, self).__init__()
    @staticmethod
    def use():
        global current_node
        if current_node == door:
            door.west = 'outside'
            door.w = 'outside'
            print("You unlock the door to outside.")
        else:
            print("There is no door to unlock here -_-")


class ShedKey(Key):
    def __init__(self):
        super(ShedKey, self).__init__()
    @staticmethod
    def use():
        global current_node
        if current_node == outside:
            outside.west = 'shed_door'
            outside.w = 'shed_door'
            print("You unlock the door to the shed, pick a gun.")
        else:
            print("There is no door to unlock here -_-")


class Character(object):
    def __init__(self, name, talk, limit, inventory, armor, abilities, health, weapon, uses, description):
        self.name = name
        self.inventory = inventory  # List
        self.health = health
        self.abilities_max = abilities
        self.weapon = weapon
        self.description = description
        self.talk_others = talk
        self.limit_have = limit
        self.armor_reduction = armor
        self.uses = uses

    def talk(self):
        print("Hello")

    def attack(self, target):
        print("%s attacks %s" % (self.name, target.name))
        target.take_damage(self.weapon.damage)

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

    def take(self, item):
        self.inventory.append(item)


class Room(object):
    def __init__(self, name, north, south, east, west, description, enemies=0, items=None):
        if items is None:
            items = []
        self.name = name
        self.east = east
        self.e = east
        self.north = north
        self.n = north
        self.south = south
        self.s = south
        self.west = west
        self.w = west
        self.description = description
        self.enemies = enemies
        self.item = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


axe = Axe()
chainsaw = Chainsaw()
headphones = Headphones()
knife = Knife()
door_key = DoorKey()
shed_key = ShedKey()
sniper = Sniper
Assault_Rifle = AR

player = Character("Soul collector", "Hello", 5, [], 80, 5, 100, axe, None, "Has been born inside of walls created \n"
                                                                            "by mankind, a colossal titan has \n"
                                                                            "broken down the wall where his family \n"
                                                                            "and himself lived and were, the debris \n"
                                                                            "got his mom stuck and broke her legs, \n"
                                                                            "then a titan got to her since there \n"
                                                                            "was a guy that was to much a coward to \n"
                                                                            "fight it and ate her, how he has to \n"
                                                                            "find a key in a house to save himself \n"
                                                                            "and others to fight back.")


enemy = Character("Zombie", None, None, None, None, None, 100, axe, "unlimited", "An undead person that goes for \n"
                                                                                 "human brains.")
# Initialize Rooms
door = Room("Door", None, None, "hallway", None, "Just ran inside after being chased from some zombies, \n"
                                                 "*check pockets for keys*, are you serious!?, now I have to \n"
                                                 "search the house for the key to the shed since that man told \n"
                                                 "me that he had guns in the shed, and they can help me \n"
                                                 "survive, but I got to be ready for anything, I still don't \n"
                                                 "know if there inside, I need to find a weapon and close all \n"
                                                 "the windows so this place can be safe again, for now I have \n"
                                                 "to find a weapon.",
            0, 0)
hallway = Room("Hallway", None, "kitchen", "closet", "door", "I can go to the closet to the West or go to the \n"
                                                             "Kitchen to the South, or just go back to the door."
                                                             "We need to go upstairs to get the key to the \n"
                                                             "shed but we can get a weapon before we go, there's \n"
                                                             "a Den to the East.")
closet = Room("Closet", None, "living_room", None, "hallway", "I'm at the closet, there might be something inside, \n"
                                                              "if not I can go to the living room to the south.", 0,
              [axe])
living_room = Room("Living Room", "closet", None, None, "stairs", "This place looks nice with no zombies", 1)
stairs = Room("Stairs", None, "hallway2", "living_Room", "den", "We need to go upstairs to get the key to the \n"
                                                                "shed(South) but we can get a weapon before \n"
                                                                "we go, there's a Den to the East.")
den = Room("Den", "kitchen", None, "stairs", None, "This den is s big.")
kitchen = Room("Kitchen", "hallway", "den", None, None, "Of course, the kitchen is empty, there might be something \n"
                                                        "in here.", 0, [knife])
hallway2 = Room("Hallway2", "stairs", "master_Bedroom", "bathroom", "hallway3", "I can go to the bathroom to the \n"
                                                                                "east but I hear sound in there, or \n"
                                                                                "just go to the master bedroom to \n"
                                                                                "the south, there is another \n"
                                                                                "hallway to the East.", 3,
                [chainsaw, headphones])
hallway3 = Room("Hallway3", "room1", "room3", "hallway2", "room2", "I can go back to the second hallway to the \n"
                                                                   "West, or go to room3 to the North, \n"
                                                                   "room2 to the South or room1 to the east.")
bathroom = Room("Bathroom", None, None, None, "hallway2", "Here is the key", 1, [door_key])
room1 = Room("Room1", None, "hallway3", None, None, "The key is not in here.")
room2 = Room("Room2", None, None, "hallway3", None, "The key is not in here.")
room3 = Room("Room3", "hallway3", None, None, None, "The key is not in here.", 1)
master_bedroom = Room("Master_Bedroom", "hallway2", None, None, None, "The key is not in here also, \n"
                                                                      "but there is a window so I better close it af\n"
                                                                      "ter I kill these 3 zombies.")
shed_door = Room("Shed_Door", None, None, None, "hallway4", "I finally got in the shed, now I have to grab a gun.")
hallway4 = Room("Hallway4", "sniper_room", "assault_room", "shed_door", None, "There is snipers to the North \n"
                                                                              "and some assault rifles to the South.")
assault_room = Room("Assault_Room", "hallway", None, None, None, "ok, seems like going with the assault rifles.", 0,
                    [Assault_Rifle])
sniper_room = Room("Sniper_Room", None, "hallway4", None, None, "ok, seems like going with the snipers rifles.", 0,
                   [sniper])
outside = Room("Outside", None, "Shed2", "Shed_Door", None, "Ok, now I have to choose a \n"
                                                            "shed to grab a weapon from.", 5)

directions = ['north', "n", 'south', "s", 'east', "e", 'west', "w"]
current_node = door
Items = []
if debug == 1:
    player.inventory = [door_key, shed_key]
    player.weapon = Axe()
    player.weapon.damage = 90000
while player.health > 0:
    if current_node.enemies > 0:
        # Enemies exist
        while current_node.enemies > 0 and player.health:
            if debug == 1:
                print("You automatically win")
                current_node.enemies = 0
                continue
            fight(Character("Zombie", None, None, None, 20, None, 100, axe, "unlimited",
                            "An undead person that goes for human brains."))
            current_node.enemies -= 1
    print(player.health)
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

    elif command == "any items?":
        found = False
        if len(current_node.item) > 0:
            for item in current_node.item:
                print(item.name)
            cmd = input("Which item?").lower()
            for item in current_node.item:
                if cmd == item.name.lower():
                    player.take(item)
                    current_node.item.remove(item)
                    found = True
                    print("You have added it to your inventory.")
            if not found:
                print("I don't see the item you are looking for here.")
        else:
            print("There is nothing here. -_-")

    elif "item" in command:
        item_requested = [Sniper and AR]
        for item in current_node.item:
            if item.name == item_requested:
                player.take(current_node.item)
                quit(0)

    elif "take" in command:
        item_requested = command[5:]
        for item in current_node.item:
            if item.name == item_requested:
                player.take(current_node.item)

    elif command == "inventory":
        print(len(player.inventory))
        print()

    elif command == "health":
        print(player.health)

    elif command == 'use key':
        for key in player.inventory:
            if isinstance(key, Key):
                if current_node == outside and isinstance(key, ShedKey):
                    key.use()
                elif current_node == door and isinstance(key, DoorKey):
                    key.use()

            else:
                print("You don't have a key.")

    else:
        print("Command not recognized")
        print()
