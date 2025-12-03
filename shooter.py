import pygame
import math

class Shooter:
    def __init__(self,s, r, sW, sH):
        self.radius = r
        self.x = sW / 2
        self.y = sH
        self.color = (0, 255, 255)
        self.screen = s
        self.angle = 90
        self.aimColor = (255, 0, 0)

    def turn(self, amount):
        self.angle += amount

    def draw(self):
        aimX = self.x + (self.radius - 10) * math.cos(math.radians(self.angle))
        aimY = self.y - (self.radius - 10) * math.sin(math.radians(self.angle))


        pygame.draw.circle(self.screen, self.color,(self.x,self.y), self.radius)
        pygame.draw.circle(self.screen, self.aimColor, (int(aimX), int(aimY)), (self.radius / 10))

