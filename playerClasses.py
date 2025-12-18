class player:
    def __init__(self,name,HP,speed,attack,defense,evasiveness,inventory,equipped,moves):
        self.HP = HP
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.evasiveness = evasiveness
        self.inventory = inventory
        self.equippted = equipped
        self.moves = moves
        self.name = name
    def returnStats(self):
        stats = {
            "attack":self.attack,
            "defense":self.defense,
            "speed":self.speed,
            "evasiveness": self.evasiveness
        }
        return stats

name = input("What is your name?")
chosenClass = input("What class are you?")
    