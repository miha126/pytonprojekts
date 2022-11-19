class nomoney():
    def __init__(self, message):
        Exception.__init__(self, message)



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

