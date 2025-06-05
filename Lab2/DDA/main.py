import os
import pygame
from pygame.locals import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import importlib
import line_drawing

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

last_modified = os.path.getmtime('line_drawing.py')

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

    new_modified = os.path.getmtime('line_drawing.py')
    if new_modified != last_modified:
        importlib.reload(line_drawing)
        last_modified = new_modified
        print('Reloaded!!!')

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    line_drawing.draw_line(x1, y1, x2, y2)
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()