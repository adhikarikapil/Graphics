import math
from OpenGL.GL import *


def draw_bar(x1, y1, x2, y2):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()


def draw_filled_semicirle(cx, cy, r, segments=50):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments + 1):
        angle = math.pi * i / segments
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()


# def draw_make_hollow(cx, cy, r, segments=50):
#     glColor3f(1, 0, 0)
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex2f(cx, cy)
#     for i in range(segments + 1):
#         angle = math.pi * i / segments
#         x = cx + r * math.cos(angle)
#         y = cy + r * math.sin(angle)
#         glVertex2f(x, y)
#     glEnd()


def draw_K():
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 200)

    glPushMatrix()
    glTranslatef(8, 112, 0)
    glRotatef(-45, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 120)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(102, 5, 0)
    glRotatef(50, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 120)
    glPopMatrix()


def draw_A():
    glPushMatrix()
    glTranslatef(-3, 4, 0)
    glRotatef(-12, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 200)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(90, 0, 0)
    glRotatef(12, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 200)
    glPopMatrix()

    glColor3f(1, 1, 1)
    draw_bar(20, 90, 80, 110)


def draw_P():
    glPushMatrix()
    # glTranslatef()
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 200)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-140, 160, 0)
    glRotatef(-90, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_filled_semicirle(20, 150, 60)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-134, 160, 0)
    glRotate(-90, 0, 0, 1)
    glColor3f(0, 0, 0)
    draw_filled_semicirle(20, 150, 40)
    glPopMatrix()


def draw_I():
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 200)

    glPushMatrix()
    glTranslatef(60, 0, 1)
    glRotatef(90, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(60, 180, 1)
    glRotatef(90, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 100)
    glPopMatrix()


def draw_L():
    glPushMatrix()
    glTranslatef(-30, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 200)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(60, 0, 1)
    glRotatef(90, 0, 0, 1)
    glColor3f(1, 1, 1)
    draw_bar(0, 0, 20, 70)
    glPopMatrix()


def draw_name():
    glPushMatrix()
    glTranslatef(-280, -100, 0)

    glPushMatrix()
    draw_K()
    glTranslatef(120, 0, 0)

    draw_A()
    glTranslatef(120, 0, 0)

    draw_P()
    glTranslatef(120, 0, 0)

    draw_I()
    glTranslatef(120, 0, 0)

    draw_L()
    glTranslatef(120, 0, 0)
    glPopMatrix()

    glPopMatrix()
