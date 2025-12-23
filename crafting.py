
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



def checkcraft():
       can_craft = None
       for item in player_invetory:
            if item in player_invetory:
                can_craft = True
            else:
                can_craft = False
                  
                  
checkcraft()