import random

debuff = [
    {"debuff":"light", "multiplyer":0.8}
    ]



class Undead:
    debuffactive = True
    if debuffactive == False:
        debuffmulti = 1
    else:
        debuffmulti = debuff[0]["multiplyer"]

class Zombie(Undead):
    def __init__(self):
        self.level = random.randint(1, 6)
        self.name = "Young Zombie"
        self.health = int(100 * (self.level * .40))
        self.attack = 4 + self.level
        self.speed = self.level
        self.defense = int(3 * self.level * self.debuffmulti)

    def display(self):
        print(self.health)
        print(self.defense)
       
zombie = Zombie()
zombie.display()
