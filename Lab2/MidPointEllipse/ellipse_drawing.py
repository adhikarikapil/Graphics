from OpenGL.GL import *


def plot_ellipse_points(xc, yc, x, y):
    glColor3f(0, 1, 0)
    glBegin(GL_POINTS)
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glEnd()


def mid_point_ellipse(xc, yc, a, b):
    x = 0
    y = b

    a2 = a * a
    b2 = b * b
    two_a2 = 2 * a2
    two_b2 = 2 * b2

    p1 = b2 - (a2 * b) + (0.25 * a2)
    dx = 2 * b2 * x
    dy = 2 * a2 * y

    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        x += 1
        dx = dx + two_b2
        if p1 < 0:
            p1 = p1 + dx + b2
        else:
            y -= 1
            dy = dy - two_a2
            p1 = p1 + dx - dy + b2

    p2 = (b2) * (x + 0.5) ** 2 + (a2) * (y - 1) ** 2 - (a2 * b2)
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        y -= 1
        dy = dy - two_a2
        if p2 > 0:
            p2 = p2 + a2 - dy
        else:
            x += 1
            dx = dx + two_b2
            p2 = p2 + dx - dy + a2
