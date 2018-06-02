import pyglet
import entities.entity
import utils
import math
from pyglet.gl import *

class Hex(entities.entity.Entity):
    def __init__(self,g,b,s):
        super().__init__(g)
        self.type=0
        self.poly=None
        self.size=s
        self.points=[]
        self.testc=[]
        self.batch=b

    def calc_points(self,x,y):
        self.points=[]
        self.testc=[]
        for i in range(1,8):
            ang=math.radians(i*60+30)
            ang2=math.radians((i-1)*60+30)
            self.points.append(self.size*math.cos(ang)+x)
            self.points.append(self.size*math.sin(ang)+y)
            self.testc.append(0)
            self.testc.append(255)
            self.testc.append(0)

            self.points.append(self.size*math.cos(ang2)+x)
            self.points.append(self.size*math.sin(ang2)+y)
            self.testc.append(0)
            self.testc.append(255)
            self.testc.append(0)


    def gen_hex(self,xx,yy):
        if self.poly:
            return None

        if self.points==[]:
            self.calc_points(xx,yy)


        self.poly=self.batch.add(14,pyglet.gl.GL_LINES,None,('v2f',tuple(self.points)))

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
            off=int(math.floor(r/2))
            for q in range(-off,self.width-off):
                self.add_hex(q,r)

        print(self._grid)

    def add_hex(self,x,y):
        if self.get_hex(x,y)==None:
            hs = utils.hash_cords(x, y)
            self._grid[hs]=Hex(self.Game,self._batch,self.size)
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
            mx=1.73*self.size
            my=2*self.size*3/4
            mx2=mx/2

            xx=math.floor(mx * self._grid[i].position.x + mx2 * self._grid[i].position.y  + self.position.x)
            yy=math.floor(my * self._grid[i].position.y + self.position.y)

            self._grid[i].gen_hex(xx,yy)

        glLineWidth(8)
        self._batch.draw()
        glLineWidth(1)

    def loop(self,dt):

        pass