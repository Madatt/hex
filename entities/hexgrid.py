import pyglet
import entities.entity

class Hex(entities.entity):
    def __init__(self,g):
        super().__init(g)
        self.type=0

    def draw(self):
        pass

    def loop(self,dt):
        pass


class HexGrid(entities.entity):
    def __init__(self,g,**kwargs):
        super().__init(g)

        self._grid = []
        self._sprites = []
        self._batch=pyglet.graphics.Batch()

    def add_hex(self,x,y):
        pass


    def remove_hex(self,x,y):
        pass

    def get_hex(self,x,y):
        

    def draw(self):
        pass


    def loop(self,dt):

        pass