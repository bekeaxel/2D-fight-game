
class Projectile:
    def __init__(self, x, y, dir):
        self.x = x 
        self.y = y
        self.radius = 18
        self.dir = dir
        self.vel = 4

    def move(self):
        self.x += self.vel * self.dir

    # def draw(self):
    #     win.blit(spell_projectile[2], (self.x - 18, self.y - 18))
