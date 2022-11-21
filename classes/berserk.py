from gamme.carreter import Character
import random
class Assasin(Character):
    def __init__(self, name='', health=100, damage=10, defence=0):
        Character.__init__(self, name, health, damage, defence,)
        self.max_health = self.health
    def attack (self, target):
        a = random.randint(1,50)
        if a <= 2:
             target.take_damage(self.damage+1000)
        else:
             target.take_damage(self.damage)
