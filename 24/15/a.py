grid = []
lines = open('input.txt').readlines()
grid = [list(line.strip()) for line in lines if line[0] == '#']
moves = ''.join([line.strip() for line in lines if line[0] != '#'])

y = [i for i, line in enumerate(grid) if '@' in line][0]
x = grid[y].index('@')


def do_move(x, y, dx, dy):
    if grid[y+dy][x+dx] == '.':
        grid[y+dy][x+dx] = grid[y][x]
        grid[y][x] = '.'
        return True
    
    if grid[y+dy][x+dx] == 'O':
        if do_move(x+dx, y+dy, dx, dy):
            do_move(x,y,dx,dy)
            return True
    
    if grid[y+dy][x+dx] == '#':
        return False
    
dirs = {'^': (0, -1), '>': (1, 0), '<': (-1, 0), 'v': (0, 1)}
for move in moves:
    dx, dy = dirs[move]
    if do_move(x,y,dx,dy):
        x,y = x+dx, y+dy

total = 0
for y, line in enumerate(grid):
    for x, val in enumerate(line):
        if val == 'O':
            total+=x+(y*100)
print(total)


   

