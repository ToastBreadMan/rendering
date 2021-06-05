import numpy as np
import pygame
import math

WIDTH = 700
HEIGHT = 700
run = True
projectionMatrix = np.array([[1,0,0],[0,1,0]])
angle = 0
position = [WIDTH/2,HEIGHT/2]
scaleFactor = 100
rotationAngle = 1
offset = 10

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('circle')

while run:
    rotationMatrixY = np.array([[math.cos(rotationAngle), 0, math.sin(rotationAngle)],
                                [0, 1, 0],
                                [-math.sin(rotationAngle), 0, math.cos(rotationAngle)]])

    rotationMatrixX = np.array([[1, 0, 0],
                                [0, math.cos(rotationAngle), -math.sin(rotationAngle)],
                                [0, math.sin(rotationAngle), math.cos(rotationAngle)]])

    rotationMatrixZ = np.array([[math.cos(rotationAngle), -math.sin(rotationAngle), 0],
                                [math.sin(rotationAngle), math.cos(rotationAngle), 0],
                                [0, 0, 1]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for donut in range(50):
        rotationMatrixY = np.array([[math.cos(donut), 0, math.sin(donut)],
                                    [0, 1, 0],
                                    [-math.sin(donut), 0, math.cos(donut)]])

        for angle in range(50):
                circle = np.array([1 * 3, 0, 0]) + np.array([1 * math.cos(angle/4), 1 * math.sin(angle/4), 0])

                points2d = np.dot(rotationMatrixY, circle)
                points2d = np.dot(rotationMatrixX, points2d)
                points2d = np.dot(rotationMatrixZ, points2d)
                points2d = np.dot(projectionMatrix, points2d)

                x = points2d[0] * scaleFactor + position[0]
                y = points2d[1] * scaleFactor + position[1]

                pygame.draw.circle(display, (255,0,210),(x,y),5)

        rotationAngle += 0.001

    pygame.display.update()
    display.fill((0,0,0))

pygame.quit()