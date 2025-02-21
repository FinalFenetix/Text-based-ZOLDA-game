import random
import os
import time


def clear_console():
    # Clear console based on the operating system
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/Mac

class Entity:
    def __init__(self, name, damageLow, damageHigh, health, inventory, itemEquipped):
        self.name = name
        self. damageLow = damageLow
        self.damageHigh = damageHigh
        self.health = health
        self.inventory = inventory
        self.itemEquipped = itemEquipped
        self.abilityEquipped = 'King of Spades'

    def attack(self):
        damageDealt = random.randint(self.damageLow, self.damageHigh)
        return damageDealt
    
    def heal(self, item):
            if item.lower() == '1':
                clear_console()
                print('You ate an apple and gained +5hp!')
                return 5
                
            if item.lower() == '2':
                clear_console()
                print('You ate an entire steak and gained +15hp!')
                return 15
    
    def abilityAttack(self):
        koslist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if self.abilityEquipped == 'King of Spades':
            randomChance = random.randint(1, 10)
            clear_console()
            abilityInput = input('King of Spades activated! \n Pick a number from 1 - 10 \n ||: ')
            while abilityInput not in koslist:
                clear_console()
                abilityInput = input('Thats not an option, try again \n Pick a number from 1 - 10 \n ||: ')
            
            abilityInput = int(abilityInput)

            if abilityInput == randomChance:
                return True
            else:
                return False


test = Entity('Test', 3, 10, 20, ['stick', 'fists', 'apple', 'steak'], 'fists')
test.abilityAttack()