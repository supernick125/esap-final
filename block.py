from pyglet.gl import *

SIDES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

EXPLODE = [
    ( 0, 1, 0),
    ( 0, 1, 1),
    ( 0, 1,-1),
    ( 0,-1, 0),
    ( 0,-1, 1),
    ( 0,-1,-1),
    ( 1, 0, 0),
    ( 1, 1, 0),
    ( 1,-1, 0),
    (-1, 0, 0),
    (-1, 1, 0),
    (-1,-1, 0),
    ( 1, 0, 1),
    ( 1, 0,-1),
    (-1, 0, 1),
    (-1, 0,-1),
]

class Block:

    def get_tex(self,file):
        """Return TextureGroup of specified image file"""
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self,pos,top_tex,side_tex,bottom_tex):
        """Initializes Block object"""

        self.top = self.get_tex(self.top_tex)
        self.side = self.get_tex(self.side_tex)
        self.bottom = self.get_tex(self.bottom_tex)

        self.pos = pos

    def gen_exposed_key(self, world):
        """Return exposure key based on which faces are exposed"""
        #true if not surrounded
        self.exposed_key = [0,0,0,0,0,0]
        x,y,z = self.pos
        for dx,dy,dz in SIDES:
            if (x + dx, y + dy, z + dz) not in world:
                self.exposed_key[SIDES.index((dx,dy,dz))] += 1
        return self.exposed_key

    def add_to_batch(self, key):
        """Create new Batch object containing faces specified by exposure key"""
        #Key is 6 long list of 1 and 0 (0,0,0,0,0,0)
        #Top Bottom Left Right Front Back

        self.batch = pyglet.graphics.Batch()

        tex_coords = ("t2f", (0,0, 1,0, 1,1, 0,1))

        x,y,z = self.pos[0] - .5,self.pos[1] - .5,self.pos[2] - .5
        X,Y,Z =  self.pos[0] + .5,self.pos[1] + .5,self.pos[2] + .5

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

    def on_destroy(self):
        return None

    def get_pos(self):
        """Return position tuple"""
        return self.pos

    def draw(self):
        """Block draw function draws batch instance"""
        self.batch.draw()

#BLOCK SUBCLASSES (ALPHABETICAL)
class Bedrock(Block):
    def __init__(self,pos):
        self.top_tex = "textures/bedrock.png"
        self.side_tex = "textures/bedrock.png"
        self.bottom_tex = "textures/bedrock.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Cactus(Block):
	def __init__(self,pos):
		self.top_tex = "textures/cactus_top.png"
		self.side_tex = "textures/cactus_side.png"
		self.bottom_tex = "textures/cactus_bottom.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Dirt(Block):
    def __init__(self,pos):
        self.top_tex = "textures/dirt.png"
        self.side_tex = "textures/dirt.png"
        self.bottom_tex = "textures/dirt.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Grass(Block):
    def __init__(self,pos):
        self.top_tex = "textures/grass_top.png"
        self.side_tex = "textures/grass_side.png"
        self.bottom_tex = "textures/dirt.png"

        super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Ice(Block):
	def __init__(self,pos):
		self.top_tex = "textures/frosted_ice_0.png"
		self.side_tex = "textures/ice.png"
		self.bottom_tex = "textures/ice.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Leaves(Block):
	def __init__(self,pos):
		self.top_tex = "textures/leaves_oak.png"
		self.side_tex = "textures/leaves_oak.png"
		self.bottom_tex = "textures/leaves_oak.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Pumpkin(Block):
	def __init__(self, pos):
		self.top_tex = "textures/pumpkin_top.png"
		self.side_tex = "textures/carved_pumpkin.png"
		self.bottom_tex = "textures/pumpkin_side.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Sand(Block):
	def __init__(self,pos):
		self.top_tex = "textures/sand.png"
		self.side_tex = "textures/sand.png"
		self.bottom_tex = "textures/sand.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Snow(Block):
	def __init__(self,pos):
		self.top_tex = "textures/snow.png"
		self.side_tex = "textures/grass_block_snow.png"
		self.bottom_tex = "textures/dirt.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Spruce(Block):
	def __init__(self,pos):
		self.top_tex = "textures/spruce_log_top.png"
		self.side_tex = "textures/spruce_log.png"
		self.bottom_tex = "textures/spruce_log_top.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Stone(Block):
	def __init__(self,pos):
		self.top_tex = "textures/stone.png"
		self.side_tex = "textures/stone.png"
		self.bottom_tex = "textures/stone.png"

		super().__init__(pos,self.top_tex,self.side_tex,self.bottom_tex)

class Tnt(Block):
    def __init__(self,pos):
        self.top_tex = "textures/tnt_top.png"
        self.side_tex = "textures/tnt_side.png"
        self.bottom_tex = "textures/tnt_bottom.png"

        self.pos = pos

        super().__init__(self.pos,self.top_tex,self.side_tex,self.bottom_tex)

    def on_destroy(self):
        exploded_blocks = []
        for dx,dy,dz in EXPLODE:
            exploded_blocks.append((self.pos[0] + dx,self.pos[1] + dy,self.pos[2] + dz))
        return exploded_blocks
