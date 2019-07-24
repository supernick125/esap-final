#Bobby and Nick ESAPCS July 2019

import math

from pyglet.gl import *
from pyglet.window import key, mouse

from player import *
from world import *

TICKS_PER_SEC = 60

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300,300)
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

        self.reticle = None

        self.world = World()
        self.player = Player((0,3,0),(0,0))

    def setLock(self,state):
        self.lock = state
        self.set_exclusive_mouse(state)
    lock = False
    mouse_lock = property(lambda self: self.lock,setLock)

    def update(self,dt):
        m = 8
        dt = min(dt, 0.2)
        for _ in range(m):
            self.player.update(dt / m,self.world.get_world_coords())

    def on_mouse_press(self,x,y,BUTTON,MOD):
        if self.mouse_lock and BUTTON == mouse.LEFT: self.player.mouse_press(x,y,BUTTON)

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock
        self.player.key_press(KEY,MOD)

    def on_key_release(self,KEY,MOD):
        self.player.key_release(KEY,MOD)

    def on_resize(self,width,height):
        if self.reticle:
            self.reticle.delete()
        x,y = self.width // 2, self.height // 2
        n = 10
        self.reticle = pyglet.graphics.vertex_list(4,("v2i", (x-n,y,x+n,y,x,y-n,x,y+n)))

    def set2d(self):
        glDisable(GL_DEPTH_TEST)
        width = self.get_size()
        height = self.get_size()
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0,self.width,0,self.height)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set3d(self,pos,rot):
        glEnable(GL_DEPTH_TEST)
        width = self.get_size()
        height = self.get_size()
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, self.width / self.height, 0.1, 60.0);
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glRotatef(rot[0],0,1,0)
        glRotatef(-rot[1], math.cos(math.radians(rot[0])), 0, math.sin(math.radians(rot[0])))
        glTranslatef(-pos[0],-pos[1],-pos[2])

    def on_draw(self):
        self.clear()
        self.set3d(self.player.pos,self.player.rot)
        glColor3d(1,1,1)
        self.world.draw()
        self.set2d()
        self.draw_reticle()

    def draw_reticle(self):
        glColor3d(0,0,0)
        self.reticle.draw(GL_LINES)

def main():
    window = Window(width=1000, height=500, caption='shitty mc', resizable=True)
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
