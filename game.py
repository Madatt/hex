import pyglet
import entities.vector2d
from pyglet.gl import *

class Game(pyglet.window.Window):
    def __init__(self, w,h):
        super().__init__(w,h)
        self.window_width=w
        self.window_height=h
        self._states= {}
        self._current= "none"

        pyglet.resource.path = ['res']
        pyglet.resource.reindex()
        self.textures={}
        self.textures["hex"]=pyglet.resource.image("hex.png")

        self.view=entities.vector2d.Vector2D()

        self.mouse_status=[0,0,0]
        self.mouse_status_drag=[[0,entities.vector2d.Vector2D(),entities.vector2d.Vector2D()],
                                [0, entities.vector2d.Vector2D(), entities.vector2d.Vector2D()],
                                [0, entities.vector2d.Vector2D(), entities.vector2d.Vector2D()]]
        self.mouse_position=entities.vector2d.Vector2D()
        self.mouse_position_last=entities.vector2d.Vector2D()

    def add_state(self, n, s):
        self._states[n] = s(self)

    def get_current(self):
        return self._states[self._current]

    def set_current(self, n):

        if n not in self._states:
            return None

        self._current= n
        self._states[self._current].init()

    def draw_view_start(self):
        glLoadIdentity()
        glTranslatef(-self.view.x,-self.view.y,0)

    def draw_view_stop(self):
        glLoadIdentity()

    def on_mouse_press(self,x,y,b,m):
        if b==pyglet.window.mouse.LEFT:
            self.mouse_status[0]=1

    def on_mouse_release(self,x,y,b,m):
        if b==pyglet.window.mouse.LEFT:
            self.mouse_status[0]=0
            self.mouse_status_drag[0][0]=0

    def on_mouse_motion(self,x, y, dx, dy):
        self.mouse_position_last.x=self.mouse_position.x
        self.mouse_position_last.y=self.mouse_position.y
        self.mouse_position.x=x+self.view.x
        self.mouse_position.y=y+self.view.y
        if dx==0 and dy==0:
            self.mouse_status_drag[0][0] = 0

    def on_mouse_drag(self,x, y, dx, dy, b, m):
        if b==pyglet.window.mouse.LEFT:
            self.mouse_status_drag[0][0] = 1
            self.mouse_status_drag[0][1].set(x+self.view.x,y+self.view.y)
            self.mouse_status_drag[0][2].set(dx,dy)

            self.mouse_position_last.x = self.mouse_position.x
            self.mouse_position_last.y = self.mouse_position.y
            self.mouse_position.x = x + self.view.x
            self.mouse_position.y = y + self.view.y

    def reset_inputs(self):
        self.mouse_status_drag[0][0] = 0


    def main_loop(self):
        acc = 0
        tps = 1.0 / 60.0

        while True:
            ela = pyglet.clock.tick()
            acc += ela

            while acc >= tps:
                acc -= tps

                if self._current in self._states:
                    self._states[self._current].run(tps)

            self.clear()

            if self._current in self._states:
                self._states[self._current].draw()

            self.flip()
            self.reset_inputs()
            self.dispatch_events()



        pass
