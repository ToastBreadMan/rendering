import numpy as np
import pygame
import math

WIDTH = 500
HEIGHT = 500
run = True
scaleFactor = 100
position = [WIDTH/2, HEIGHT/2]
angle = 0

projectionMatrix = np.array([[1,0,0], [0,1,0]])
points = []

points.append(np.array([-1,1,0]))
points.append(np.array([1,1,0]))
points.append(np.array([1,-1,0]))
points.append(np.array([-1,-1,0]))
points.append(np.array([0,0,1]))
points.append(np.array([0,0,-1]))

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('pyramid')


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
        point2d = np.dot(rotationMatrixX,point)
        point2d = np.dot(rotationMatrixY, point2d)
        point2d = np.dot(rotationMatrixZ, point2d)
        point2d = np.dot(projectionMatrix, point2d)
        points2d.append(point2d)

        x = point2d[0] * scaleFactor + position[0]
        y = point2d[1] * scaleFactor + position[1]
        pygame.draw.circle(display, (255,210,0), (x,y), 5)

    """
    connect(0,1,points2d)
    connect(0,4,points2d)
    connect(0,5,points2d)

    connect(1,2,points2d)
    connect(1,4,points2d)
    connect(1, 5, points2d)

    connect(2,3, points2d)
    connect(2,4,points2d)
    connect(2, 5, points2d)

    connect(3,0,points2d)
    connect(3,4,points2d)
    connect(3, 5, points2d)
    """

    pygame.display.update()
    display.fill((0,0,0))
    angle += 0.001

pygame.quit()
