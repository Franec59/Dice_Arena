from checker40k import Checker40K

damagepool=Dice.damagpool()

class Rolldamage():
# Fonction du jet des dégâts
    def rolldamage():
        bless=Checker40K.checker40k()
        modif=int(input("Modificateur de blessure: "))          #Integer a mettre dans l'HTML
        saveset=0
        if modif<0:
            bless=bless-modif
        elif modif>0:
            bless=bless+modif
        for dice in damagepool:
            if dice>=bless:
                dice=1
                saveset+=dice
            else:
                continue
        return(saveset)
