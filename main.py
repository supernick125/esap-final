from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import math

class Chunk:
    def __init__(self):
        self.blocks = []
        for i in range(16):
            for j in range(16):
                self.blocks.append(Block((i,0,j)))

    def draw(self):
        for block in self.blocks:
            block.draw()

class Block:

    def get_tex(self,file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self,pos):

        self.top = self.get_tex("textures/grass_top.png")
        self.side = self.get_tex("textures/grass_side.png")
        self.bottom = self.get_tex("textures/dirt.png")

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


class Player:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def fire(self):
        bullet = Bullet(self.pos,self.rot)

    def mouse_press(self,x,y,BUTTON):
        if BUTTON == mouse.LEFT: self.fire()

    def mouse_motion(self,dx,dy):
        dx/=8; dy/=8; self.rot[0] += dy; self.rot[1] -= dx
        if self.rot[0]>90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if keys[key.W]: self.pos[0] += dx; self.pos[2] -= dz
        if keys[key.S]: self.pos[0] -= dx; self.pos[2] += dz
        if keys[key.A]: self.pos[0] -= dz; self.pos[2] -= dx
        if keys[key.D]: self.pos[0] += dz; self.pos[2] += dx

        if keys[key.SPACE]: self.pos[1] += s
        if keys[key.LSHIFT]: self.pos[1] -= s

class Window(pyglet.window.Window):

    def push(self,pos,rot): glPushMatrix(); glRotatef(-rot[0],1,0,0); glRotatef(-rot[1],0,1,0); glTranslatef(-pos[0],-pos[1],-pos[2])

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0,self.width,0,self.height); self.Model
    def set3d(self): self.Projection(); gluPerspective(70,self.width/self.height,0.05,1000); self.Model

    def setLock(self,state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self: self.lock,setLock)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300,300)
        self.cursor = self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR)
        self.set_mouse_cursor(self.cursor)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.chunk = Chunk()
        self.player = Player((0.5,2,2),(0,-90))

    def on_mouse_press(self,x,y,BUTTON,MOD):
        if self.mouse_lock: self.player.mouse_press(x,y,BUTTON)

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.player.update(dt,self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)
        self.chunk.draw()
        glPopMatrix()

if __name__ == "__main__":
    window = Window(width=1500,height=700,caption="Minecraft",resizable=True)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST)
    pyglet.app.run()
