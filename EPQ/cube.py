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

def set_vertices(max_distance, min_distance = -20): #This method sets the range which each vertice can move by
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1 * max_distance, min_distance)

    new_vertices = [] #creates a list which the vertices can be added to and iterated through

    for vert in vertices: #For each vertice in the list the following code is applied
        new_vert = []
        new_x = vert[0] + x_value_change #Changes the value to whatever randomly generated value is added
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x) #Adds the new values to the list
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert) #Adds the list to the other list to make a nested list

    return new_vertices #Returns the final list to be used

def Cube(vertices): #This is the template for the actual cube which appears
    glBegin(GL_QUADS)
    for surface in surfaces: #This instantiates the surfaces created above
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colour[x]) #this makes the colour grade change across the surfaces of the cubes; for every 1 unit the hex colour value changes creating a rainbow effect
            glVertex3fv(vertices[vertex]) #Applies the vertex values to each vertice.
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex]) #This instantiates the vertices created above
    glEnd()

def main():
    pygame.init() #Initialises the pygame package
    display = (1200,900) #Sets the size of the window that will appear
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #does something to minimise frame rate

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40)

    #object_passed = False

    x_move = 0
    y_move = 0

    max_distance = 100

    cube_dict = {} #all this stuff decides the range that the cube can move

    for x in range(20):
        cube_dict[x] = set_vertices(max_distance)
    
    #glRotatef(1, 1, 1, 1)

    while True: #Sets a condition to keep the program running until another condition is met
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #If the user presses the left key this enables them to move the camera towards the left, like a movement control
                    x_move = 0.3
                if event.key == pygame.K_RIGHT: #same except the camera moves right
                    x_move = -0.3
                if event.key == pygame.K_UP: #Same except camera move up
                    y_move = -0.3 # the distance the camera moves per 'click'
                if event.key == pygame.K_DOWN: #camera moves down
                    y_move = 0.3
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0 #This makes the camera only able to move if the user presses the key, it doesn't keep going
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: #This enables the user to zoom in and out, or in this case speed up or slow down the cubes
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        #glRotatef(1, 1, 3, 1)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        print(x) #This prints all the maths stuff and coordinates of the cubes in the Python shell

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

main()    #this automatically runs the program
pygame.quit()
quit() #This closes the window when the user inputs to quit
    
