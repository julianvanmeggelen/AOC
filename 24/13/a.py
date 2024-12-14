lines = [line.strip().replace('Button A: ', '').replace('Button B: ', '').replace('Prize: ', '') for line in open('input.txt').readlines() if line.strip() != '']

from functools import cache
import sys

sys.setrecursionlimit(1000000000)
@cache
def tokens_to_win(x, y, dxa, dya, dxb, dyb, px, py) -> float:
    # print(x,y)
    if x == px and y == py:
        return 0
    
    if x > px or y > py:
        return float('inf')
    
    return min(
        3 + tokens_to_win(x+dxa, y+dya, dxa, dya, dxb, dyb, px, py),
        1 + tokens_to_win(x+dxb, y+dyb, dxa, dya, dxb, dyb, px, py)
    )

total = 0
while lines:
    line = lines.pop(0).split(', ')
    dxa,dya = int(line[0].split('+')[1]), int(line[1][2:])
    line = lines.pop(0).split(', ')
    dxb,dyb = int(line[0].split('+')[1]), int(line[1][2:])
    line = lines.pop(0).split(', ')
    px,py = int(line[0].split('=')[1])+10000000000000, int(line[1][2:])+10000000000000
    ttw = tokens_to_win(0,0,dxa,dya,dxb,dyb,px,py)
    if ttw < float('inf'):
        total += ttw
print(total)




