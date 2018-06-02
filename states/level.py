import states.state
import entities.hexgrid
import entities.vector2d


class Level(states.state.State):
    def __init__(self, g):
        super().__init__(g)

        self.grid=entities.hexgrid.HexGrid(g,100,80,48,1,1)

    def run(self, dt):
        pass


    def draw(self):
        self.Game.clear()
        self.grid.draw()
        self.Game.flip()


