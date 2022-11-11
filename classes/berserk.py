from gamme.carreter import Character
import random
success = 0
for i in range(10):
    if random.randint(1,10 ) <= 9:
        print('Прокнуло')

    else:
        print("und")
        success += 1
class Assasin(Character):
    def __init__(self, name='', health=100, damage=10, defence=0):
        Character.__init__(self, name, health, damage, defence )
        while(10):
            if success >= 1:
                    damage = 1000
             else:
                damage = (damage)

