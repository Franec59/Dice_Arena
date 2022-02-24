import random

class Craps():

    def diceNumber():
        # _=input("dès")
        dice1=random.randrange(1, 7)                    #Les deux ligne ici a modifier avec le système de dès
        dice2=random.randrange(1, 7)
        return (dice1, dice2)

    # def twoDice(dices):
    #     dice1, dice2= dices
    #     return (dice1, dice2, sum(dices))


    def game(self):
        value=Craps.diceNumber()
        # Craps.twoDice(value)
        sum_of_dices=sum(value)
        if sum_of_dices in (7, 11):
            return "v"

        elif sum_of_dices in (2, 3, 12):
            return "p"

        else:
            return "c"
            # result="Continue your game"
            # currentpoint=sum_of_dices
            # return currentpoint
    def suitgame(point):
        value=Craps.diceNumber()
        # Craps.twoDice(value)
        sum_of_dices=sum(value)
        if sum_of_dices == point:
            return "v"
        elif sum_of_dices == 7:
            return "p"
        # if result== "Congrats":
        #     print("Congrats")
        # else:
        #     print("Lost")