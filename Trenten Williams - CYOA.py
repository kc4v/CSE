import random

# from tkinter import *
# import image
# root = Tk()
# root.title("Trenten!!!!!")
# label = Label(root, text="Hello and Welcome!")
# label.pack()
# root.mainloop()
# window = Tk()
#
# window.title("Join")
# window.geometry("800x800")
# window.configure(background='grey')
#
# imageFile = "flat,800x800,070,f.u3.jpg"
# window.im1 = image.open(imageFile)
#
# window.mainloop()

debug = 0  # Cheat Mode


def fight(enemy):
    print("A %s has appeared!" % enemy.name)
    while player.health > 0 and enemy.health > 0:
        print("What do you want to do? -_-")
        print("You have %d health left" % player.health)
        print("%s has %d health left" % (enemy.name, enemy.health))
        cmd = input(">_ ")
        if cmd == 'fight':
            player.attack(enemy)
            if player.equip == Weapons:
                Weapons.durability -= 1
            else:
                print("")
        else:
            print("You hesitate")
        if enemy.health > 0:
            enemy.attack(player)
        if cmd == 'run':
            if random.randint(0, 100) < 25:
                print("RUN AWAY!!!!!")
                print(" ----->  _0_/")
                print(" -----> / | ")
                print(" ----->  / \ ")
                return 1
    return 0


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


class Axe(Weapons):
    def __init__(self):
        super(Axe, self).__init__("Huntress Axe", 66, 568, 1, 87)

    def axe(self):
        print("You have the %s" % self.name)


class Hands(Weapons):
    def __init__(self):
        super(Hands, self).__init__("Hands", 0, 0, 1000000000, 1)


class Chainsaw(Weapons):
    def __init__(self):
        super(Chainsaw, self).__init__("Hillbilly's Chainsaw", 134, 690, 3, 200)

    def chainsaw(self):
        print("You have the %s" % self.name)


class Sniper(Weapons):
    def __init__(self):
        super(Sniper, self).__init__("Glaz's Sniper", 86, 18028, 10000, 1000)


class AssaultRifle(Weapons):
    def __init__(self):
        super(AssaultRifle, self).__init__("Fortnite Legendary Scar", 123, 8467, 10000, 100)


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Michel Myers Knife", 45, 700, 1, 27)


class Bow(Weapons):
    def __init__(self):
        super(Bow, self).__init__("Warframe Bow", 10, 267, 3, 44)


class NinjaStars(Weapons):
    def __init__(self):
        super(NinjaStars, self).__init__("Genji's Ninja Stars", 4, 409, 2, 60)


class Headphones(Weapons):
    def __init__(self):
        super(Headphones, self).__init__("My headphones", 2, 70, 1, 13)


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 2, 5, 1, 0)


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
        if armor is None:
            armor = 0
        self.armor_reduction = armor
        self.uses = uses
        self.equip = []

    def talk(self):
        print("Hello")

    def attack(self, target):
        print("%s attacks %s" % (self.name, target.name))
        target.take_damage(self.weapon.damage)

    def limit(self, inventory):
        inventory.limit = 8

    def abilities(self, limit):
        limit.abilities = 5

    def heal(self, amt):
        if apple in player.inventory:
            self.health += amt
            if self.health > 100:
                self.health = 100
            self.inventory.remove(apple)
        else:
            print("You need a apple to eat a apple -_-. So I have to say")

    def take_damage(self, dmg):
        total_dmg = dmg - self.armor_reduction
        if total_dmg < 0:
            total_dmg = 0
        self.health -= total_dmg
        if self.health < 0:
            self.health = 0

    def inventory_use(self):
        self.inventory.remove(Weapons)

    def take(self, item):
        self.inventory.append(item)


class Boss(Character):
    def __init__(self):
        super(Boss, self).__init__("Zombie", None, None, None, None, None, 10000, axe, "unlimited", None)


class Room(object):
    def __init__(self, name, north, south, east, west, description, enemies=None, items=None):
        if enemies is None:
            enemies = []
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
        self.boss = Boss
        self.item = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


apple = Apple()
axe = Axe()
chainsaw = Chainsaw()
headphones = Headphones()
knife = Knife()
door_key = DoorKey()
shed_key = ShedKey()
sniper = Sniper()
assault_rifle = AssaultRifle()
hands = Hands()
boss1 = Boss()
boss2 = Boss()

player = Character("Soul collector", "Hello", 5, [], 80, 5, 100, hands, None, None)

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
                                                 "to find a weapon. But I have to look in every room because it can\n"
                                                 " have something useful.", None, None)
hallway = Room("Hallway", None, "kitchen", "closet", "door", "I can go to the closet to the East or go to the \n"
                                                             "Kitchen to the South, or just go back to the door(West)."
                                                             "We need to go upstairs to get the key to the \n"
                                                             "shed.")
closet = Room("Closet", None, "living_room", None, "hallway", "I'm at the closet, there might be something inside, \n"
                                                              "if not I can go to the living room to the south.", None,
              [axe])
living_room = Room("Living Room", "closet", None, None, "stairs", "This place looks nice with no zombies",
                   [Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                              "An undead person that goes for \nhuman brains.")])
stairs = Room("Stairs", None, "hallway2", "living_room", "den", "We need to go upstairs to get the key to the \n"
                                                                "shed(South), there is a den to the West, there \n"
                                                                "might be something in there...")
den = Room("Den", "kitchen", None, "stairs", None, "This den is big just like my friends house.", boss2)
kitchen = Room("Kitchen", "hallway", "den", None, None, "There might be something \n"
                                                        "in here.", None, [knife, apple])
