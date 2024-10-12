from pyray import *

from ball import Ball
import ball

from player import Player


# TODO add a SCALER to multiple the size of the entity's per the screen resolutions


class Game:
    def __init__(self) -> None:
        init_window(640, 360, "Breakout")
        set_target_fps(60)
        
        self.state: bool = True

        self.player = Player(70, 15, 6, GRAY)
        ball = Ball.spawn(5, 2, WHITE)
        Ball.total.append(ball)

    def Update(self) -> None:
        if window_should_close():
            self.state = False
        if is_key_pressed(KEY_R):
            Ball.total.append(Ball.spawn(5, 2, WHITE))
        
        self.player.update()
        ball.updateAll(Ball.total, self.player)

    def Render(self) -> None:
        begin_drawing()
        
        clear_background(BLACK)
        
        self.player.render()
        ball.renderAll(Ball.total)

        end_drawing()

    def Loop(self) -> None:
        while self.state:
            self.Update()
            self.Render()
        close_window()


if __name__ == "__main__":
    game = Game()
    game.Loop()
