from pyray import *


class Entidy():
    def __init__(self, x: float, y: float, sx: float, sy: float, color: int = WHITE):
        self.position = Vector2(x, y)
        self.size = Vector2(sx, sy)
        self.color = color

    def collisionLeft(self, other) -> bool:
        if (    _collisionLeft(self, other) and
                _collisionUp(self, other) and
                _collisionDown(self, other)):
            return True
        return False

    def collisionRight(self, other) -> bool:
        if (    _collisionRight(self, other) and
                _collisionUp(self, other) and
                _collisionDown(self, other)):
            return True
        return False

    def collisionUp(self, other) -> bool:
        if (    _collisionUp(self, other) and
                _collisionLeft(self, other) and
                _collisionRight(self, other)):
            return True
        return False

    def collisionDown(self, other) -> bool:
        if (    _collisionDown(self, other) and
                _collisionLeft(self, other) and
                _collisionRight(self, other)):
            return True
        return False

def _collisionLeft(entidy_1: Entidy, entidy_2: Entidy) -> bool:
    if entidy_1.position.x < entidy_2.position.x + entidy_2.size.x:
        return True
    return False

def _collisionRight(entidy_1: Entidy, entidy_2: Entidy) -> bool:
    if entidy_1.position.x + entidy_1.size.x > entidy_2.position.x:
        return True
    return False

def _collisionUp(entidy_1: Entidy, entidy_2: Entidy) -> bool:
    if entidy_1.position.y < entidy_2.position.y + entidy_2.size.y:
        return True
    return False

def _collisionDown(entidy_1: Entidy, entidy_2: Entidy) -> bool:
    if entidy_1.position.y + entidy_1.size.y > entidy_2.position.y:
        return True
    return False
