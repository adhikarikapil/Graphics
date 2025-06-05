from OpenGL.GL import *


def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x, y = x1, y1

    if dx > dy:
        err = 2 * dy - dx
        for _ in range(dx):
            points.append((x, y))
            x += sx
            if err < 0:
                err = err + 2 * dy
            else:
                y += sy
                err = err + ((2 * dy) - (2 * dx))
    else:
        err = 2 * dx - dy
        for _ in range(dy):
            points.append((x, y))
            y += sy
            if err < 0:
                err = err + 2 * dx
            else:
                x += sx
                err = err + ((2 * dx) - (2 * dy))
    
    points.append((x2, y2))
    return points


def draw_line(x1, y1, x2, y2):
    points = bresenham_line(x1, y1, x2, y2)
    glColor3f(0, 1, 0)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(float(x), float(y))
    glEnd()

