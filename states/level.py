import states.state
import entities.hexgrid
import entities.vector2d


class Level(states.state.State):
    def __init__(self, g):
        super().__init__(g)

        self.grid=entities.hexgrid.HexGrid(g,100,80,48,14,8)

    def run(self, dt):

        self.Game.view.x+=32*dt

        pass


    def draw(self):

        self.Game.draw_view_start()
        self.grid.draw()
        self.Game.draw_view_stop()
        self.grid.draw()


