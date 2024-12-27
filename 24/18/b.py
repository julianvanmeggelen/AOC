from heapq import heappop, heappush
all_corr = [(int((s:=line.split(','))[0]), int(s[1])) for line in open('input.txt').readlines()]
w = 70

for i in range(1024, len(all_corr)):
    corr = set(all_corr[:i])
    heap  = [(0, 0, 0)]
    visited = set()
    found = False
    while heap:
        score, x, y  = heappop(heap)
        if (x, y) in visited:
            continue 
        if (x,y) == (w, w):
            found=True
            break
        visited.add((x, y))
        
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            if ((x+dx, y+dy) not in corr) and ((x+dx,y+dy) not in visited ) and (x+dx<=w and y+dy<=w and x+dx>=0 and y+dy>=0):
                heappush(heap, (score+1, x+dx, y+dy))
    if not found:
        print(all_corr[:i][-1])
        break
