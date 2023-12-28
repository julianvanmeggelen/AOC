c = 10**6
if __name__ == "__main__":
    lines = open('input.txt').readlines()
    grid = [[*line.strip()] for line in lines]
    expand_rows = [i for i, row in enumerate(grid) if not '#' in row]
    expand_cols = [i for i in range(len(grid[0])-1) if not '#' in [row[i] for row in grid]]
    galaxy_pos = [(x,y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == '#']
    res = 0
    visited = set()
    for a in galaxy_pos:
        for b in galaxy_pos:
            if (a,b) not in visited and (b,a) not in visited and not a == b:
                range_x = min(a[0],b[0]), max(a[0],b[0])
                expands_x = len([i for i in expand_cols if i> range_x[0] and i< range_x[1]])
                range_y =  min(a[1],b[1]), max(a[1],b[1])
                expands_y = len([i for i in expand_rows if i> range_y[0] and i< range_y[1]])
                visited.add((a,b))
                res += (range_x[1] - range_x[0]) + (range_y[1] - range_y[0]) + (expands_x + expands_y) * (c-1) 

   

   






    


     

