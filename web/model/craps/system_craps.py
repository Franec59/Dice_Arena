import random

class Craps():

    def diceNumber():
        # _= LANCER
        dice1=random.randrange(1, 7)                    #Les deux ligne ici a modifier avec le système de dès
        dice2=random.randrange(1, 7)
        return (dice1, dice2)

    def twoDice(dices):
        dice1, dice2= dices
        print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(dice1, dice2, sum(dices)))

    def game(self):
        value=Craps.diceNumber()
        Craps.twoDice(value)
        sum_of_dices=sum(value)
        if sum_of_dices in (7, 11):
            result = "Congrats"

        elif sum_of_dices in (2, 3, 12):
            result="Loose"

        else:
            result="Continue your game"
            currentpoint=sum_of_dices
            print("good game, your current point is", currentpoint)
            
        while result == "Continue your game":
            value=Craps.diceNumber()
            Craps.twoDice(value)
            sum_of_dices=sum(value)
            if sum_of_dices == currentpoint:
                result="Congrats"
            elif sum_of_dices == 7:
                result="Loose"
        if result== "Congrats":
            print("Congrats")
        else:
            print("Lost")