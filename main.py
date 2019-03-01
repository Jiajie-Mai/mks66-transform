from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
matrix = new_matrix()

transform = make_rotZ(30)
print_matrix(transform)

add_edge(matrix,1,2,3,4,5,6)
add_edge(matrix,7,8,9,10,11,12)
print_matrix(matrix)

matrix_mult(transform,matrix)
print_matrix(matrix)

parse_file( 'script', edges, transform, screen, color )
