class Monster(object):
    def __init__(self, hit_points=5, weapon="sword", color="red", sound="roar"):
        self.hit_points = hit_points
        self.weapon = weapon
        self.color = color
        self.sound = sound

    def battlecry(self):
        return self.sound.upper()
