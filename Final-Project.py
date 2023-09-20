#import dependencies
import time
import os
import random

#Define variables
rooms = ['Start', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'Boss']
items = {'Hat': '''This hat made of felt is a perfect choice for every adventurer. If you are
going for a peregrination, this felt hat will help you in preparing for any
weather conditions.\n''', 'Shield':'''This round shield is a perfect addition to armament. It will work well during
training and tournaments.\n''', 'Sword':'''Single handed sword, a perfect match for you.\n''', 'Goggles':'''Brass goggles with green lenses?\n''', 'Health Potion': '''A bitter red drink, tastes like a mouth full of pennies but you feel
great afterwords.\n''', 'Magic Ring':'''Wearing this ring makes you like you could slay an adult dragon!\n''', 'Key':'''Heavy Brass Key.\n'''}
monsters = {'Rabid Rat': 12, 'Goblin': 15, 'Flying Snake': 8}
player_name = 'Player'
inventory = []
userInput = 'a'
confirmDirection = 'a'
HatName = 'the Hat'
divider = '-------------------------'
current_location = 'First Room'
North = ['North', 'north', 'N', 'n']
South = ['South', 'south', 'S', 's']
East = ['East', 'east', 'E', 'e']
West = ['West', 'west', 'W', 'w']
directions = ['North', 'north', 'N', 'n', 'South', 'south', 'S', 's', 'East', 'east', 'E', 'e', 'West', 'west', 'W', 'w']
Yes = ['Yes', 'yes', 'Y', 'y']
No = ['No', 'no', 'N','n']
Yes_no = ['Yes', 'yes', 'Y', 'y', 'No', 'no', 'N','n']
player_HP = 30
boss_HP = 30
boss_block = False
boss_attack = False
player_attack = False
boss_lock = True
first_entry = True
fight = ['Attack', 'A', 'a', 'Block', 'B', 'b']
attack = ['Attack', 'A', 'a']
block = ['Block', 'B', 'b']
d4 = random.randint(1, 4)
d6 = random.randint(1, 6)

#header function
def header():
    print('\n')
    print('{} is in {}.'.format(player_name, current_location))
    print('Inventory: ', inventory)
    print(divider)

#sleep function
def sleep():
    time.sleep(1)

#inventory management    
def view_inventory():
    global userInput
    header()
    print('Current Inventory: ', inventory)
    userInput = input('Which item would you like to inspect? ')
    if userInput in items:
        if userInput in inventory:
            print(items[userInput])
        else:
            print('Did you pickup that item yet?')
    else:
        print('Item not found. Typo?')


#get direction to travel prior to activating inventory
def get_directions_no_inventory ():
    global userInput
    userInput = input('\nWhere do you want to go? North, South, East, or West? ')
    return userInput

#get direction to travel.
def get_directions ():
    global userInput
    userInput = input('\nWhere do you want to go? North, South, East, or West? or i for Inventory: ')
    if userInput == 'i':
        view_inventory()
    else:
        return userInput

#boss battle
def boss_battle():
    global userInput
    global player_name
    global player_HP
    global boss_HP
    global boss_block
    global boss_attack
    global d4
    global d6
    damage_done = 0
    rounds = 0
        #battle here
    while boss_HP > 0:
        if player_HP > 0:
            d4 = random.randint(20, 20)
            d6 = random.randint(1, 6)   
            rounds += 1
            userInput = input('Attack or Block? a or b ')
            boss_block = bool(random.getrandbits(1))
            boss_attack = bool(random.getrandbits(1))
            # damage_done = d6
            print(rounds)
            if userInput in attack:
                if boss_block is True:
                    print('The Psuedolich blocked the attack.')
                else:
                    boss_HP = boss_HP - d6
                    print('You struck Psuedolich caused {} point\'s of damage. He has {} HP.'.format(d6, boss_HP))
                    if boss_attack is True:
                        player_HP = player_HP - d4
                        print('The Psuedolich struck you for {} damage. You have {} HP'.format(d4, player_HP))
            elif userInput in block:
                if boss_block is True:
                    print('both blocked')
                else: 
                    print('You blocked the Psuedolich attack.')
            # else:
            #     pass
        else:
            print('player died')
            return





