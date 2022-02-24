class Checker40K:
    checker=0
    def checker40k():
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


