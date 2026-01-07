from Enemies import mob 
from playerClasses import character
import random as rand
moves = [
    {
        "name":"Bite",
        "dmg":20,
        "accuracy":1,
        "type":"undead"
    },
        {
        "name":"Basic Sword",
        "dmg":30,
        "accuracy":1,
        "type":"normal"
    },
]
def playerAttack(playerMoves,playerStats,enemieStats,enemie):
    for i in range(len(playerMoves)):
        print(f"{i+1}: {playerMoves[i]}")
    chosenMove = int(input("Chose a move!(A number pls dont break my code ill fix this later) "))
    chosenMove = playerMoves[chosenMove - 1]
    for i in range(len(moves)):
        if moves[i]["name"] == chosenMove:
            move = moves[i]
    chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
    dmg = round(move["dmg"] * playerStats["attack"]/enemieStats["defense"],1)
    if rand.randint(1,100) < chanceToHit:
        print(f"You used {move["name"]}!")
        print(f"{enemie.returnName()} is at {enemie.returnHP()} HP")
        enemie.doDamage(dmg)
    return enemie
def enemieAttack(enemieMoves,playerStats,enemieStats,player):
    chosenMove = rand.choice(enemieMoves)
    for i in range(len(moves)):
        if moves[i]["name"] == chosenMove:
            move = moves[i]
    chanceToHit = move["accuracy"] * enemieStats["evasiveness"] * 100
    dmg = round(move["dmg"] * enemieStats["attack"]/playerStats["defense"],1)
    if rand.randint(1,100) < chanceToHit:
        print(f"You were attacked with {move["name"]}")
        print(f"You are at {player.returnHP()} HP")
        player.doDmg(dmg)
    return player
def battle(enemie,player):
    enemieStats = enemie.returnStats()
    playerStats = player.returnStats()
    enemieMoves = enemie.returnMoves()
    playerMoves = player.returnMoves()
    battle = True
    while battle:
        if playerStats["speed"] > enemieStats["speed"]:
            enemie = playerAttack(playerMoves,playerStats,enemieStats,enemie)
            if enemie.Alive():
                player = enemieAttack(enemieMoves, playerStats,enemieStats,player)
        elif playerStats["speed"] < enemieStats["speed"]:
            player = enemieAttack(enemieMoves, playerStats,enemieStats,player)
            if player.isAlive():
                enemie = playerAttack(playerMoves,playerStats,enemieStats,enemie)
        if enemie.Alive() == False:
            battle = False
            print(enemie.health)
            print(enemie.Alive())
            loot = enemie.lootdrop()
            player.addToInventory(loot)
            print(f"You defeated {enemie.returnName()}")
        elif player.isAlive() == False:
            battle = False
            print("YOU DIED")
            quit()
    return player

player = character("your mother",100,50,50,100,50,1,[],[],["Basic Sword"])
enemie = mob(1,7,"chris da zombie",20,20,20,25,1,["Iron","Rotten Flesh"],1,None,1,["Bite"])
player = battle(enemie,player)
