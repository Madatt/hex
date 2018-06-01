import pyglet
import entities.entity
import utils
import math

class Hex(entities.entity.Entity):
    def __init__(self,g):
        super().__init__(g)
        self.type=0
        self.sprite=None

    def draw(self):
        pass

    def loop(self,dt):
        pass


class HexGrid(entities.entity.Entity):
    def __init__(self,g,x,y,s,w,h):
        super().__init__(g)

        self._grid = {}
        self._batch=pyglet.graphics.Batch()

        self.position.x=x
        self.position.y=y

        self.size=s
        self.width=w
        self.height=h

        for r in range(self.height):
            off=math.floor(r/2)
            for q in range(-off,self.width-off):
                self.add_hex(q,r)

    def add_hex(self,x,y):
        if self.get_hex(x,y)==None:
            hs = utils.hash_cords(x, y)
            self._grid[hs]=Hex(self.Game)
            self._grid[hs].position.x=x
            self._grid[hs].position.y=y
            return self._grid[hs]

        return None

    def remove_hex(self,x,y):
        hs = utils.hash_cords(x, y)
        if hs in self._grid:
            del self._grid[hs]

    def get_hex(self,x,y):
        hs=utils.hash_cords(x,y)
        if hs in self._grid:
            return self._grid[hs]
        else:
            return None



    def draw(self):
        for i in self._grid:
            if self._grid[i].sprite == None:
                self._grid[i].sprite = pyglet.sprite.Sprite(self.Game.textures['hex'],batch=self._batch)


            self._grid[i].sprite.x = (112 - 2) * self._grid[i].position.x + self._grid[i].position.y * 56
            self._grid[i].sprite.y = -(128 - 2) * self._grid[i].position.y * 3 / 4 + 500


        self._batch.draw()

    def loop(self,dt):

        pass