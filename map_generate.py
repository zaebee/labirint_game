import random
import os

WALL = u'\u2588'
EMPTY = ' '

def _shape_maze(maze):
    """Returns size of maze as `(col, row)`."""
    return (
        max(maze.keys(), key=lambda x: x[1])[1] + 1, # width
        max(maze.keys(), key=lambda x: x[0])[0] + 1, # height,
    )

def init_maze(height=7, width=7):
    """Initialize maze with size height and width."""
    maze = {}
    for y in range(height):
        for x in range(width):
            dict_key = (x, y)
            maze[dict_key] = WALL
    return maze
 
def print_maze(maze):
    height, width = _shape_maze(maze)
    for y in range(height):
        for x in range(width):
            print(maze[(x, y)], end='')
        print()

     
def get_directions(x, y, maze=None, has_visited=None):
    """Gets direction to next cells from current (x, y)."""
    height, width = _shape_maze(maze)
    for col in range(1, height, 2):
        for row in range(1, width, 2):
            maze[(row, col)] = EMPTY
    
    has_visited = has_visited or [(x, y)]
    directions = []
    if y > 1 and (x, y - 2) not in has_visited:
        directions.append('up')
    if y < height - 1 and (x, y + 2) not in has_visited:
        directions.append('down')
    if x < height - 1 and (x + 2, y) not in has_visited:
        directions.append('right')
    if x > 1 and (x - 2, y) not in has_visited:
        directions.append('left')
    return directions  
    # has_visited.append(next_coords)
    # next_cell = random.choice(directions)
    # while True:
    # TODO: remove WALLs when move to direction.