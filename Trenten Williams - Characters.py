# 1 Name
# 2 Move
# 3 Talk to a person
# 4 Interact(use, pick up, etc.)
# 5 Inventory
# 6 Abilities
# 8 Health
# 9 Stats Effect
# 10 Description
# 11 Dialogue
# 12 Attack
# 13 Take Damage


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


player = Character("Eren Jaeger", "Hello", 5, [], "Protection", 5, 100, "Depends on the power of the weapon", )