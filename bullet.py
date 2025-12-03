import pygame
import math


class Bullet:
    def __init__(self, s, x, y, r, sp, ang, sW, sH):
        self.screen = s
        self.x = x
        self.y = y
        self.radius = r
        self.speed = sp
        self.angle = ang
        self.color = (255, 255, 0)

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)