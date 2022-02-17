class W40K():
    def __init__(self) -> None:
        pass
    
    def checker40k(self, checker):
        force=int(input("Force: "))             #Integer a mettre dans l'HTML
        endurance=int(input("Endurance: "))     #Integer a mettre dans l'HTML
        differenciel=force-endurance
        if differenciel==0:
            checker=4
            return checker
        elif differenciel==1:
            checker=3
            return checker
        elif differenciel>=2:
            checker=2
            return checker
        elif differenciel== -1:
            checker=5
            return checker
        elif differenciel<= -2:
            checker=6
            return checker
        else:
            return "Valeur trop faible pour être prise en compte."
    
    def rollsave(self):
        armor=int(input("Sauvegarde d'armure: "))               #Integer a mettre dans l'HTML
        couvert=int(input("bonus de couvert: "))                #Integer a mettre dans l'HTML
        pa=int(input("PA de l'arme: "))                         #Integer a mettre dans l'HTML
        armorTest=armor+couvert-pa
        savesucced=0
        for dice in savepool:                   # pareil que pour dicepool
            if dice >= armorTest:
                dice=1
                savesucced+=dice
            else:
                continue
        return(savesucced)
    
    def rollattaque(self,):
        ct=int(input("CT de l'attaquant: "))        #Integer a mettre dans l'HTML
        modif=int(input("Modificateur d'attaque: "))        #Integer a mettre dans l'HTML
        damageset=0
        if modif>0:
            ct=ct+modif
        elif modif<0:
            ct=ct-modif
        for dice in dicepool:                   #dicepool à remplacer par le résultat de la sélection des dès en HTML
            if dice>=ct:
                dice=1
                damageset+=dice
            else:
                continue
        return(damageset)
    
    def rolldamage(self,checker):
        bless=checker
        modif=int(input("Modificateur de blessure: "))          #Integer a mettre dans l'HTML
        saveset=0
        if modif<0:
            bless=bless-modif
        elif modif>0:
            bless=bless+modif
        for dice in damagepool:                 # pareil que pour dicepool
            if dice>=bless:
                dice=1
                saveset+=dice
            else:
                continue
        return(saveset)