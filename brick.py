from pyray import *

from entidy import Entidy


class Brick(Entidy):
    def __init__(self, x: float, y: float, sx: float, sy: floar, color: int = WHITE):
        super().__init__(x, y, sx, sy, color)

    def render(self):
        
