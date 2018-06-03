import states.state
import entities.hexgrid
import entities.vector2d


class Level(states.state.State):
    def __init__(self,g):
        super().__init__(g)

    def init(self):
        self.grid=entities.hexgrid.HexGrid(self.Game,00,0,48,14,8)
        self.grid2=entities.hexgrid.HexGrid(self.Game,100,100,48,1,2)
        self.Game.view.x=0
        self.Game.view.y=0



    def run(self, dt):

        if self.Game.mouse_status_drag[0][0]:
            self.Game.view.x-=self.Game.mouse_status_drag[0][2].x
            self.Game.view.y-=self.Game.mouse_status_drag[0][2].y

        ps=self.grid.pixel_to_hex(self.Game.mouse_position.x,self.Game.mouse_position.y)
        self.grid.add_hex(ps.x,ps.y)


        pass


    def draw(self):

        self.Game.draw_view_start()
        self.grid.draw()
        self.Game.draw_view_stop()
        self.grid2.draw()


