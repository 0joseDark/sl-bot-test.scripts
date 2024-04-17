# pip install tk
# pip install PyOpenGL PyOpenGL_accelerate

import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image

class Image3DViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.root.title("Image 3D Viewer")

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.gl_frame = self.canvas.winfo_id()

        glutInit()

        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        self.glut_window = glutCreateWindow(b"Image 3D Viewer")

        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.width / self.height), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        self.load_image("example.jpg")  # Carregue sua imagem aqui

        self.root.after(10, self.draw)
        self.root.mainloop()

    def load_image(self, filename):
        img = Image.open(filename)
        img_data = np.array(list(img.getdata()), np.uint8)

        glEnable(GL_TEXTURE_2D)
        glGenTextures(1, glGenTextures)
        glBindTexture(GL_TEXTURE_2D, glGenTextures[0])
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-1, -1, 0)
        glTexCoord2f(1, 0)
        glVertex3f(1, -1, 0)
        glTexCoord2f(1, 1)
        glVertex3f(1, 1, 0)
        glTexCoord2f(0, 1)
        glVertex3f(-1, 1, 0)
        glEnd()

        glutSwapBuffers()
        self.root.after(10, self.draw)

if __name__ == "__main__":
    viewer = Image3DViewer(800, 600)
