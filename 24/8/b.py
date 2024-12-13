freq_points: dict[str, list] = {}
for y, line in enumerate(open('input.txt').readlines()):
    for x, freq in enumerate(line):
        if freq != '.':
            if freq not in freq_points:
                freq_points[freq] = []
            freq_points[freq].append((x,y))
locs: set[tuple[int,int]] = set()
for freq, points in freq_points.items():
    for  x1, y1  in points:
        for x2, y2 in points:
            if (x1,y1) != (x2,y2):
                dx = x2-x1
                dy = y2-y1
                ax,ay = x1,y1
                while True:
                    ax, ay = (ax-dx, ay-dy)
                    if ax > x or ax<0 or ay<0 or ay >y:
                        break
                    locs.add((ax,ay))
                ax,ay = x1,y1
                while True:
                    ax, ay = (ax+dx, ay+dy)
                    if ax > x or ax<0 or ay<0 or ay >y:
                        break
                    locs.add((ax,ay))
print(len(locs))
               


