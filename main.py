#Bobby and Nick ESAPCS July 2019

import math
from collections import deque

from pyglet.gl import *
from pyglet.window import key, mouse

from player import *
from world import *

TICKS_PER_SEC = 60
#collision updates

class Window(pyglet.window.Window):

    def push(self,pos,rot): glPushMatrix(); glRotatef(-rot[0],1,0,0); glRotatef(-rot[1],0,1,0); glTranslatef(-pos[0],-pos[1],-pos[2])

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()


    def set2d(self):
        glDisable(GL_DEPTH_TEST)

        width = self.get_size()
        height = self.get_size()

        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        
       
        self.Projection()
        gluOrtho2D(0,self.width,0,self.height)
        self.Model()


    def set3d(self): 
        glEnable(GL_DEPTH_TEST)

        width = self.get_size()
        height = self.get_size()

        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))

        self.Projection(); 
        gluPerspective(65.0, self.width / self.height, 0.1, 60.0);
        self.Model()


    def setLock(self,state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self: self.lock,setLock)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300,300)
        self.cursor = self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR)
        self.set_mouse_cursor(self.cursor)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

        self.world = World()
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
        self.set2d()
        self.set3d()

        self.push(self.player.pos,self.player.rot)
        self.world.draw()
        glPopMatrix()

        

def main():
    window = Window(width=1200, height=600, caption='MINECRAFT?', resizable=True)
    glEnable(GL_FOG)
    glClearColor(0.5, 0.69, 1.0, 1)
    glEnable(GL_CULL_FACE)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
    glHint(GL_FOG_HINT, GL_DONT_CARE)
    glFogi(GL_FOG_MODE, GL_LINEAR)
    glFogf(GL_FOG_START, 15.0)
    glFogf(GL_FOG_END, 55.0)


    pyglet.app.run()

if __name__ == "__main__":
    main()
