from heapq import heappop, heappush

grid = [line.strip() for line in open('input.txt').readlines()]
y0 = [i for i, line in enumerate(grid) if 'S' in line][0]
yt = [i for i, line in enumerate(grid) if 'E' in line][0]
x0 = grid[y0].index('S')
xt = grid[yt].index('E')

heap  = [(0, x0, y0, 1, 0)]
visited = set()

while heap:
    score, x, y, dx, dy = heappop(heap)
    if (x,y) == (xt, yt):
        break
    
    visited.add((x, y, dx, dy))

    if grid[y+dy][x+dx] in ('.', 'E') and (x+dx,y+dy,dx,dy) not in visited:
        heappush(heap, (score+1, x+dx, y+dy, dx, dy))

    if (x,y,dy,-dx) not in visited:
        heappush(heap, (score+1000, x, y, dy, -dx))

    if (x,y,-dy,dx) not in visited:
        heappush(heap, (score+1000, x, y, -dy, dx))

print(score)









