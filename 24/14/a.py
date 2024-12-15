q1,q2,q3,q4=0,0,0,0
w, h = 101, 103
xm, ym = int(w/2), int(h/2)
T = 100
for line in open('input.txt').readlines():
    line = line.replace('p=', '').replace('v=', '').split()
    x0, y0 = map(int, line[0].split(','))
    dx, dy = map(int, line[1].split(','))
    x100, y100 = (x0 +T*dx)%w, (y0+T*dy)%h
    lh, rh, th, bh = x100 < xm, x100 > xm, y100 < ym, y100 > ym
    if th and lh: q1+=1
    if th and rh: q2+=1
    if bh and lh: q3+=1
    if bh and rh: q4+=1
print(q1*q2*q3*q4)
