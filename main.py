from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 1, 0 ]
edges = []
matrix = new_matrix()
transform = new_matrix()

#parse_file( 'script', edges, transform, screen, color )

i = 0
while i < 500:
    add_edge( matrix, 0, 0 + i, 0, 250, 250 + i, 0 )
    add_edge( matrix, 0, 0 + i, 0, 500, 0 + i, 0 )
    add_edge( matrix, 250, 250 + i, 0, 500, 0 + i, 0 )
    color[1] = 500 - i 
    draw_lines( matrix, screen, color )
    transform = make_scale( 1, 2, 1 )
    matrix_mult( transform, matrix )
    i += 100


save_extension(screen, 'img.png')
display(screen)


