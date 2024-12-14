grid = [line.strip() for line in open('input.txt').readlines()]
m = len(grid)
n = len(grid[0])

def get_corners(i, j):
    NW, W, SW, N, S, NE, E, SE = [
        (
            i+x in range(m) and 
            j+y in range(n) and 
            grid[i+x][j+y] == plant
        )
        for x in [-1, 0, 1]
        for y in [-1, 0, 1] 
        if x or y
    ]
    return sum([
        N and W and not NW, 
        N and E and not NE, 
        S and W and not SW, 
        S and E and not SE, 
        not (N or W),
        not (N or E),
        not (S or W),
        not (S or E)
    ])

def is_same(i, j, plant):
    return (
        i in range(m) and 
        j in range(n) and 
        grid[i][j] == plant
    )

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
                    if (is_same(x, y, plant) and
                        (x, y) not in region and
                        (x, y) not in queue
                    ):
                        queue.add((x, y))

            corners = sum(get_corners(x, y) for x, y in region)
            total += corners * len(region)
            visited |= region

print(total)