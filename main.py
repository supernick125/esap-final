from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from player import *
from block import *
from chunk import *
import math
#collision updates

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
        if self.mouse_lock and BUTTON == mouse.LEFT: self.player.mouse_press(x,y,BUTTON)

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
    glEnable(GL_CULL_FACE) #Only renders visible faces
    pyglet.app.run()
