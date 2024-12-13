import copy

grid = [list(line.strip()) for line in open("input.txt")]
sy = [i for i, line in enumerate(grid) if "^" in line][0]
sx = grid[sy].index("^")


total = 0
for block_x in range(len(grid[0])):
    for block_y in range(len(grid)):
        print(block_x, block_y)
        if (block_x, block_y) == (sx, sy):
            continue
        prev = grid[block_y][block_x]
        grid[block_y][block_x] = '#'
        dx, dy = 0, -1
        unique_coord = set()
        x,y = sx, sy
        while x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
            unique_coord.add((x, y, dx, dy))
            while (
                y + dy >= 0
                and y + dy < len(grid)
                and x + dx >= 0
                and x + dx < len(grid[0])
                and grid[y + dy][x + dx] == "#"
            ):
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
            if (x,y,dx,dy) in unique_coord:
                total+=1
                break
        grid[block_y][block_x] = prev

print(total)