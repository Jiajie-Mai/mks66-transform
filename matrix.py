"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    output = new_matrix()

    for r in range( len ( output[0] ) ):
        for c in range( len ( output ) ):
            if ( r == c ):
                output[c][r] = 1
            else:
                output[c][r] = 0

    output[3] = [x,y,z,1]

    return output

def make_scale( x, y, z ):
    output = new_matrix()

    for r in range( len ( output[0] ) ):
        for c in range( len ( output ) ):
            if ( r == c ):
                if ( r == 0 ):
                    output[c][r] = x
                elif ( r == 1 ):
                    output[c][r] = y
                elif ( r == 2 ):
                    output[c][r] = z
                else:
                    output[c][r] = 1
            else:
                output[c][r] = 0

    return output

def make_rotX( theta ):
    output = new_matrix()

    output[0][0] = math.cos( theta )
    output[0][1] = math.sin( theta ) * -1
    output[1][0] = math.sin( theta )
    output[1][1] = math.cos( theta )
    output[2][2] = 1
    output[3][3] = 1

    return output


def make_rotY( theta ):
    output = new_matrix()

    output[1][1] = math.cos( theta )
    output[1][2] = math.sin( theta ) * -1
    output[2][1] = math.sin( theta )
    output[2][2] = math.cos( theta )
    output[0][0] = 1
    output[3][3] = 1

    return output

def make_rotZ( theta ):
    output = new_matrix()

    output[0][0] = math.cos( theta )
    output[2][0] = math.sin( theta )
    output[0][2] = math.sin( theta ) * -1
    output[2][2] = math.cos( theta )
    output[1][1] = 1
    output[3][3] = 1

    return output

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (math.floor(m1[0][r] * tmp[0]) +
                            math.floor(m1[1][r] * tmp[1]) +
                            math.floor(m1[2][r] * tmp[2]) +
                            math.floor(m1[3][r] * tmp[3]))
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
