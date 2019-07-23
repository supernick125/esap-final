from pyglet.gl import *
#move in direction of camera facing

class Projectile:

    def get_tex(self,file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self,pos,rot):
        self.batch = pyglet.graphics.Batch()
        self.pos = list(pos)
        self.rot = list(rot)
        self.vel = [10,10,10]

        self.top = self.get_tex("textures/tnt_top.png")
        self.side = self.get_tex("textures/tnt_side.png")
        self.bottom = self.get_tex("textures/tnt_bottom.png")

        x,y,z = pos[0],pos[1],pos[2]
        X,Y,Z = x+.25,y+.25,z+.25

        tex_coords = ("t2f", (0,0, .25,0, .25,.25, 0,.25))

        self.back_verts = ("v3f",(X,y,z, x,y,z, x,Y,z, X,Y,z))
        self.front_verts = ("v3f",(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z))
        self.left_verts = ("v3f",(x,y,z, x,y,Z, x,Y,Z, x,Y,z))
        self.right_verts = ("v3f",(X,y,Z, X,y,z, X,Y,z, X,Y,Z))
        self.bottom_verts = ("v3f",(x,y,z, X,y,z, X,y,Z, x,y,Z))
        self.top_verts = ("v3f",(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z))

        self.v = self.batch.add(4,GL_QUADS,self.side,self.back_verts,tex_coords) #back
        self.batch.add(4,GL_QUADS,self.side,self.front_verts,tex_coords) #front
        self.batch.add(4,GL_QUADS,self.side,self.left_verts,tex_coords) #left
        self.batch.add(4,GL_QUADS,self.side,self.right_verts, tex_coords) #right
        self.batch.add(4,GL_QUADS,self.bottom,self.bottom_verts, tex_coords) #bottom
        self.batch.add(4,GL_QUADS,self.top,self.top_verts, tex_coords) #top

    def draw(self):
        self.batch.draw()

    def update(self,dt):
        s = dt * 10
        self.pos[0] += self.vel[0] * s
        self.pos[1] += self.vel[1] * s
        self.pos[2] += self.vel[2] * s
