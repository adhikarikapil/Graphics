import os
import time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import importlib
import name

last_modified = os.path.getmtime('name.py')

pygame.init()
display=(1920, 1080)
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

        
    new_modified = os.path.getmtime('name.py')
    if new_modified != last_modified:
        importlib.reload(name)
        last_modified = new_modified
        print("Reloaded!!!")

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    name.draw_name()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()