grid = [line.strip() for line in open('input.txt').readlines()]
all_areas = []
dirs = [(1,0), (0,1), (-1,0), (0,-1)]
total = 0
for sy, line in enumerate(grid):
    for sx, val in enumerate(line):
        print(sx,sy,val)
        if (
            (sx == 0 or grid[sy][sx-1] != grid[sy][sx])
            and (sy == 0 or grid[sy-1][sx] != grid[sy][sx])
        ): 
            if any((sx, sy) in area for area in all_areas):
                continue
            print(val)
            area_points = []
            to_visit = [(sx,sy)]
            visited = []
            while len(to_visit) > 0:
                x, y = to_visit.pop()
                visited.append((x,y))
                if grid[y][x] == val:
                    area_points.append((x,y))
                    for dx, dy in dirs:
                        if (x+dx, y+dy) not in visited and (x+dx) < len(grid[0]) and x+dx>=0 and (y+dy) < len(grid) and y+dy>=0: 
                            to_visit.append((x+dx,y+dy))
            all_areas.append(area_points)
            surface = len(set(area_points))
            perim = sum([sum((x+dx,y+dy) not in area_points for dx, dy in dirs) for (x,y) in set(area_points)])
            total += perim * surface

print(total)
          