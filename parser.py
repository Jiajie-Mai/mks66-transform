from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):

    f = open(fname)
    s = f.read()
    w = s.split()
    i = 0

    #opens files and parses through them
    #a ==> x0 ==> y0 ==> z0 ==> x1 ==> y1 ==> z1

    while i < len(w):
        if (w[i] == "line"):
            add_edge(points,int(w[i+1]),int(w[i+2]),int(w[i+3]),int(w[i+4]),int(w[i+5]),int(w[i+6]))
            i += 7
        elif (w[i] == "scale"):
            matrix_mult(make_scale(int(w[i+1]),int(w[i+2]),int(w[i+3])),transform)
            i += 4
        elif (w[i] == "translate"):
            matrix_mult(make_translate(int(w[i+1]),int(w[i+2]),int(w[i+3])),transform)
            i += 4
        elif (w[i] == "rotate"):
            if (w[i+1] == "x"):
                matrix_mult(make_rotX(int(w[i+2])),transform)
            elif (w[i+1] == "y"):
                matrix_mult(make_rotY(int(w[i+2])),transform)
            else:
                matrix_mult(make_rotZ(int(w[i+2])),transform)
            i += 3
        elif (w[i] == "apply"):
            matrix_mult(transform,points)
            for x in range(len(points)):
                for y in range(4):
                    points[x][y] = int(points[x][y])
            i += 1
        elif (w[i] == "display"):
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
            i += 1
        elif (w[i] == "save"):
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,w[i+1])
            i += 2
        else:
            f.close()

