import random

import pygame
import sys

from shooter import Shooter
from enemy import Enemy

# Initialize pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600

# Create the window

background = (30, 30, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ShooterBlock")

sh = Shooter(screen, 50, WIDTH, HEIGHT)

enemies = []
enemyCount = 5
starterY = -100
enemyW = 40
enemyH = 40

for i in range(enemyCount):
    enemyColor = (random.randint(0, 255), 255, 0)
    enemySpeed = random.randint(1, 3) / 5
    enemies.append(Enemy(screen, starterY, enemyW, enemyH, enemyColor, enemySpeed, WIDTH, HEIGHT))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with a color
    screen.fill(background)
    sh.draw()
    for en in enemies:
        en.update()
    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()