from pyray import *

from entidy import Entidy


# TODO add mouse support

# ERROR the player collision wall isn't working


class Player(Entidy):
    def __init__(self,
                 sx: float, sy: float,
                 v: float = 1,
                 color: int = WHITE) -> None:
        super().__init__(get_screen_width() - sx, self.getPositionY(sy),
                         sx, sy, color)
        self.velocity = v

    @staticmethod
    def getPositionY(sy: float) -> int:
        return get_screen_height() - sy - 10
    
    def update(self) -> None:
        # Input
        if (    ( is_key_down(KEY_D) or is_key_down(KEY_RIGHT) ) and
                self.position.x + self.size.x < get_screen_width()):
            self.position.x += self.velocity
        elif (  ( is_key_down(KEY_A) or is_key_down(KEY_LEFT) ) and
                self.position.x > 0):
            self.position.x -= self.velocity

    def render(self) -> None:
        draw_rectangle(int(self.position.x), int(self.position.y), int(self.size.x), int(self.size.y), self.color)
