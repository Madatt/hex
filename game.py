import pyglet


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

    def add_state(self, n, s):
        self._states[n] = s(self)

    def get_current(self):
        return self._states[self._current]

    def set_current(self, n):

        if n not in self._states:
            return None

        self._current= n


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

            if self._current in self._states:
                self._states[self._current].draw()

            self.dispatch_events()


        pass