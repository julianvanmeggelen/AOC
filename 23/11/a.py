if __name__ == "__main__":
    lines = open('input.txt').readlines()
    grid = [[*line.strip()] for line in lines]
    expand_rows = [i for i, row in enumerate(grid) if not '#' in row]
    expand_cols = [i for i in range(len(grid[0])-1) if not '#' in [row[i] for row in grid]]

    for n, i in enumerate(expand_rows): grid.insert(i+n, ['.']*len(grid[0]))

    for n, i in enumerate(expand_cols):
        for row in grid: row.insert(i+n, '.') 

    galaxy_pos = [(x,y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == '#']
    res = 0
    visited = set()
    for a in galaxy_pos:
        for b in galaxy_pos:
            if (a,b) not in visited and (b,a) not in visited and not a == b:
                visited.add((a,b))
                res += abs(a[0]-b[0]) + abs(a[1]-b[1])
    print(res)
   

   






    


     

