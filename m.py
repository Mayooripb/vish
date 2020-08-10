from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)


def plot_point(Point):
    x, y = Point
    glVertex2f(x, y)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    plot_point(Point)
    glEnd()
    glFlush()



def make_point(x, y):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'a_new_day')
    global Point
    X, Y = x, y
    glutDisplayFunc(display)
    init()
    glutMainLoop()
