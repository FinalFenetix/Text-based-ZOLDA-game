import random
import os
import time


def clear_console():
    # Clear console based on the operating system
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/Mac

def cPrint(text, delay):
    clear_console()
    print(text)
    time.sleep(delay)

def cInput(text, delay):
    clear_console()
    return input(text)
    time.sleep(delay)

def ChoiceList(list, range):
    print('NOTE: Use numbers to complete questions and actions')
    for i in list:
        print(i)
    choice = ''
    choice = input('||: ')
    while choice not in range:
        print('That isnt a valid option, sorry.')
        choice = input('||: ')

    return choice
    


class Entity:
    def __init__(self, name, damageLow, damageHigh, health, inventory, itemEquipped):
        self.name = name
        self. damageLow = damageLow
        self.damageHigh = damageHigh
        self.health = health
        self.inventory = inventory
        self.itemEquipped = itemEquipped
        self.abilityEquipped = ''

    def attack(self):
        damageDealt = random.randint(self.damageLow, self.damageHigh)
        return damageDealt
    
    def heal(self, item):
            if item == '1':
                clear_console()
                print('You ate an apple and gained +5hp!')
                return 5
                
            if item == '2':
                clear_console()
                print('You ate an entire steak and gained +15hp!')
                return 15

            print(f'{self.name}s current health: {self.health}')
    
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
    
    def statCheck(self, enemy):
        clear_console()
        print(f'{Player.name}s health: {Player.health} \n{enemy.name} health: {enemy.health}')
        print(f'Inventory: {Player.inventory}')
        print(f'Current item equipped: {Player.itemEquipped}')
        print(f'{Player.name} damage low to high: {Player.damageLow} - {Player.damageHigh}')
        print(f'{enemy.name} damage low to high: {enemy.damageLow} - {enemy.damageHigh}')


gameState = ''
turn = True
Player = Entity('Leank', 3, 10, 20, ['stick', 'fists', 'apple', 'steak'], 'fists')
trainingDummy = Entity('Training Dummy', 1, 3, 10, ['fists'], 'fists')

def startUp():
    gameState = 'startUp'
    cPrint('Welcome to The Legend of Zolda!', 3)
    Player.name = cInput(f'Your current name is {Player.name}. What do you want your new name to be? \n ||: ', 1)
    cPrint(f'Welcome {Player.name}, I trust that your slumber has made you forget your fighting capabilities, no?', 1)
    pChoice = ChoiceList(['1. Yes', '2. No'], ['1', '2'])
    
    if pChoice == '1':
        tutorial()
    
    else:
        #game()
        pass

def tutorial():
    cPrint(f'Lets see how much you remember, {Player.name}!', 2)
    global turn
    while turn:
        pChoice = ChoiceList(['1. Attack', '2. Stat check', '3. Change item', '4. heal'], ['1', '2', '3', '4'])
        if pChoice == '1':
            damage = Player.attack()
            trainingDummy.health -= damage
            cPrint(f'You hit {trainingDummy.name} for {damage} damage! \n{trainingDummy.name} health: {trainingDummy.health}', 2)
            turn = False
        
        if pChoice == '2':
            Player.statCheck(trainingDummy)

        if pChoice == '3':
            pass

        if pChoice == '4':
            if 'apple' in Player.inventory or 'steak' in Player.inventory:
                Player.heal(ChoiceList(['1. apple', '2. steak'], ['1', '2']))
                turn = False
            
            else:
                cPrint('You dont have any health consumables!', 2)

startUp()