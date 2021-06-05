import numpy as np
import pygame
import math

WIDTH = 500
HEIGHT = 500
run = True
scaleFactor = 100
points = []
position = [WIDTH/2,HEIGHT/2]
angle = 0

projectionMatrix = np.array([[1,0,0],
                             [0,1,0]])

#array should not have all zero points
points.append(np.array([-1,-1,-1]))
points.append(np.array([1,-1,-1]))
points.append(np.array([1,1,-1]))
points.append(np.array([-1,1,-1]))
points.append(np.array([-1,-1,1]))
points.append(np.array([1,-1,1]))
points.append(np.array([1,1,1]))
points.append(np.array([-1,1,1]))

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game')


def connect(f, s, points2d):
    x = points2d[f]
    y = points2d[s]
    pygame.draw.line(display, (255,210,0), (x[0] * scaleFactor + position[0], x[1] * scaleFactor + position[1]),(y[0] * scaleFactor + position[0], y[1] * scaleFactor + position[1]))


while run:
    points2d = []
    rotationMatrixX = np.array([[1, 0, 0],
                                [0, math.cos(angle), -math.sin(angle)],
                                [0, math.sin(angle), math.cos(angle)]])
    rotationMatrixY = np.array([[math.cos(angle), 0, math.sin(angle)],
                                [0, 1, 0],
                                [-math.sin(angle), 0, math.cos(angle)]])
    rotationMatrixZ = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 0, 1]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for point in points:
        point2d = np.dot(rotationMatrixZ, point)
        point2d = np.dot(rotationMatrixY, point2d)
        point2d = np.dot(rotationMatrixX, point2d)
        points2d.append(point2d)

        x = point2d[0]
        y = point2d[1]
        pygame.draw.circle(display, (255, 210, 0), (x * scaleFactor + position[0], y * scaleFactor + position[1]), 3)

    for i in range(4):
       connect(i, (i+1) % 4, points2d)
       connect(i+4, ((i+1) % 4)+4, points2d)
       connect(i, i+4, points2d)

    pygame.display.update()
    display.fill((0,0,0))
    angle += 0.001
    points2d = []



pygame.quit()