import os
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import importlib
import ellipse_drawing

xc = 0
yc = 0
a = int(input("Enter semi-major axis: "))
b = int(input("Enter semi-minor axis: "))

last_modified = os.path.getmtime('ellipse_drawing.py')

pygame.init()
display = (1920, 1080)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glViewport(0, 0, display[0], display[1])
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-960, 960, -540, 540)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glClearColor(0, 0, 0, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_modified = os.path.getmtime('ellipse_drawing.py')
    if new_modified != last_modified:
        importlib.reload(ellipse_drawing)
        last_modified = new_modified
        print("Reloaded!!")

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    ellipse_drawing.mid_point_ellipse(xc, yc, a, b)
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()