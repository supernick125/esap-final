from projectile import *

class Projectiles:

    def add_to_projectiles(self,proj):
        self.projectiles.append(proj)

    def __init__(self):
        self.projectiles = []
        self.projectiles.append(Projectile([-1,0,0,1],[0,0]))

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()

    def update(self,dt):
        for projectile in self.projectiles:
            projectile.update2(dt)
