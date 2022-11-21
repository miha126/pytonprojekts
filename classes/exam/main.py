from person import human
from person import nomoney
from person import no_nastroenie
from person import pomer
import random



Man = human(name="сашка", money = 45, mood = 100, health= 100)
while True:
    print(Man)
    ass = random.randint(1, 2)
    if ass == 1:
        Man.cgange_stats(
            money = random.randint(20, 50),
            mood = random.randint(-20, -10),
            health = random.randint(-10, -5)
        )
    else:
        Man.cgange_stats(
            money=random.randint(-50, -20),
            mood=random.randint(10, 20),
            health=random.randint(5, 10)
        )