"""
This is the start of the MFE program for Angband created by Team 8 for
Software Engineering 1!

#for edit() function if you mess up and acidently overwrite the monster file incorrectly go to the og angband code for correct file or
contact emily for a correct copy
"""
import sys
from os import name
from pathlib import Path
from typing import List

istrue = True #added as testing revision, allows the program to contunite running until isfalse



#Monster class with list of all attributes for each monster.
class Monster:
    #Intializes all the ALL variables for the monsters.
    def __init__(self, id: str = ""):
        #updates 02/24/2025 to include all possible variables in a monsters stats
        self.name = id
        self.base = "this stat does not exist for this monster"
        self.speed = 0
        self.hitPoints = 0
        self.hearing = 0
        self.armorclass = 0
        self.sleepiness = 0

        self.experience = 0
        self.blows = ["this stat does not exist for this monster"]  # List of tuples: (attack method, effect, damage)
        self.flags = ["this stat does not exist for this monster"]  # List of strings
        self.flagOff = ["this stat does not exist for this monster"]  # List of strings
        self.descp = "this stat does not exist for this monster"
        self.rarity = 0
        self.depth = 0

        # Optional fields not in your class but from your monster list
        self.plural = "this stat does not exist for this monster"
        self.glyph = "this stat does not exist for this monster"
        self.color = "this stat does not exist for this monster"
        self.light = 0
        self.innateFreq = 0
        self.spellFreq = 0
        self.spellPower = 0
        self.spells = ["this stat does not exist for this monster"]  # List of strings
        self.messageVis = {"this stat does not exist for this monster" : "this stat does not exist for this monster"}  # Dict: spell -> message
        self.messageInvis = {"this stat does not exist for this monster" : "this stat does not exist for this monster"}  # Dict: spell -> message
        self.messageMiss = {"this stat does not exist for this monster" : "this stat does not exist for this monster"}  # Dict: spell -> message
        self.drop = ["this stat does not exist for this monster"]  # List of tuples: (item type, item name, chance, min, max)
        self.dropBase = ["this stat does not exist for this monster"]  # List of tuples: (item type, chance, min, max)
        self.mimic = ("this stat does not exist for this monster")  # Tuple: (tval, sval)
        self.friends = ["this stat does not exist for this monster"]  # List of tuples: (chance, number, name, role)
        self.friendsBase = ["this stat does not exist for this monster"]  # List of tuples: (chance, number, name, role)

    def __str__(self) -> str:
        #Return all monster stats as a formatted string.
        #updated 02/24/2025 to include all monster stats
        attrs = [
            f"name: {self.name}",
            f"plural: {self.plural}",
            f"base: {self.base}",
            f"glyph: {self.glyph}",
            f"color: {self.color}",
            f"speed: {self.speed}",
            f"hitPoints: {self.hitPoints}",
            f"hearing: {self.hearing}",
            f"armorclass: {self.armorclass}",
            f"sleepiness: {self.sleepiness}",
            f"experience: {self.experience}",
            f"blows: {self.blows}",
            f"flags: {self.flags}",
            f"flagOff: {self.flagOff}",
            f"descp: {self.descp}",
            f"rarity: {self.rarity}",
            f"depth: {self.depth}",
            f"light: {self.light}",
            f"innateFreq: {self.innateFreq}",
            f"spellFreq: {self.spellFreq}",
            f"spellPower: {self.spellPower}",
            f"spells: {self.spells}",
            f"messageVis: {self.messageVis}",
            f"messageInvis: {self.messageInvis}",
            f"messageMiss: {self.messageMiss}",
            f"drop: {self.drop}",
            f"dropBase: {self.dropBase}",
            f"mimic: {self.mimic}",
            f"friends: {self.friends}",
            f"friendsBase: {self.friendsBase}",
        ]
        return "\n".join(attrs)

