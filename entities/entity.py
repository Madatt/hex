import pyglet
import entities.vector2d

class Entity:
    def __init__(self,g):
        self.Game=g
        self._position=entities.vector2d.Vector2D()


    def draw(self):
        pass

    def loop(self,dt):
        pass