#room 1
def r1():
    global directions
    global current_location 
    global inventory 
    global userInput
    global HatName
    global player_name
    current_location = 'First Room'
    header()
    if 'Hat' in inventory:
        print('This the the room you retrieved the hat. Nothing else to see here.')
    else:
        print('''As you approach the door to the south, it almost sounds like someone
or was it some thing speaking?!\n
Pulling open the door you are greeted with a long room, maybe 40ft in length.
In the center of the room there is a round stone column, upon which sits a hat.''')
    while 'Hat' not in inventory:
        userInput = input('\nWould you like to take the hat? ')
        while userInput not in Yes:
                print('Take the Hat.')
                userInput = input('\nWould you like to take the hat? ')
        inventory.append('Hat')
        header()
        print('Added Sentient Hat to Inventory.\n')
        print('You can now access your inventory using \'i\' when asked where to go.\n')
        # print('Inventory: ', inventory) 
        print('\"Hello\"?')
        print('''\"Well, it\'s been quite some time since someone wore me! I suppose
I should introduce myself.\"\n''')
        HatName = input('Name the hat: ')
        HatName = HatName + ' The Hat'
        print('\"My name is {}, in case you have not figured it out already, I\'m alive!\"\n'.format(HatName))
        player_name = input('\"What\'s your name? ')
        header()
        print('\"Well {}, I\'m really glad you found me. Lets go!\"'.format(player_name))
    print('''\nThere is a door to the east, and a door to the south.''')
    get_directions()
    while userInput not in directions:
        get_directions()
    if userInput in North:
        current_location = 'Start Room'
    elif userInput in South:
        current_location = 'Second Room'
    elif userInput in East:
        current_location = 'Third Room'
    else:
        current_location = 'First Room'
    return current_location

#room 2
def r2():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Second Room'
    header()
    if 'Shield' in inventory:
        print('This the the room you retrieved the shield. Nothing else to see here.')
    else:
        print('''You approach the door to the south and pass through it, fining yourself in a square
room. Looking around the room, you find little of interest. As you turn to leave
something catches your eye. There appears to be a shield sitting in the corner!''')
    while 'Shield' not in inventory:
        userInput = input('\nWould you like to take the Shield? ')
        while userInput not in Yes:
                print('Take the Shield.')
                userInput = input('\nWould you like to take the Shield? ')
        print('Added Shield to Inventory.\n')
        header()
        inventory.append('Shield')
        print('Inventory', inventory)
    print('As you look around the room, you see the only door is to the north.')
    get_directions()
    while userInput not in North:
        print('The only door is in the north.')
        get_directions()
    if userInput in North:
        current_location = 'First Room'
    return current_location

#room 3
def r3():
    global directions
    global current_location 
    global inventory 
    global userInput
    global boss_lock
    global first_entry
    current_location = 'Third Room'
    header()
    if first_entry is False:
        print('This the the room where you retrieved the sword.\n')
        if 'Key' not in inventory:
            if len(inventory) < 7:
                    print('{} says, \"I don\'t think you\'ve gathered enough equipment to defeat the boss.\"\n'.format(HatName))
            else:
                print('{} says, \"I hope you still have the key for that big door to he south...'.format(HatName))
    else:
        print('''As you enter the chamber you discover the ceiling is quite high. You get the
feeling this is the central chamber. You notice there are 4 doors in this room,
one in each of the cardinal directions. In the center of the room is a massive
stone altar. Draped in black cloth, something glints at you in the torch light...''')
        first_entry = False
    while 'Sword' not in inventory:
        userInput = input('\nWould you like to take the Sword? ')
        while userInput not in Yes:
                print('Take the Sword.')
                userInput = input('\nWould you like to take the Sword? ')
        header()
        print('Added Sword to Inventory.\n')
        inventory.append('Sword')
    print('''Their are four doors in this room, one in each direction. The doors to the south 
are massive.\n''')
    if len(inventory) >= 7:
        print('''You walk over to the large doors on the south wall, insert the key and with a 
stiff twist, you hear a loud \"CLICK\".''')
        boss_lock = False
    if boss_lock is True:
        print('The big double doors are still locked.')
    else:
        print('Door UNLOCKED!')
    get_directions()
    while userInput not in directions:
        get_directions()
    if userInput in North:
        current_location = 'Forth Room'
    elif userInput in South:
        if boss_lock == False:
            current_location = 'Boss Room'
        else:
            print('The door is locked.')
    elif userInput in East:
        current_location = 'Sixth Room'
    elif userInput in West:
        current_location = 'First Room'
    return current_location

