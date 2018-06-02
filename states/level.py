import states.state
import entities.hexgrid
import entities.vector2d


class Level(states.state.State):
    def __init__(self,g):
        super().__init__(g)

    def init(self):
        self.grid=entities.hexgrid.HexGrid(self.Game,100,80,48,14,8)
        self.Game.view.x=0
        self.Game.view.y=0



    def run(self, dt):

        if self.Game.mouse_status_drag[0][0]:
            self.Game.view.x-=self.Game.mouse_status_drag[0][2].x
            self.Game.view.y-=self.Game.mouse_status_drag[0][2].y




        pass


    def draw(self):

        self.Game.draw_view_start()
        self.grid.draw()
        self.Game.draw_view_stop()


