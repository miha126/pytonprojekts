from carreter import Character

player1 = Character(name='vladick' , damage=10)
player2 = Character(name='sanya' , damage=8)
print(player1)
print(player2)
player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)