#room 4
def r4():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Forth Room'
    header()
    if 'Goggles' in inventory:
        print('''This the the room you found the goggles. Nothing else to see
here aside from the skeleton still sitting in the corner.''')
    else:
        print('''Entering the next room you find it much like the others. But is there any
treasure?''')
        print('''EEK!\n''')
        print('''As you struggle to get your blood pressure back down it\s starting to make
sense. Of course there are skeletons in here... It's a dungeon. Examining the
skeleton there isn\'t much to see, except the goggles sitting on it\'s forehead.''')
        print('\"Oooo shinney!\", says {}'.format(HatName))
    while 'Goggles' not in inventory:
        userInput = input('\nTake the Goggles? ')
        while userInput not in Yes:
            print('{} really wants you to take the Goggles.'.format(HatName))
            userInput = input('\nTake the Goggles? ')
        inventory.append('Goggles')
        header()
        print('Added Goggles to Inventory.\n')
    print('There is a door to east, and a door to the south.')
    get_directions()
    while userInput not in directions:
        print('The only doors are in the East and South.')
        get_directions()
    if userInput in South:
        current_location = 'Third Room'
    elif userInput in East:
        current_location = 'Fifth Room'
    else:
        print('The only doors are in the East and South.')
    return current_location

#room 5
def r5():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Fifth Room'
    header()
    if 'Health Potion' in inventory:
        print('This the room you got the potion. Nothing else to see here.')
    else:
        print('''Another dead end... Maybe there is some treasure here too? Looking around there
is a small wooden chest on the floor. You think to yourself, this could be
great... or not...''')
        print('You open the chest.')
        while 'Health Potion' not in inventory:
            userInput = input('\nShall we grab the health potion? ')
            while userInput not in Yes:
                    print('{} really thinks you\'ll need it later, better take it.'.format(HatName))
                    userInput = input('\nShall we grab the health potion? ')
            inventory.append('Health Potion')
            header()
            print('Added Health Potion to Inventory.\n')
        print('There is nothing else of interest in this room.')
        print('The only door is to the west.')
    get_directions()
    while userInput not in West:
        print('The only door is in the west.')
        get_directions()
    if userInput in West:
        current_location = 'Forth Room'
    return current_location

#room 6
def r6():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Sixth Room'
    header()
    if 'Magic Ring' in inventory:
        print('This the room you found the ring. Nothing else to see here.')
    else:
        if 'Goggles' not in inventory:
            print('Great, completely empty. Total disappointment just like mother said.')
        else:
            print('''Coming into yet another room, you see absolutely nothing... It\'s completely
empty. Well that\'s kind of disappointing isn\'t it? Hold on, how about those
goggles? We haven\'t used them yet. You slide on the goggles and aside from a
bit of a funky smell you see a glow in the far corner of the room! As you walk
over you discover the room isn\'t the disappointment your mother always said
you would be!''')
            while 'Magic Ring' not in inventory:
                userInput = input('\nYou found a ring, pick it up? ')
                while userInput not in Yes:
                        print('Are we still doing this? Just type yes already.')
                        userInput = input('\nPick up the ring? ')
                header()
                print('Added Ring to Inventory.\n')
                inventory.append('Magic Ring')
                print('''Magic Ring?! As you examine it further, the ring is a thin gold band with a
solitary jet black stone set on it. As you slide the ring on your finger feel 
you strong. Strong enough to kill a dragon!''')
    print('There is a door to the west and the south.')
    get_directions()
    while userInput not in directions:
        get_directions()
    if userInput in North:
        print('The only doors are to the west and the south.')
    elif userInput in South:
        current_location = 'Seventh Room'
    elif userInput in West:
        current_location = 'Third Room'
    else:
        print('The only doors are to the west and the south.')
    return current_location

#room 7
def r7():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Seventh Room'
    header()
    if 'Key' in inventory:
        print('This is the cluttered room where you found the key.')
    else:
        print('''As you walk into what seems like the millionth room you finally discover where
all the stuff went. Dungeons are supposed to have lots of stuff right? Well
here it is. You gaze upon an absolute mountain of things.\m''')
        print('\"That is one big pile of junk. Who saves this kind of stuff?\" says {}.'.format(HatName))
        print('''He right and you know it, the treasure trove you were hoping to find just isn\'t
here... All this exploring and it ends with junk. Papers, packing material,
broken chairs...''')
        print('\n\"Look at this!\" says {}. "Who would save a broken ladle? What good is that?\"'.format(HatName))
        if 'Goggles' in inventory:
            print('''You might was well poke around a little to see if something of value remains. Oh!
the goggles! Let\'s try those again. Slipping the goggles back on you see a
faint glow under what must be a literal ton of old furniture. After quite
a long time digging through you find an cabinet at the bottom of the pile.
Pulling one of the drawers you finally found something! ''')
            while 'Key' not in inventory:
                userInput = input('\nYou found a heavy key, you take it.')
                inventory.append('Key')
                header()
                print('Added Key to Inventory.\n')
            print('''\nDigging yourself back out of the pile you find yourself standing back by the
door on the north wall.''')
        else:
            print('\nYou\'ll never find anything in this mess with out some help.')
            print('Better come back later... The only door is to the north.')
    get_directions()
    while userInput not in North:
        print('The only door is in the north.')
        get_directions()
    if userInput in North:
        current_location = 'Sixth Room'
    else:
        print('The only door is in the north.')
    return current_location

