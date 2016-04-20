import pygame #imports the pre-coded pygame files which contain the settings for a game program to run
from pygame.locals import * #imports more specific files which are required for some of the lines of code below to run, but not all of them

from OpenGL.GL import * #imports all of the pre-coded OpenGL files required to run code from the OpenGL programming language
from OpenGL.GLU import * #imports more pre-coded OpenGL for more specific parts of the program

import random #imports a pre-coded set of randomisation routines 

vertices = ( #Assigning a variable to the vertices which can now be manipulated by calling that variable
    (1, -1, -1), #All of these vertices represent the position of the corners of the cube
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = ( #Assigning a variable to the edges so that they can be manipulated by calling the variable
    (0, 1), #These co-ordinates represent the position of the edges of the cube; where they connect to
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

surfaces = ( #Assigning a variable to the surfaces so they can be manipulated by calling the variable
    (0, 1, 2, 3), #These co-ordinates represent the positions of the corners which the surface needs to stretch across
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
    )

colour = ( #Assigning a variable to the colour scheme of the cube so that it can easily be changed and manipulated by calling the variable
    (1, 0, 0), #These represent the RGB values of the colour of the cube
    (1, 0, 1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 0, 0),
    )

ground_vertices = ( #Assigning a variable to the vertices of the ground/background of the window
    (-10, 0, 20), #These co-ordinates represent the position of the ground shape 
    (10, 0, 20),
    (-10, 0, -300),
    (10, 0, -300),
    )

def ground(): #This function is used to colour the ground and place it in the window
    glBegin(GL_QUADS)
    for vertex in ground_vertices: #The process below will happen for all of the vertices in the ground's assigned vertice co-ordinates
        glColor3fv((0, 0.5, 0.5)) #This sets the colour of the ground
        glVertex3fv(vertex) #Points to an array to pass the vertex co-ordinates to OpenGL
    glEnd()

def set_vertices(max_distance, min_distance = -20):
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1 * max_distance, min_distance)

    new_vertices = []

    for vert in vertices:
        new_vert = []
        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

def Cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colour[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (1200,900)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)

    #object_passed = False

    x_move = 0
    y_move = 0

    max_distance = 100

    cube_dict = {}

    for x in range(20):
        cube_dict[x] = set_vertices(max_distance)
    
    #glRotatef(1, 1, 1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = 0.3
                if event.key == pygame.K_RIGHT:
                    x_move = -0.3
##                if event.key == pygame.K_UP:
##                    y_move = -0.3
##                if event.key == pygame.K_DOWN:
##                    y_move = 0.3
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
##                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
##                    y_move = 0
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 4:
##                    glTranslatef(0, 0, 1.0)
##                if event.button == 5:
##                    glTranslatef(0, 0, -1.0)

        #glRotatef(1, 1, 3, 1)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        print(x)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glTranslate(x_move, y_move, .90)

        #ground()
        
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])

        deletye_list = []

        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                print("Passed a cube")
                #delete_list.append(each_cube)
                new_max = int(-1 * (camera_z - max_distance))
                cube_dict[each_cube] = set_vertices(new_max, int(camera_z))
                
            
        pygame.display.flip()
        pygame.time.wait(10)

main()    
pygame.quit()
quit()
    
