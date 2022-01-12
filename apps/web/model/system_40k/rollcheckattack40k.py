
dicepool=Dice.dicecheck()

class Rollcheckattack40K():

# Fonction du jet d'attaque
    def rollattaque():
        ct=int(input("CT de l'attaquant: "))        #Integer a mettre dans l'HTML
        modif=int(input("Modificateur d'attaque: "))        #Integer a mettre dans l'HTML
        damageset=0
        if modif>0:
            ct=ct+modif
        elif modif<0:
            ct=ct-modif
        for dice in dicepool:
            if dice>=ct:
                dice=1
                damageset+=dice
            else:
                continue
        return(damageset)

