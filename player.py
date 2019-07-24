from pyglet.window import key
from pyglet.window import mouse
import math

WALKING_SPEED = 10

GRAV = 20.0
MAX_JUMP = 1.0
JUMP_SPEED = math.sqrt(2 * GRAV * MAX_JUMP)
TERMINAL_VEL = 50

PLAYER_HEIGHT = 2

class Player:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = pos
        self.rot = rot
        self.lat = [0,0] #lateral movement
        self.dy = 0 #vertical velocity

    def fire(self):
        print("pew")

    def mouse_press(self,x,y,BUTTON):
        return self.fire()

    def mouse_motion(self,dx,dy):
        m = 0.15
        x,y = self.rot
        x,y = x + dx * m, y + dy * m
        y = max(-90, min(90, y))
        self.rot = (x, y)

    def key_press(self,KEY,MOD):
        if KEY == key.W:
            self.lat[0] -= 1
        elif KEY == key.S:
            self.lat[0] += 1
        elif KEY == key.A:
            self.lat[1] -= 1
        elif KEY == key.D:
            self.lat[1] += 1
        elif KEY == key.SPACE:
            if self.dy == 0:
                self.dy = JUMP_SPEED

    def key_release(self,KEY,MOD):
        if KEY == key.W:
            self.lat[0] += 1
        elif KEY == key.S:
            self.lat[0] -= 1
        elif KEY == key.A:
            self.lat[1] += 1
        elif KEY == key.D:
            self.lat[1] -= 1

    def get_sight_vector(self):
        x,y = self.rot

        q = math.cos(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * q
        dy = math.sin(math.radians(y))
        dz = math.sin(math.radians(x - 90)) * q

        return (dx,dy,dz)

    def get_motion_vector(self):
        if any(self.lat):
            x,y = self.rot
            lat = math.degrees(math.atan2(*self.lat))
            x_angle = math.radians(x + lat)
            y_angle = math.radians(y)

            #flying?

            dx = math.cos(x_angle)
            dy = 0.0
            dz = math.sin(x_angle)
        else:
            dx = 0.0
            dy = 0.0
            dz = 0.0
        return (dx,dy,dz)

    def update(self,dt,keys):
        speed = WALKING_SPEED
        d = dt*speed
        dx,dy,dz = self.get_motion_vector()
        dx,dy,dz = dx * d, dy * d, dz * d

        #GRAVITY
        # self.dy -= dt * GRAV
        # self.dy = max(self.dy, -TERMINAL_VEL)
        # dy += self.dy * dt

        x,y,z = self.pos
        x,y,z = self.collide((x + dx,y + dy,z + dz), PLAYER_HEIGHT)
        self.pos = (x,y,z)

        rotY = -self.rot[1]/180*math.pi
        dx,dz = d*math.sin(rotY),d*math.cos(rotY)

    def collide(self, pos, height):
        p = list(pos)


        return tuple(p)
