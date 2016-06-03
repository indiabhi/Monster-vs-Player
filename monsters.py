class Monster(object):
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get('hit_points', 5)
        self.weapon = kwargs.get('weapon', 'sword')
        self.color = kwargs.get('color', 'red')
        self.sound = kwargs.get('sound', 'roar')

    def battlecry(self):
        return self.sound.upper()