hallway2 = Room("Hallway2", "stairs", "master_Bedroom", "bathroom", "hallway3", "Where is the Key!, there is another \n"
                                                                                "hallway to the west and there is a \n"
                                                                                "bathroom to the east, or just go \n"
                                                                                "back downstairs -_-(North).",
                [Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                           "An undead person that goes for human brains."),
                 Character("Zombie", None, None, None, None, None, 100, axe, "unlimited", "An undead person that "
                                                                                          "goes for \n human brains."),
                 Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                           "An undead person that goes for \nhuman brains.")
                 ],
                [chainsaw, headphones])
hallway3 = Room("Hallway3", "room1", "room3", "hallway2", "room2", "I can go back to the second hallway to the \n"
                                                                   "West, or go to room3 to the North, \n"
                                                                   "room2 to the South or room1 to the east.")

bathroom = Room("Bathroom", None, None, None, "hallway2", "Here is the key, but WHY WAS THERE A ZOMBIE HULK \n"
                                                          "IN HERE!!!!????", [boss1], [door_key])
room1 = Room("Room1", None, "hallway3", None, None, "The key is not in here also.", None, [apple])
room2 = Room("Room2", None, None, "hallway3", None, "The key is not in here.")
room3 = Room("Room3", "hallway3", None, None, None, "The key is not in here too.", None)
master_bedroom = Room("Master_Bedroom", "hallway2", None, None, None, "The key is not in here also.")
shed_door = Room("Shed_Door", None, None, None, "hallway4", "I finally got in the shed, now I have to grab a gun.")
hallway4 = Room("Hallway4", "sniper_room", "assault_room", "shed_door", None, "There is snipers to the North \n"
                                                                              "and some assault rifles to the South.")
assault_room = Room("Assault_Room", "hallway", None, None, None, "ok, seems like going with the assault rifles.", None,
                    [assault_rifle])
sniper_room = Room("Sniper_Room", None, "hallway4", None, None, "ok, seems like going with the snipers rifles.", None,
                   [sniper])
outside = Room("Outside", None, "Shed2", "Shed_Door", None, "Ok, since I killed the zombies in the way, I can get \n"
                                                            "in the shed.",
               [Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                          "An undead person that goes for \nhuman brains."),
                Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                          "An undead person that goes for \nhuman brains."),
                Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                          "An undead person that goes for \nhuman brains."),
                Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                          "An undead person that goes for \nhuman brains."),
                Character("Zombie", None, None, None, None, None, 100, axe, "unlimited",
                          "An undead person that goes for \nhuman brains.")
                ])

directions = ['north', "n", 'south', "s", 'east', "e", 'west', "w"]
current_node = door
Items = []

if debug == 1:
    player.inventory = [door_key, shed_key]
    player.weapon = Axe()
    player.weapon.damage = 90000
while player.health > 0:
    run_cmd = 0
    if sniper in player.inventory or assault_rifle in player.inventory:
        print("You have finished part 1 of my game. GJ")
        quit(0)
    if len(current_node.enemies) > 0:
        # Enemies exist)
        while len(current_node.enemies) > 0 and player.health and run_cmd == 0:
            if debug == 1:
                print("You automatically win")
                current_node.enemies = 0
                continue
            run_cmd = fight(current_node.enemies[0])
            if run_cmd == 0:
                current_node.enemies.pop(0)
    if run_cmd == 1:
        previous_node = current_node
        while previous_node == current_node:
            try:
                direction = random.choice(directions)
                current_node.move(direction)
            except KeyError:
                pass
        continue
    print("---Health---")
    print(player.health)
    print("---Place---")
    if player.health <= 0:
        print("You have died.")
        quit(0)
    print(current_node.name)
    print(current_node.description)
    command = input('>_')
    if command == 'quit':
        quit(0)

    elif command == "scout":
        found = False
        if len(current_node.item) > 0:
            for Weapons in current_node.item:
                print(Weapons.name)
            cmd = input("Which item do you want to put in your inventory").lower()
            for Weapons in current_node.item:
                if cmd == Weapons.name.lower():
                    player.take(Weapons)
                    current_node.item.remove(Weapons)
                    found = True
                    print("You have added it to your inventory.")
            if not found:
                print("I don't see the item you are looking for here. -_-")
        else:
            print("There is nothing here. -_-")

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way. -_-")
    elif "take" in command:
        Weapons_requested = command[5:]
        for Weapons in current_node.item:
            if Weapons.name == Weapons_requested:
                player.take(current_node.item)

    elif 'equip' in command:
        found = False
        equipment_name = command[6:]
        for item in player.inventory:
            if item.name.lower() == equipment_name.lower():
                player.weapon = item
                found = True
                print("You have just equipped the %s." % Weapons.name)
                print("-----Damage-----")
                print(player.weapon.damage)
                print("----------------")
                # print("-----Durability-----")
                # print(Weapons.durability)
                # print("--------------------")
        if not found:
            print("You have to chose a weapon to equip. -_-")

    elif command == "inventory":
        for Weapons in player.inventory:
            # print(len(player.inventory))
            print("-----Inventory-----")
            print(Weapons.name)
            print("-------------------")
        if len(player.inventory) == 0:
            print("You have nothing in you inventory. -_-")

    elif command == 'use key':
        for key in player.inventory:
            if isinstance(key, Key):
                if current_node == outside and isinstance(key, ShedKey):
                    key.use()
                elif current_node == door and isinstance(key, DoorKey):
                    key.use()

        else:
            print("You don't have a key. -_-")
    elif command == "eat apple":
        if apple in player.inventory:
            player.heal(45)
        else:
            print("You don't have a apple to eat.")
    else:
        print("Command not recognized -_-, so make a command that I can recognize.")
