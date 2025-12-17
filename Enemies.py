




class Undead:
    def __init__(self,debuffs):
        self.debuffs = debuffs
        print(debuffs)

class Zombie(Undead):

    def __init__(self, debuffs):
        super.__init__(self, debuffs)


print(Undead("Bob", "Fire"))
