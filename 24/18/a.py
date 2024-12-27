from heapq import heappop, heappush
corr = set((int((s:=line.split(','))[0]), int(s[1])) for line in open('input.txt').readlines()[:1024])
w = 70
heap  = [(0, 0, 0)]
visited = set()
while heap:
    score, x, y  = heappop(heap)
    if (x, y) in visited:
        continue 
    if (x,y) == (w, w):
        break
    visited.add((x, y))
    
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        if ((x+dx, y+dy) not in corr) and ((x+dx,y+dy) not in visited ) and (x+dx<=w and y+dy<=w and x+dx>=0 and y+dy>=0):
            heappush(heap, (score+1, x+dx, y+dy))
print(score)









