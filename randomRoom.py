import random as rand
stepsLeft = 7
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
class roomStuff:
    def randomiseRooms():
        roomTypes = []
        bossText = []
        bossList = []
        for i in range(4):
            seed = rand.randint(1,10)
            if seed == 1:
                roomTypes.append("Boss")
                bossChosen = bosses[rand.randint(0,len(bosses)-1)]
                bossText.append(f"{bossChosen["text"]} {i}")
                bossList.append(bosses[rand.randint(0,len(bosses)-1)]["name"])
            elif seed == 2:
                roomTypes.append("Crafting")
                bossList.append(None)
            elif seed == 3:
                roomTypes.append("Shop")
                bossList.append(None)
            else:
                roomTypes.append("Encounter")
                bossList.append(None)
        correctRoom = rand.randint(1,4)
        return roomTypes, correctRoom, bossText,bossList
    def chooseRooms():
        global stepsLeft
        roomTypes, correctRoom,bossText,bossList = roomStuff.randomiseRooms()
        for i in range(len(bossText)):
            print(bossText[i])
        choseRoom = False
        options = ["1","2","3","4"]
        while choseRoom == False:
            chosenRoomNum = input("Chose a room (1,2,3,4)")
            if chosenRoomNum in options:
                choseRoom = True
        if chosenRoomNum == correctRoom:
            stepsLeft = stepsLeft - 1
        chosenRoom = roomTypes[chosenRoomNum-1]
        if chosenRoom == "Boss":
            chosenRoom = bossList[chosenRoomNum-1]
        return chosenRoom
        

