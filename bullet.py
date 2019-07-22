from pyglet.gl import *

class Bullet:
    def __init__(self,pos,rot):
        self.batch = pyglet.graphics.Batch()
        self.pos = list(pos)
        self.rot = list(rot)

        x,y,z = pos[0],pos[1],pos[2]
        X,Y,Z = x

        self.batch.add(3,GL_TRIANGLES,None,("v3f",(x,y,z, x,y,z, x,y,z)),)

    def draw(self):
        self.batch.draw()

    def update(self,dt):
        s = dt * 10
        vel[0]
        self.pos[0] += vel[0] * s
        self.pos[1] += vel[1] * s
        self.pos[2] += vel[2] * s
