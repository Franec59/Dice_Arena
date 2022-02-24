import random

class Craps():

    def diceNumber():
        # _=input("dès")
        dice1=random.randrange(1, 7)                    #Les deux ligne ici a modifier avec le système de dès
        dice2=random.randrange(1, 7)
        return (dice1, dice2)

    def game(self):
        value=Craps.diceNumber()
        sum_of_dices=sum(value)
        if sum_of_dices in (7, 11):
            return "v", sum_of_dices, value
        elif sum_of_dices in (2, 3, 12):
            return "p", sum_of_dices, value
        else:
            return "c", sum_of_dices, value
            
    def faire_le_point(self):
        value=Craps.diceNumber()
        sum_of_dices=sum(value)
        return sum_of_dices, value
        