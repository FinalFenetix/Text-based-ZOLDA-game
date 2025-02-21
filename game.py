import random

class Entity:
    def __init__(self, name, damageLow, damageHigh, health, inventory, itemEquipped):
        self.name = name
        self. damageLow = damageLow
        self.damageHigh = damageHigh
        self.health = health
        self.inventory = inventory
        self.itemEquipped = itemEquipped

    def attack(self):
        damageDealt = random.randint(self.damageLow, self.damageHigh)
        return damageDealt