
player_invetory =["Iron", "Iron"]
crafting_recipes = [
    
        {"item":"Iron Sword",
          "recipe":"Iron "*2},
        {"item":"Blood Wand", 
         "recipe": "Vampire Essense "*5},
        {"item":"Blood Sword", 
         "recipe":"Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Iron, Iron"},
        {"item":"Vampire Mask",
         "recipe":"Vampire Essence, Vampire Essence, Bones, Bones, Bones"}
        ]


class craftingfunc():
    def __init__(self, item_input):

        self.chosen_item = None



        self.recipes =[
    
        {"item":"Iron Sword",
          "recipe":"Iron "*2},
        {"item":"Blood Wand", 
         "recipe": "Vampire Essense "*5},
        {"item":"Blood Sword", 
         "recipe":"Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Vampire Essense, Iron, Iron"},
        {"item":"Vampire Mask",
         "recipe":"Vampire Essence, Vampire Essence, Bones, Bones, Bones"}
        ]


    def inputmats(self)

    def checkcraft(self, desired_item):
        for recipes in self.recipes:
            if self.recipes["item"].lower() == desired_item.lower():
                self.chosen_item = recipes["item"]
            if self.chosen_item == None:
                return
            





           

