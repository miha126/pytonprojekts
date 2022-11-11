from berserk import Assasin
from gamme.carreter import Character

player1 = Assasin(name="vladik")
player2 = Character (name="antushka", damage=10)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)