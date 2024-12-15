w, h = 101, 103
xm, ym = int(w/2), int(h/2)

# from scipy.spatial import distance_matrix use if need speed

for T in range(10000):
    end_pos = []
    for line in open('input.txt').readlines():
        line = line.replace('p=', '').replace('v=', '').split()
        x0, y0 = map(int, line[0].split(','))
        dx, dy = map(int, line[1].split(','))
        x100, y100 = (x0 +T*dx)%w, (y0+T*dy)%h
        end_pos.append((x100,y100))
    dists= []
    for x1, y1 in end_pos:
        for x2, y2 in end_pos:
            dists.append(((x2-x1)**2 + (y2-y1)**2)**0.5)
    if sum(dists)/len(dists) < 40:
    # dm  = distance_matrix(end_pos, end_pos)
    # if (adm:=dm.mean()) < 40:
        print(T)
        break
