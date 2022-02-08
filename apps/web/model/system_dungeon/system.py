import random

class Dungeon():
    def __init__(self) -> None:
        pass
    
    def attaque(self):
        bonus=int(input("bonus d'attaque: "))
        ca=int(input("classe d'armure adverse: "))
        pot=random.sample(range(1, 21), 1)
        resultattaque=[]
        for dice in pot:
            dice=dice+bonus
            if dice<ca:
                resultattaque.append("Echec")
            else:
                resultattaque.append("Touche")
        return resultattaque

    def jet(self):
        bonus=int(input("bonus du jet: "))
        diff=int(input("difficulté à atteindre: "))
        malus=int(input("Malus? "))
        pot=random.sample(range(1, 21), 1)
        resultatjet=[]
        for dice in pot:
            dice=dice+bonus-malus
            if dice<diff:
                resultatjet.append("Echec")
            else:
                resultatjet.append("Réussite")
        return resultatjet