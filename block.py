from pyglet.gl import *
#get coords function

SIDES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

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

        self.pos = pos

    def gen_exposed_key(self, world): #DONT CALL EVERY TIME
        #true if not surrounded
        self.exposed_key = [0,0,0,0,0,0]
        x,y,z = self.pos
        for dx,dy,dz in SIDES:
            if (x + dx, y + dy, z + dz) not in world:
                self.exposed_key[SIDES.index((dx,dy,dz))] += 1
        return self.exposed_key

    def add_to_batch(self, key):
        #Key is 6 long list of 1 and 0 (0,0,0,0,0,0)
        #Top Bottom Left Right Front Back

        self.batch = pyglet.graphics.Batch()

        tex_coords = ("t2f", (0,0, 1,0, 1,1, 0,1))

        x,y,z = self.pos[0] - .5,self.pos[1] - .5,self.pos[2] - .5
        X,Y,Z =  self.pos[0] + .5,self.pos[1] + .5,self.pos[2] + .5

        #(1,0,0,1,0,0)
        if key[0]:
            self.batch.add(4,GL_QUADS,self.top,("v3f",(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z)), tex_coords) #Top
        if key[1]:
            self.batch.add(4,GL_QUADS,self.bottom,("v3f",(x,y,z, X,y,z, X,y,Z, x,y,Z)), tex_coords) #Bottom
        if key[2]:
            self.batch.add(4,GL_QUADS,self.side,("v3f",(x,y,z, x,y,Z, x,Y,Z, x,Y,z)), tex_coords) #Left
        if key[3]:
            self.batch.add(4,GL_QUADS,self.side,("v3f",(X,y,Z, X,y,z, X,Y,z, X,Y,Z)), tex_coords) #Right
        if key[4]:
            self.batch.add(4,GL_QUADS,self.side,("v3f",(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), tex_coords) #Front
        if key[5]:
            self.batch.add(4,GL_QUADS,self.side,("v3f",(X,y,z, x,y,z, x,Y,z, X,Y,z)), tex_coords) #Back

    def get_pos(self):
        return self.pos

    def draw(self):
        self.batch.draw()
