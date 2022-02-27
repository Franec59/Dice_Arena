# test des fonctions de craps.py avec pytest

# pour installer pytest : pip install -U pytest
# pour lancer pytest : taper la commande pytest

# tester pytest ====================================================
# def inc(x):
#     return x + 1

# def test_anwser():
#     assert inc(3) == 5
    
# test de la fonction dice_number()

import random

def diceNumber():
    dice1=random.randrange(1, 7)                    #Les deux ligne ici a modifier avec le système de dès
    return dice1

def test_diceNumber():
    # assert diceNumber() in (8, 9, 10)
    assert diceNumber() in (1, 2, 3, 4, 5 ,6, 7)