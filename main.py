import random as r
from crafting import craftingfunc
from Enemies import mob
from playerClasses import character
from combat import battleStuff
from randomRoom import roomStuff
stepsLeft = 7
classes = [   
        {
        "name":"Melee",
        "HP":80,
        "maxHP":80,
        "speed":80,
        "attack":120,
        "defense":80,
        "evasiveness":0.99,
        "inventory": [],
        "equipped": ["Basic Sword"],
        "moves": ["Sword Slash"]
    },
        {
        "name":"Tank",
        "HP":120,
        "maxHP":120,
        "speed":60,
        "attack":100,
        "defense":120,
        "evasiveness":1,
        "inventory": [],
        "equipped": ["Giant Fists","Basic Armor"],
        "moves": ["Giant Punch"]
    },
        {
        "name":"Assasin",
        "HP":60,
        "maxHP":60,
        "speed":120,
        "attack":110,
        "defense":60,
        "evasiveness":0.85,
        "inventory": [],
        "equipped": ["Basic Dagger"],
        "moves": ["Stab"]
    }
]
bosses = [
    {
        "name":"Giant Zombie",
        "text":"You hear growling coming from door ",
        "type":"Encounter",
        "mob":"Giant Zombie"
     },
     {
         "name":"Damien",
         "Text":"You hear absolutly nothing from door ",
         "type":"Other",
         "mob":None
     }
]
rooms = [
    {
        "name":"Zombie Room",
        "encounter":"Zombie",
        "reward":["coins","Leather Chestplate","Leather Leggings","Leather Boots","Health Charm"]
    },
    {
        "name":"Vampire Room",
        "encounter":"Vampire",
        "reward":["coins","Leather Chestplate","Iron Leggings","Iron Boots","Speed Charm"]
    },
    {
        "name":"Skeleton Room",
        "enounter":"Skeleton",
        "reward":["coins","Leather Chestplate","Leather Leggings","Leather Boots","Damage Charm"]
    }
]
mobs = [
    {
        "name": "Zombie",
        "hp":r.randint(50,70), 
        "attack":r.randint(4,7), 
        "mob_name": r.choice([
        "Shambling Corpse","Rotwalker","Graveborn","Fleshdragger","Mudclaw","Hollow One","Graveshuffler","Rotting Husk","Bonechewer","Ashen Dead"]), 
        "lootdrops":r.choice(["Flesh","Iron","Zombie Head", "Leather Chestplate"]), 
        "speed":r.randint(1,2), 
        "defense":r.randint(2,6),
        "evasiveness":1,
        "chance":r.randint(1,4),
        "debuff": None,
        "debuffmulti": 1,
        "moves":["Bite","Bad Breath"]
    },
    {
        "name": "Vampire",
        "hp":r.randint(60,100), 
        "attack":r.randint(3,6), 
        "mob_name": r.choice(["Draven", "Lilith", "Lucien", "Nyx", "Vesper"]), 
        "lootdrops":r.choice(["Vampire Essence","Vampire Essence","Silver helment", "Silver Leggings", "Silver Chestplate"]), 
        "speed":r.randint(4,7), 
        "defense":r.randint(1,4),
        "evasiveness":0.9,
        "chance":r.randint(1,6),
        "debuff": None,
        "debuffmulti": 1,
        "moves":["Bite","Blood Shot"]
    },
    {
    "name": "Skeleton",
        "hp":r.randint(30,50), 
        "attack":r.randint(5,9), 
        "mob_name": r.choice(["Rattlebone", "Graveclatter","Bonewalker","Dustmarrow","Crypt Rattler"]), 
        "lootdrops":r.choice(["Bones","Chainmail ""Skeleton head","Goggles"]), 
        "speed":r.randint(2,3), 
        "defense":r.randint(1,4),
        "evasiveness":1,
        "chance":r.randint(1,5),
        "debuff": None,
        "debuffmulti": 1,
        "moves":["Bone Bash","Arrow"]
    }
]
moves = [
    {
        "name":"Bite",
        "dmg":20,
        "accuracy":1,
        "type":"undead",
        "heal":10,
        "attackChangeS":None,
        "attackChangeE":None,
        "defenseChangeS":None,
        "defenseChangeE":None,
        "speedChangeS":None,
        "speedChangeE":None
    },
        {
        "name":"Basic Sword",
        "dmg":30,
        "accuracy":1,
        "type":"normal",
        "heal": None,
        "attackChangeS":None,
        "attackChangeE":None,
        "defenseChangeS":None,
        "defenseChangeE":None,
        "speedChangeS":None,
        "speedChangeE":None
    }
]
classNames = []
for i in range(len(classes)):
    classNames.append(classes[i]["name"])

name = input("What is your name?")
chosenClass = input(f"What class are you?{classNames} ")
for I in range(len(classes)):
    for i in range(len(classes)):
        if classes[i]["name"] == chosenClass:
            chosenData = classes[i]
            player = character(name,chosenData["HP"],chosenData["speed"],chosenData["attack"],chosenData["defense"],chosenData["evasiveness"],chosenData["inventory"],chosenData["equipped"],chosenData["moves"])