class MonsterEditor:
    #Initializes filepath information to get game data.
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.monsterFile = self.filepath
        self.monsters: List[Monster] = [] #this might need to be a dic.
        self.dictwithallmonsters = {}
        if not self.monsterFile:
            raise FileNotFoundError("monster.txt not found.")



    #Parses the monster text file and compiles all the attributes for each into a Monster dictanery
    def parse_monsters(self):
        #updated 02/25/2026 to include all monster variables, before it was just updateing the name to the monster class
        #PLEASE DONT CHANGE THIS, IT TOOK ME LIKE 6 HOURS TO MAKE WORK :} if you need to change parse_monsters make a new function
        self.monsters = []
        variabledic = {
            "name": 5,
            "plural": 5,
            "base": 5,
            "glyph": 5,
            "color": 6,
            "speed": 6,
            "hitPoints": 10,
            "hearing": 8,
            "armorclass": 11,
            "sleepiness": 11,
            "light": 6,
            "depth": 6,
            "rarity": 7,
            "experience": 11,
            "blows": 10,
            "flags": 8,
            "flagOff": 8,
            "descp": 10,
            "innateFreq": 5,
            "spellFreq": 5,
            "spellPower": 5,
            "spells": 8,
            "messageVis": 10,
            "messageInvis": 10,
            "messageMiss": 10,
            "drop": 8,
            "dropBase": 8,
            "mimic": 6,
            "friends": 8,
            "friendsBase": 8
        }
        varlist = list(variabledic.keys())

        with open(self.monsterFile, 'r') as file:
            content = file.readlines()
            print("File being read")
            currentM = None

            for line in content:
                line = line.rstrip()
                if not line or line.startswith('#'):
                    continue

                # Finds a new monster in the file, letting
                if line.startswith('name:'):
                    monster_id = line[5:].strip()
                    currentM = Monster(monster_id)
                    self.monsters.append(currentM)
                    continue

                # adds to the self/__init__ thing
                if currentM:
                    for var in varlist:
                        if line.startswith(f"{var}:"):
                            value = line[len(var)+1:].strip()
                            setattr(currentM, var, value)
                            break

            #structure of the dictaneru
            """
            name: filthy street urchin
            plural: this stat does not exist for this monster
            base: townsfolk
            glyph: this stat does not exist for this monster
            color: D
            speed: 110
            hitPoints: 0
            hearing: 4
            armorclass: 0
            sleepiness: 40
            experience: 0
            blows: ['this stat does not exist for this monster']
            flags: RAND_25 | OPEN_DOOR | TAKE_ITEM
            flagOff: ['this stat does not exist for this monster']
            descp: this stat does not exist for this monster
            rarity: 2
            depth: 0
            light: 0
            innateFreq: 0
            spellFreq: 0
            spellPower: 0
            spells: ['this stat does not exist for this monster']
            messageVis: {'this stat does not exist for this monster': 'this stat does not exist for this monster'}
            messageInvis: {'this stat does not exist for this monster': 'this stat does not exist for this monster'}
            messageMiss: {'this stat does not exist for this monster': 'this stat does not exist for this monster'}
            drop: ['this stat does not exist for this monster']
            dropBase: ['this stat does not exist for this monster']
            mimic: this stat does not exist for this monster
            friends: 100:3d4:Same
            friendsBase: ['this stat does not exist for this monster']
            """

            print(f"Loaded {len(self.monsters)} monsters.")

    #Lists every Dungeon level and the monsters that begin appearing on that floor.
    def dungeonLevel(self):
        #TODO: This is where the dungeon search goes
        monDepth = {}
        for m in self.monsters:
            if m.depth not in monDepth:
                monDepth[m.depth] = []
            monDepth[m.depth].append(m)
        for depth in sorted(monDepth.keys()):
            print("=" * 45)
            print(f"Dungeon Level {depth}")
            print("=" * 45)
            for m in monDepth[depth]:
                print(f"{m.name}")
            print()

    #Code from Elyse, works my typing in part/all of monster name and getting a list of them.
    #Then you type in the monster you want to edit.
    def monsterSearch(self, search:str) -> List[Monster]:
        #TODO: This is where monster name search goes
        s = search.lower()
        for n in self.monsters:
            if s in n.name.lower():
                print(f"{n.name}")


    def edit(self):
        # TODO: This is where individual monsters will be edited
        while True:

            variabledic = {
                "name": 5,
                "plural": 5,
                "base": 5,
                "glyph": 5,
                "color": 6,
                "speed": 6,
                "hitPoints": 10,
                "hearing": 8,
                "armorclass": 11,
                "sleepiness": 11,
                "light": 6,
                "depth": 6,
                "rarity": 7,
                "experience": 11,
                "blows": 10,
                "flags": 8,
                "flagOff": 8,
                "descp": 10,
                "innateFreq": 5,
                "spellFreq": 5,
                "spellPower": 5,
                "spells": 8,
                "messageVis": 10,
                "messageInvis": 10,
                "messageMiss": 10,
                "drop": 8,
                "dropBase": 8,
                "mimic": 6,
                "friends": 8,
                "friendsBase": 8
            }
            varlist = list(variabledic.keys())

            # find the name of the monster
            isvaildname = True
            nameOfMonter = input("what is the name of the monster you wish to edit? enter n to escape: ")
            #print(nameOfMonter)
            #edited as part of testing revisions
            if nameOfMonter == "n":
                return print("all done")

            while isvaildname:
                found = False #helps determine if the entry was vaild
                for monster in self.monsters:
                    if monster.name == nameOfMonter:
                        print(nameOfMonter, "is chosen")
                        isvaildname = False #breaks while loop
                        found = True #breaks the vaild entry
                        break #termainaes the for loop early
                if not found:
                    print("not a valid monster") #asks for a vaild monster
                    nameOfMonter = input("what is the name of the monster you wish to edit? ")

            #determinds what section they want to edit
            vaildname = True
            #lets user pick there varibale change of choice
            changecharagory = input(
                "What variable would you like to change: ")
            #error checking
            while vaildname:
                if changecharagory not in varlist:
                    print("this is not an accpted variable Try again: ")
                    changecharagory = input("What variable would you like to change: ")
                    changecharagory = changecharagory.lower()
                else:
                    vaildname = False
                    print(changecharagory)

            monster_to_edit = None
            for monster in self.monsters:
                if monster.name == nameOfMonter:
                    monster_to_edit = monster
                    break

            current_value = getattr(monster_to_edit, changecharagory)
            #print(f"The current {changecharagory} for the monster {nameOfMonter} is {current_value}")
            try:
                if current_value == "this stat does not exist for this monster":
                    return print("this stat does not exist for this monster")
                else:
                    print(f"The current {changecharagory} for the monster {nameOfMonter} is {current_value}")
                    letsgo = input("would you like to continue? y/n: ")
            except:
                return print("this stat does not exist for this monster")

            if letsgo == "y":
                update = input("update: ")
            elif letsgo == "n" :
                return print("ending program")
            else:
                return print("error not y or n")

            setattr(monster_to_edit, changecharagory, update)

            change = input("WARNING!!!!! from angband monster.txt file: \n Do not modify this file unless you know exactly what you are doing, \n unless you wish to risk possible system crashes and broken savefiles.\n would you like to write this to the file? y/n: ")



            #take the name, and loop thought until we find in the parse,
            #then we pull the infomation
            #then we change the data
            #then we update it

            #changecharagory = name of the chatagory they want to change
            #nameOfMonster = name of the monster they want to change
            #parse_monster gets me the date of date catagory

            with open(self.monsterFile, "w") as file:
                for monster in self.monsters:
                    for key, value in monster.__dict__.items():

                        # Skip fake default stats
                        if value == "this stat does not exist for this monster": #excludes values that don't exist for the street urchin
                            continue

                        if value == ["this stat does not exist for this monster"]:
                            continue

                        if value == {"this stat does not exist for this monster":
                                         "this stat does not exist for this monster"}:
                            continue

                        file.write(f"{key}: {value}\n")

                    file.write("\n")

            #updated dictanery

            """
            ##name is updated, the rest remains the same
            name: stinky street urchin 
            plural: this stat does not exist for this monster
            base: townsfolk
            glyph: this stat does not exist for this monster
            color: D
            speed: 110
            hitPoints: 0
            hearing: 4
            armorclass: 0
            sleepiness: 40
            experience: 0
            blows: ['this stat does not exist for this monster']
            flags: RAND_25 | OPEN_DOOR | TAKE_ITEM
            flagOff: ['this stat does not exist for this monster']
            descp: this stat does not exist for this monster
            rarity: 2
            depth: 0
            light: 0
            innateFreq: 0
            spellFreq: 0
            spellPower: 0
            spells: ['this stat does not exist for this monster']
            messageVis: {'this stat does not exist for this monster': 'this stat does not exist for this monster'}
            messageInvis: {'this stat does not exist for this monster': 'this stat does not exist for this monster'}
            messageMiss: {'this stat does not exist for this monster': 'this stat does not exist for this monster'}
            drop: ['this stat does not exist for this monster']
            dropBase: ['this stat does not exist for this monster']
            mimic: this stat does not exist for this monster
            friends: 100:3d4:Same
            friendsBase: ['this stat does not exist for this monster']
            """

            anotherchange = input("Any more updates? y/n: ")

            if anotherchange.lower() != "y":
                break

        return print("Finished editing.")

    #This is the main start up function for the program.
    def mainMenu(self):
        print("=" * 60)
        print("Monster File Editor (MFE) for Angband")
        print("=" * 60)
        while istrue:
            try:
                #testing updated 03/30/2026 revision to include clearer navigation
                self.parse_monsters()
                print("Search monster to edit:")
                print("Type 1 to search by dungeon level, 2 to search by name, or 3 to edit monsters: ")
                searchChoice = input()
                if searchChoice == "2":
                    mSearch = input("Enter Monster Name: ")
                    self.monsterSearch(mSearch)
                elif searchChoice == "1":
                    self.dungeonLevel()
                elif searchChoice == "3":
                    self.edit()
                else:
                    print("Invalid response.")
            except Exception as e:
                print(f"Error parsing monster.txt: {e}")
                return
            #edited 03/03/2026 to revise testing
            contu = input("would you like to continue? (y/n): ")
            if contu.lower() == "n":
                break


#This function starts the program, and takes the filepath as an arg for startup.
"""
To run the program, go into the directory where this file is stored, open a
terminal, and type "python MFE.py {monster.txt filepath}, replacing the text
and brackets with the actual text filepath on your personal machine.
"""

def main():
    if len(sys.argv) != 2:
        print("Please include text file path.")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        editor = MonsterEditor(filepath)
        editor.mainMenu()
    except FileNotFoundError as e:
        print("File does not exist.")
        sys.exit(1)

main()
