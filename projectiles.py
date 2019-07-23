
class Projectiles:

    def add_to_projectiles(self,proj):
        self.projectiles.append(proj)

    def __init__(self):
        self.projectiles = []

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()

    def update(self,dt):
        for projectile in self.projectiles:
            projectile.update2(dt)
