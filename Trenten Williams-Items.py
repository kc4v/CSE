class Item(object):
    def __init__(self, name, weight, value, durability):
        self.name = name
        self.weight = weight
        self.value = value
        self.durability = durability

    def picked_up(self):
        print("You picked up %s" % self.name)


class Weapons(Item):
    def __init__(self, name, weight, value, durability, damage):
        super(Weapons, self).__init__(name, weight, value, durability)
        self.damage = damage

    def attack(self):
        print("You attacked the target and did %s" % self.damage)


class Consumable(Item):
    def __init__(self, name, weight, value, durability):
        super(Consumable, self).__init__(name, weight, value, durability)

    def eat(self):
        print("You are able to eat the %s" % self.name)


class Clothing(Item):
    def __init__(self, name, weight, value, durability, damage_resistant):
        super(Clothing, self).__init__(name, weight, value, durability)
        self.damage_resistant = damage_resistant

    def wear(self):
        print("The clothing protected you and it did %s" % self.damage_resistant)


class Potion(Item):
    def __init__(self, name, weight, value, durability, heal):
        super(Potion, self).__init__(name, weight, value, durability)
        self.heal = heal

    def drink(self):
        print("You can drink the %s potion" % self.name)


class Backpack(Item):
    def __init__(self, name, weight, value, durability, stored_items):
        super(Backpack, self).__init__(name, weight, value, durability)
        self.stored_items = stored_items

    def open(self):
        print("Shows every %s" % self.stored_items)


class Throwable(Item):
    def __init__(self, name, weight, value, durability):
        super(Throwable, self).__init__(name, weight, value, durability)

    def throw(self):
        print("If u want to, you can throw this %s" % Throwable)


class Drop(Item):
    def __init__(self, name, weight, value, durability):
        super(Drop, self).__init__(name, weight, value, durability)

    def discard(self):
        print("You have dropped %s" % Drop)


class Combination(Item):
    def __init__(self, name , weight, value, durability):
        super(Combination, self).__init__(name, weight, value, durability)

    def combine(self):
        print("You have created %s" % Combination)


class Axe(Item):
    def __init__(self, name, weight, value, durability):
        super(Axe, self).__init__("Huntress Axe", "86 pounds", "$500,900", "55/55")

    def Axe(self):
        print("You have the %s" % Axe)


class Chainsaw(Item):
    def __init__(self, name, weight, value, durability):
        super(Chainsaw, self).__init__("Hillbillys Chainsaw", "134 pounds", "$690,040", "87/87")

    def Chainsaw(self):
        print("You have the %s" % Chainsaw)


class Knife(Item):
    def __init__(self, name, weight, value, durability):
        super(Knife, self).__init__("Michel Myers Knife", "45 pounds", "$4,002", "69/69")