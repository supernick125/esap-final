from pyglet.gl import *

class Block:

    def get_tex(self,file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self,pos,top_tex,side_tex,bottom_tex):

        self.top = self.get_tex(self.top_tex)
        self.side = self.get_tex(self.side_tex)
        self.bottom = self.get_tex(self.bottom_tex)

        self.batch = pyglet.graphics.Batch()

        tex_coords = ("t2f", (0,0, 1,0, 1,1, 0,1))

        x,y,z = pos[0],pos[1],pos[2]
        X,Y,Z = x+1,y+1,z+1

        self.batch.add(4,GL_QUADS,self.side,("v3f",(X,y,z, x,y,z, x,Y,z, X,Y,z)), tex_coords) #back
        self.batch.add(4,GL_QUADS,self.side,("v3f",(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), tex_coords) #front
        self.batch.add(4,GL_QUADS,self.side,("v3f",(x,y,z, x,y,Z, x,Y,Z, x,Y,z)), tex_coords) #left
        self.batch.add(4,GL_QUADS,self.side,("v3f",(X,y,Z, X,y,z, X,Y,z, X,Y,Z)), tex_coords) #right
        self.batch.add(4,GL_QUADS,self.bottom,("v3f",(x,y,z, X,y,z, X,y,Z, x,y,Z)), tex_coords) #bottom
        self.batch.add(4,GL_QUADS,self.top,("v3f",(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), tex_coords) #top

    def draw(self):
        self.batch.draw()
