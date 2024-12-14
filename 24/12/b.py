grid = [line.strip() for line in open('input.txt').readlines()]
m = len(grid)
n = len(grid[0])
total = 0
visited = set()
for i in range(m):
    for j in range(n):
        if (i, j) not in visited:
            plant = grid[i][j]
            region = set()
            queue = set([(i, j)])
            while queue:
                i, j = queue.pop()
                region.add((i, j))
                for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                    if (
                        x in range(m) and 
                        y in range(n) and 
                        grid[x][y] == plant and
                        (x, y) not in region and
                        (x, y) not in queue
                    ):
                        queue.add((x, y))
           
            for x, y in region:
                TL, L, BL, T, B, TR, R, BR = [
                    (
                        x+dx in range(m) and 
                        y+dy in range(n) and 
                        grid[x+dx][y+dy] == plant
                    )
                    for dx in [-1, 0, 1]
                    for dy in [-1, 0, 1] 
                    if dx or dy
                ]
                total += sum([
                    T and L and not TL, 
                    T and R and not TR, 
                    B and L and not BL, 
                    B and R and not BR, 
                    not (T or L),
                    not (T or R),
                    not (B or L),
                    not (B or R)
                ]) * len(region)

            visited |= region

print(total)