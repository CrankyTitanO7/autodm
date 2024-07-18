import random
import colorama

class speels:
    ice_learned = False
    fire_learned = False
    lightning_learned = False

class monsters:
    monnies = {
        "vilespawn" : "alive",
        "ogre" : "alive",
        "minotaur" : "alive"
    }

    def createMonster(name):
        name = input()
        monsters.monnies[name] = "alive"
    
    def listmons():
        print(monsters.monnies)

print("name?")
name = input()
monsters.createMonster(name)
monsters.listmons()