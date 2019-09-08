#Bobby and Nick ESAPCS July 2019

import pygame
import math
import wave
import sys

import pyglet
from pyglet.gl import *
from pyglet.window import key, mouse
import pyglet.media

from player import *
from world import *

TICKS_PER_SEC = 60

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        """Initialize Window object and create important game objects"""
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300,300)
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

        self.reticle = None
        self.world = World()
        self.player = Player((9,5,9),(0,0))

        self.place = "stone"

    def setLock(self,state):
        """Set mouse exclusivity state"""
        self.lock = state
        self.set_exclusive_mouse(state)
    lock = False
    mouse_lock = property(lambda self: self.lock,setLock)

    def update(self,dt):
        """Built in update function runs consistently based on scheduler"""
        m = 8
        dt = min(dt, .2)
        for _ in range(m):
            self.player.update(dt / m,self.world.get_world_coords())

    def on_mouse_press(self,x,y,BUTTON,MOD):
        """Built in functions runs on mouse press"""
        if self.mouse_lock:
            click = self.player.mouse_press(x,y,BUTTON,MOD,self.world.get_world_coords())
            if click == None:
                pass
            elif click[0] == "build":
                self.world.add_block(click[1],self.place)
            elif click[0] == "break":
                self.world.destroy_block(click[1])

    def on_mouse_motion(self,x,y,dx,dy):
        """Built in function runs on mouse motion"""
        if self.mouse_lock:
            self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        """Built in function runs on key press"""
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.E:
            self.mouse_lock = not self.mouse_lock
        elif KEY == key.Z:
            self.place = "stone"
        elif KEY == key.X:
            self.place = "dirt"
        elif KEY == key.C:
            self.place = "tnt"
        self.player.key_press(KEY,MOD)

    def on_key_release(self,KEY,MOD):
        """Bulit in function runs on key release"""
        self.player.key_release(KEY,MOD)

    def on_resize(self,width,height):
        """Built in function runs on window resize"""
        if self.reticle:
            self.reticle.delete()
        x,y = self.width // 2, self.height // 2
        n = 10
        self.reticle = pyglet.graphics.vertex_list(4,("v2i", (x-n,y,x+n,y,x,y-n,x,y+n)))

    def set2d(self):
        """Set openGL draw mode to 2d"""
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
        """Set openGL draw mode to 3d"""
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
        """Built in draw function runs consistently"""
        self.clear()
        self.set3d(self.player.pos,self.player.rot)
        glColor3d(1,1,1)
        self.world.draw()
        self.set2d()
        self.draw_reticle()

    def draw_reticle(self):
        """Draw reticle in center of screen"""
        glColor3d(0,0,0)
        self.reticle.draw(GL_LINES)

def play_background_music():
    """Start background music"""
    pygame.mixer.init()
    pygame.mixer.music.load('backgroundmusic.wav')
    pygame.mixer.music.play(999)

def main():
    """Main function create Window object and set openGL and fog settings"""
    window = Window(width=1250, height=750, caption='shitty mc', resizable=True)
    glEnable(GL_FOG)
    glClearColor(0.5, 0.69, 1.0, 1)
    glEnable(GL_CULL_FACE)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
    glHint(GL_FOG_HINT, GL_DONT_CARE)
    glFogi(GL_FOG_MODE, GL_LINEAR)
    glFogf(GL_FOG_START, 5.0)
    glFogf(GL_FOG_END, 20.0)

    play_background_music()
    pyglet.app.run()

if __name__ == "__main__":
    main()
