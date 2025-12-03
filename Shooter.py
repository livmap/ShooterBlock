import pygame

class Shooter:
    def __init__(self,s, r, sW, sH):
        self.radius = r
        self.x = sW / 2
        self.y = sH - r
        self.color = (0, 255, 255)

    def draw(self):
        pygame.draw.circle(s, self.color,(self.x,self.y), self.radius)

