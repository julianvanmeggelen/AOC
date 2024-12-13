import copy

grid = [list(line.strip()) for line in open('input.txt')]
y = [i for i,line  in enumerate(grid) if '^' in line][0]
x = grid[y].index('^')
dx, dy = 0, -1
unique_coord = set()
while True:
    try:
        unique_coord.add((x,y))
        while grid[y+dy][x+dx] ==  '#':
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    except IndexError:
        break

print(len(unique_coord))