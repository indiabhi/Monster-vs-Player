import random

class Combat(object):
    dodge_limit = 7
    attack_limit = 7

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4
