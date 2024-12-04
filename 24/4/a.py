a = [line.strip() for line in open('input.txt').readlines()]

curr = []
word="XMAS"
nrows = len(a)
ncols = len(a[0])
def search(x:int, y:int, dx: int, dy: int) -> bool:
    global curr
    curr+=[(x,y)]
    for i, c in enumerate(word):
        nx = x+dx*i
        ny= y+dy*i
        if nx < 0 or ny < 0 or nx >= ncols or ny >= nrows:
            return False
        if a[ny][nx] != c:
            return False
    return True
    
total = 0
for y in range(nrows):
    for x in range(ncols):
        if a[y][x] == 'X':
            total += search(x,y,1,1)
            total += search(x,y,0,1)
            total += search(x,y,0,-1)
            total += search(x,y,1,0)
            total += search(x,y,-1,0)
            total += search(x,y,1,-1)
            total += search(x,y,-1,1)
            total += search(x,y,-1,-1)
           
print(total)
