class Character:
    name = ''
    group = ''
    old = ''
    mark = ''

    def __init__(self, name="name", mark=mark, group=group, old=old ):

        self.name = name
        self.group = group,
        self.old = old
    def __str__(self):
        return f' == {self.name} ==\n ' \
            f'Здоровье: {self.health}\n'\
            f'Урон: {self.damage}\n'\
            f'защита: {self.defence}\n'
        f'Группа: {self.group}\n'
        f'возваст: {self.old}\n'
    def take_damage(self,damage=0):
        self.health -=max(damage, 0)

    def attack(self,  target):
        target.take_damage(self.damage)