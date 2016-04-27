from OpenGL.GL import shaders
from OpenGL.arrays import vbo
from OpenGL.GL import *
from OpenGL.raw.GL.ARB.vertex_array_object import glGenVertexArrays, \
                                                  glBindVertexArray
#All of the above are specific parts of the package which contains the preset code used to make it compatible with Python
import pygame #This is the Python game package

import numpy as np #This is the Python numbers package

def run(): #this function contains everything which creates the triangle and is called at the bottom
    pygame.init()
    screen = pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)#This sets the size of the window which will open when the program runs

    #Creates the VBO (Vertex Buffer Object to store data about the object (triangle))
    vertices = np.array([[0,1,0],[-1,-1,0],[1,-1,0]], dtype='f')
    vertexPositions = vbo.VBO(vertices)

    #Creates the index buffer object
    indices = np.array([[0,1,2]], dtype=np.int32)
    indexPositions = vbo.VBO(indices, target=GL_ELEMENT_ARRAY_BUFFER)

    #Creates the shaders
    VERTEX_SHADER = shaders.compileShader("""
    #version 330
    layout(location = 0) in vec4 position;
    void main()
    {
        gl_Position = position;
    }
    """, GL_VERTEX_SHADER)
    #These shaders set the colour of the triangle (in this case to lime green)
    FRAGMENT_SHADER = shaders.compileShader("""
    #version 330
    out vec4 outputColor;
    void main()
    {
        outputColor = vec4(0.0f, 1.0f, 0.0f, 1.0f);
    }
    """, GL_FRAGMENT_SHADER)

    shader = shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER) #This applies all of the attributers of hte triangle object to a variable which can be called to run instantiate the object

    #The draw loop
    while True:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glUseProgram(shader) #Instantiates the triangle object

        indexPositions.bind() #Binds hte index as the primary index so the program doesn't get confused (if there was more than one object)

        vertexPositions.bind() #Binds the vertex as above
        glEnableVertexAttribArray(0);
        glVertexAttribPointer(0, 3, GL_FLOAT, False, 0, None)

        #glDrawArrays(GL_TRIANGLES, 0, 3) 
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, None) #The triangle is a preset shape so can be drawn using hte PyOpenGL functions

        # Show the screen
        pygame.display.flip()

run() #This calls the run function which contains all the code to create the triangle

