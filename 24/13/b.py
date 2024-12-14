lines = [line.strip().replace('Button A: ', '').replace('Button B: ', '').replace('Prize: ', '') for line in open('input.txt').readlines() if line.strip() != '']
#ok apparently there is only a single solution each time so we can just math it out
total = 0
while lines:
    line = lines.pop(0).split(', ')
    dxa,dya = int(line[0].split('+')[1]), int(line[1][2:])
    line = lines.pop(0).split(', ')
    dxb,dyb = int(line[0].split('+')[1]), int(line[1][2:])
    line = lines.pop(0).split(', ')
    px,py = int(line[0].split('=')[1])+10000000000000, int(line[1][2:])+10000000000000
    
    A = (dxb*py - dyb*px) / (dxb*dya - dyb*dxa)
    B = (px-dxa*A) / dxb
    if abs(A - round(A)) < 0.0000001 and abs(B - round(B)) < 0.00000001:
        total += 3*A + B
print(total)




