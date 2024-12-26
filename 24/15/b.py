grid = []
lines = open('input.txt').readlines()
grid = [list(line.strip().replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')) for line in lines if line[0] == '#']
moves = ''.join([line.strip() for line in lines if line[0] != '#'])


import sys
sys.setrecursionlimit(100)

for y, line in enumerate(grid):
    print(''.join(line))


def move_possible(x, y, dx, dy, skip_sidecheck=False):
    print('move_possible', x,y, dx, dy, grid[y][x], skip_sidecheck)
        
    if not skip_sidecheck:
        if grid[y][x] == '[' and dy != 0:
            return move_possible(x+1, y, dx, dy, True) and move_possible(x, y+dy, dx, dy)

        if grid[y][x] == ']' and dy != 0:
            print('here')
            return move_possible(x-1, y, dx, dy, True) and move_possible(x, y+dy, dx, dy)

    
    if grid[y][x] == '.':
        return True
    if grid[y+dy][x+dx] == '#':
        return False
    # if currently_in_place == '[' or currently_in_place == ']':
    #     print('here')
    return move_possible(x+dx, y+dy, dx, dy)

    return True
           
    
def do_move(x, y, dx, dy, skip_sidecheck=False):    
    if grid[y][x]=='.' or grid[y][x]=='#':
        return
    if grid[y][x] == '[' and dy !=0 and not skip_sidecheck:
        do_move(x+1,y,dx,dy, True)
    if grid[y][x] == ']' and dy !=0 and not skip_sidecheck:
        do_move(x-1,y,dx,dy, True)

    do_move(x+dx,y+dy,dx,dy)

    grid[y+dy][x+dx] = grid[y][x]
    grid[y][x] = '.'

    
y = [i for i, line in enumerate(grid) if '@' in line][0]
x = grid[y].index('@')
dirs = {'^': (0, -1), '>': (1, 0), '<': (-1, 0), 'v': (0, 1)}
# for move in moves:
# while True:
#     moves = input('move')
for move in moves:
    dx, dy = dirs[move]
    print(x,y,dx,dy, move)
    if move_possible(x,y,dx,dy):
        do_move(x,y,dx,dy)
        x,y = x+dx, y+dy
    # for line in grid:
    #     print(''.join(line))

for line in grid:
    print(''.join(line))

total = 0
for y, line in enumerate(grid):
    for x, val in enumerate(line):
        if val == '[':
            total+=x+(y*100)
print(total)


   

