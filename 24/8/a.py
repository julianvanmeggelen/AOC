freq_points: dict[str, list] = {}
for y, line in enumerate(open('input.txt').readlines()):
    for x, freq in enumerate(line):
        if freq != '.':
            if freq not in freq_points:
                freq_points[freq] = []
            freq_points[freq].append((x,y))
locs: set[tuple[int,int]] = set()
#print(freq_points)
for freq, points in freq_points.items():
    for  x1, y1  in points:
        for x2, y2 in points:
            if (x1,y1) != (x2,y2):
                dx = x2-x1
                dy = y2-y1
                for ax, ay in ((x1-dx, y1-dy), (x2+dx, y2+dy)):
                    if ax <= x and ax>=0 and ay>=0 and ay <=y:
                        print(ax, ay)
                        locs.add((ax,ay))
print(len(locs))
               


