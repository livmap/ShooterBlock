import random

import pygame.draw

class Enemy:
    def __init__(self,s, y, w, h, clr, sp, sW, sH):
        self.w = w
        self.h = h
        self.color = clr
        self.speed = sp
        self.x = random.randint(0, sW - self.w)
        self.yInit = y
        self.y = y
        self.screenWidth = sW
        self.screenHeight = sH
        self.screen = s

    def move(self):
        self.y += self.speed

    def relocate(self):
        self.x = random.randint(0, self.screenWidth - self.w)
        self.y = self.yInit

    def update(self):
        if self.y < self.screenHeight:
            self.move()
        else:
            self.relocate()
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.w, self.h])