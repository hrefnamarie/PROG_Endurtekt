# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def print_grid(grid):
    for row in grid:
        ret_str = ""
        for numb in row:
            ret_str += "{} ".format(numb)
        print(ret_str)


def make_move(move, pos):
    x, y = pos
    if move == UP:
        if x == 0:
            new_pos = [4, y]
        else:
            new_pos = [x-1, y]
    elif move == DOWN:
        if x == 4:
            new_pos = [0, y]
        else:
            new_pos = [x+1, y]
    elif move == LEFT:
        if y == 0:
            new_pos = [x, 4]
        else:
            new_pos = [x, y-1]
    elif move == RIGHT:
        if y == 4:
            
            new_pos = [x, 0]
        else:
            new_pos = [x, y+1]

    return new_pos

def set_grid(grid, pos, new_pos):
    grid[pos[0]][pos[1]] = EMPTY
    grid[new_pos[0]][new_pos[1]] = POSITION

grid = initialize_grid()
print_grid(grid)
pos = [0,0]
while True:
    move = get_move()
    if move == QUIT:
        quit()
    new_pos = make_move(move, pos)
    set_grid(grid, pos, new_pos)
    pos = new_pos
    print_grid(grid)
