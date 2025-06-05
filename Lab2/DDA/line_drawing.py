from OpenGL.GL import *

def dda_line(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points


def draw_line(x1, y1, x2, y2):
    points = dda_line(x1, y1, x2, y2)
    glColor3f(0, 1, 0)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2i(x, y)
    glEnd()
