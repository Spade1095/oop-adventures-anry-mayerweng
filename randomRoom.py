import random as rand
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
class rooms:
    def randomiseRooms():
        roomTypes = []
        bossText = []
        for i in range(4):
            seed = rand.randint(1,10)
            if seed == 1:
                roomTypes.append("Boss")
                bossText.append(f"{bosses[rand.randint(0,len(bosses)-1)]["text"]} {i}")
            elif seed == 2:
                roomTypes.append("Crafting")
            elif seed == 3:
                roomTypes.append("Shop")
            else:
                roomTypes.append("Encounter")
        correctRoom = rand.randint(1,4)
        return roomTypes, correctRoom, bossText
    def chooseRooms():
        roomTypes, correctRoom,bossText = rooms.randomiseRooms()
        for i in range(len(bossText)):
            print(bossText[i])
        choseRoom = False
        options = ["1","2","3","4"]
        while choseRoom == False:
            chosenRoom = input("Chose a room (1,2,3,4)")
            if chosenRoom in options
