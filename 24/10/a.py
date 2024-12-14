grid = [[int(el) for el in line.strip()] for line in open('input.txt').readlines()]



def find_unique_tops(x, y) -> set[tuple[int,int]]:
    print(x,y,grid[y][x])
    if grid[y][x] == 9:
        return [(x,y)]
    else:
        all_tops = set()
        for dx, dy in [(0,1), (1,0), (-1,0),(0, -1)]:
            if y+dy < len(grid) and y+dy>=0 and x+dx < len(grid[0]) and x+dx >= 0 and grid[y+dy][x+dx] == grid[y][x] + 1:
                all_tops = all_tops.union(find_unique_tops(x+dx, y+dy))
        return all_tops

total = 0
for y, line in enumerate(grid):
    for x, h in enumerate(line):
        if h == 0:
            total += len(find_unique_tops(x,y))
print(total)