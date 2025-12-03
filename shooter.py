import pygame

class Shooter:
    def __init__(self,s, r, sW, sH):
        self.radius = r
        self.x = sW / 2
        self.y = sH
        self.color = (0, 255, 255)
        self.screen = s

    def draw(self):
        pygame.draw.circle(self.screen, self.color,(self.x,self.y), self.radius)

