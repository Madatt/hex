import pyglet
import entities.entity

class Hex(entities.entity):
    def __init__(self,g):
        super().__init(g)





class HexGrid(entities.entity):
    def __init__(self,g,w,h):
        super().__init(g)

        self._grid = []

        self._width = w
        self._height = h
        self._grid = [[0 for x in range(w)] for y in range(h)]

        self._batch=pyglet.graphics.Batch()

        self._sprites = [[None for x in range(w)] for y in range(h)]

    def get(self, x, y):
        return self._grid[y][x]

    def draw(self):
        for j in range(self._height):
            for i in range(self._width):
                if(self._sprites[j][i]==None):
                    self._sprites[j][i]=pyglet.sprite.Sprite(self.Game.textures['hex'],batch=self._batch)

                self._sprites[j][i].x=(112-2)*i+j*56
                self._sprites[j][i].y=-(128-2)*j*3/4+500


        self._batch.draw()



    def loop(self,dt):

        pass