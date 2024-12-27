from heapq import heappop, heappush

grid = [line.strip() for line in open('input.txt').readlines()]
y0 = [i for i, line in enumerate(grid) if 'S' in line][0]
yt = [i for i, line in enumerate(grid) if 'E' in line][0]
x0 = grid[y0].index('S')
xt = grid[yt].index('E')

heap  = [(0, x0, y0, 1, 0, ())]
visited = set()
best= float('inf')
all_solutions = []
while heap:
    score, x, y, dx, dy, trace = heappop(heap)
    if (x,y) == (xt, yt):
        if score <= best:
            all_solutions.append((score, x, y, dx, dy, (*trace, (x,y))))
        continue

    visited.add((x, y, dx, dy))

    if grid[y+dy][x+dx] in ('.', 'E') and (x+dx,y+dy,dx,dy) not in visited:
        heappush(heap, (score+1, x+dx, y+dy, dx, dy, (*trace, (x,y))))

    if (x,y,dy,-dx) not in visited:
        heappush(heap, (score+1000, x, y, dy, -dx, (*trace, (x,y))))

    if (x,y,-dy,dx) not in visited:
        heappush(heap, (score+1000, x, y, -dy, dx, (*trace, (x,y))))

all_solutions=[el for el in all_solutions if el[0] ==min(sol[0] for sol in all_solutions)]
all_points= set(point for solution in all_solutions for point in solution[5])
print(len(all_points))









