from pyray import *
from random import random
from math import sqrt


from entidy import Entidy


# ERROR when the ball hits player's left or right side it don't invert velocity


class Ball(Entidy):
    total = []

    def __init__(self,
                x: float, y: float,
                radius: float,
                vx: float, vy: float,
                color: int) -> None:
        super().__init__(x, y, radius, radius, color)
        self.velocity = Vector2(vx, vy)
        self.acce = 2
        self.alive = True
        
    @classmethod
    def spawn(cls, radius: float = 1, velo: float = 1, color: int = WHITE):
        """ Automatic set's the x and y, dx and dy """
        x = get_screen_width() / 2
        y = get_screen_height() / 2
        vx = random() * velo
        vy = random() * velo
        return cls(x, y, radius, vx, vy, color)

    def collisionWall(self):
        if (    self.position.x > get_screen_width() - self.size.x or
                self.position.x < self.size.x):
            self.velocity.x *= -1
       
        if self.position.y < self.size.y:
            self.velocity.y *= -1
        elif self.position.y > get_screen_height() - self.size.y:
            self.alive = False

    def collisionBalls(self, balls: list):
        for ball in balls:
            if collisionBall(self, ball):
                self.velocity.x *= -1 
                self.velocity.y *= -1
                ball.velocity.x *= -1
                ball.velocity.y *= -1

    def collisionPlayer(self, player):
        if self.collisionDown(player):
            self.velocity.y *= -1
        if (  self.collisionLeft(player) and
                self.collisionRight(player)):
            self.velocity.x *= -1
    
    def update(self, player, balls: list) -> None:
        self.position.x += self.velocity.x + self.acce * 0.2
        self.position.y += self.velocity.y + self.acce * 0.2

        self.collisionWall()
        self.collisionPlayer(player)
        self.collisionBalls(balls)

    def render(self) -> None:
        draw_ellipse(int(self.position.x), int(self.position.y),
                     int(self.size.x), int(self.size.y), self.color)


def collisionBall(ball_1: Ball, ball_2: Ball):
    def distance(position_1: Vector2, position_2: Vector2):
        distance_x = position_1.x - position_2.x
        distance_y = position_1.y - position_2.y

        return sqrt(distance_x * distance_x + distance_y * distance_y )
    
    total_radius = ball_1.size.x + ball_2.size.x
    return distance(ball_1.position, ball_2.position) <= total_radius

def updateAll(balls: list[Ball], player) -> None:
    for i in range(len(balls) - 1, -1, -1):
        ball = balls[i]
        ball.update(player, balls)
        if not balls[i].alive:
            balls.pop(i)


def renderAll(balls: list[Ball]):
    for ball in balls:
        ball.render()
