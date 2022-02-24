
savepool=Dice.savepool()

class Rollsave():
# Fonction du test d'armure
    def rollsave():
        armor=int(input("Sauvegarde d'armure: "))               #Integer a mettre dans l'HTML
        couvert=int(input("bonus de couvert: "))                #Integer a mettre dans l'HTML
        pa=int(input("PA de l'arme: "))                         #Integer a mettre dans l'HTML
        armorTest=armor+couvert-pa
        savesucced=0
        for dice in savepool:
            if dice >= armorTest:
                dice=1
                savesucced+=dice
            else:
                continue
        return(savesucced)
