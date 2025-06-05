from OpenGL.GL import *

def plot_circle_points(xc, yc, x, y):
    glColor3f(0, 1, 0)
    glBegin(GL_POINTS)
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)
    glEnd()


def mid_point_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y = y -1
            p = p + ((2 * x) - (2 * y) + 1)
        plot_circle_points(xc, yc, x, y)