#define win function
def Win():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Boss Room'
    print('\n\nCongratulations. You won.\n\n')
    quit()

#boss room
def Boss():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Boss Room'
    header()
    print('''As you lean into the doors with both hands they easily swing outward into a the
new room. You find yourself in a moderately furnished room of simple 
accommodations. Near the center of the room, a figure sits at an old wooden
table dutifully mixing a small bowl. Just then, as if it could feel your gaze,
or perhaps it noticed the torch light, the creature stood and faced you leaving
the bowl on the table.\n

What stands before you kind of looks like a zombie. But something
isn\'t quite right... The face, the face has a look of intelligence... ''')

    boss_battle()
    if player_HP > 0:
        print('''You leap forward drawing your sword and killing it with one final stroke.''')
    else:
        print('''In a brutal blow the Psuedolich finishes you off. You have died. What will
become of your body I wonder?''')
    quit()

#dungeon exit
def ExitDungeon():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Ruins'
    print('You have exited dungeon.')
    if 'Hat' in inventory:
        print('{} says, "Well, at least you\'ve still got me!'.format(HatName))
        print('Shall we go find another adventure?')
    else:
        print('You have a nagging feeling you missed something...')
        userInput = input('\nWant to go back in? y or n: ')
        if userInput == 'y':
            start_room()
        else:
            print('I hope you enjoyed this game. Created by Hiroshi Thomas for IT-140 SNHU 22EW2.')
            print('Thank you Prof. Hogdon.')
            quit()

#start room
def start_room():
    global directions
    global current_location 
    global inventory 
    global userInput
    current_location = 'Dungeon Entrance'
    header()
    print('''The room is constructed of rough stone masonry walls, ceiling, and floor.
Cobwebs here and there, the occasional shred of cloth or discarded trash
litter the floor. The stale smell of damp fills your nostrils as you take
in your surroundings. What\'s this? Another door?\n
There is door to the north which leads back to the outside world
and a door to the south that leads deeper into the dungeon.''')
    while userInput not in South:
        get_directions_no_inventory()
        if userInput in North:
            confirmDirection = input('Do you really want to EXIT the dungeon? y or n: ')
            if confirmDirection == 'y':
                ExitDungeon()
        elif userInput in East:
            print('You just see more of the same kind of stone wall.')
        elif userInput in West:
            print('You just see more of the same kind of stone wall.')

        elif userInput in South:
            current_location = 'First Room' 

#main function
if __name__ == "__main__":
    while True:
        current_location = 'Dungeon Entrance'
        header()
        print('''While exploring local ruins you stumble across a wooden doorway. The door
it\'s self is not unexpected or out of place, but as you inspect it there
is something unusual… Looking down, the dirt which should be undisturbed
looks as though something has been dragged across it. As if the door has
recently been opened… Do you dare enter? These ruins are supposed to be
abandoned. Nothing lives out here anyway. There is no food or water nearby.
You\'ve barely seen any living creatures. Even the ever-present rats seem to
be absent. Of course, you didn\'t come out here for a stroll. You\'re looking
for treasure after all. You easily pull the door open and peer inside, it\'s
dark… very dark. As you strike a torch and step inside you can finally see
what\'s been behind the door…''')
        userInput = input('\nReady for the adventure to start? y or n: ')
        while userInput not in Yes_no:
            print('You must choose Yes or No.')
            userInput = input('\nReady for the adventure to start? y or n: ')
        if userInput in No:
            quit()
        if userInput in Yes:
            start_room()
        while player_HP > 0:

            #room movement based on called current_location name
            if current_location == 'Dungeon Entrance':
                start_room()
            elif current_location == 'First Room':
                r1()
            elif current_location == 'Second Room':
                r2()
            elif current_location == 'Third Room':
                r3()
            elif current_location == 'Forth Room':
                r4()
            elif current_location == 'Fifth Room':
                r5()
            elif current_location == 'Sixth Room':
                r6()
            elif current_location == 'Seventh Room':
                r7()
            elif current_location == 'Boss Room':
                Boss()
            else:  
                print("Error Exit")
                ExitDungeon()
        print('You Died')

