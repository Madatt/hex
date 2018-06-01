import pyglet
import game
import states.menu
import states.level

if __name__ == "__main__":

    Game = game.Game(1280,720)
    Game.add_state("Menu", states.menu.Menu)
    Game.add_state("Level", states.level.Level)
    Game.set_current("Level")
    Game.main_loop()
