import random

import pygame
import sys

from bullet import Bullet
from shooter import Shooter
from enemy import Enemy
from utilities import collision

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

bullets = []
bulletRadius = 5
coolDown = 250

# Main game loop
running = True
clock = pygame.time.Clock()

currentTime = 0
prevTime = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sh.turn(5)
    if keys[pygame.K_RIGHT]:
        sh.turn(-5)
    if keys[pygame.K_SPACE]:
        currentTime = pygame.time.get_ticks()
        if currentTime > prevTime + coolDown:
            bullets.append(Bullet(screen, sh.aimX, sh.aimY, bulletRadius, 5, sh.angle, WIDTH, HEIGHT))
            prevTime = pygame.time.get_ticks()


    # Fill the screen with a color
    screen.fill(background)
    sh.draw()
    for b in bullets:
        if b.x < 0 or b.x > WIDTH:
            if b.y < 0 or b.y > HEIGHT:
                bullets.remove(b)
        b.draw()
    for en in enemies:
        for b in bullets:
            if collision(b.x, b.y, b.radius, en.x, en.y, en.w, en.h):
                bullets.remove(b)
                en.life -= b.damage

        if  en.life <= 0:
            enemies.remove(en)
        en.update()
    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()