class nomoney():
    def __init__(self, message):
        Exception.__init__(self, message)
        if self.money <= 0:
            raise nomoney("нет бабушек")
        else:
            return
class no_nastroenie():
    def __init__(self, message):
        Exception.__init__(self, message)
        if self.mood <= 0:
            raise no_nastroenie("стал дед инсайдом")
        else:
            return
class pomer():
    def __init__(self, message):
        Exception.__init__(self, message)
        if self.health <= 0:
            raise nomoney("помер")
        else:
            return



class human:
    name = ''
    health = 100
    mood = 1
    money = 0

    def __init__(self, name='', health=100, mood=100, money=100):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money
    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.health} ' \
            f' настроение: {self.mood}\n' \
            f' бабло: {self.money}\n'

    def cgange_stats (self, money, mood, health):
        self.money += money
        self.mood += mood
        self.health += health

