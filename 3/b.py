

import math


def get_number(line, i, l ):
    res = line[i]
    key = [i]
    j = i+1

    while line[j].isdigit():
        res+=line[j]
        key.append(j)
        j+=1

    j = i-1
    while line[j].isdigit():
        res = line[j] + res
        key.append(j)
        j-=1

    return res, tuple([l] + sorted(key))

if __name__ == "__main__":
    res = 0
    lines = open('input.txt').readlines()
    for l, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '*':
                gear_res = {}
                if (c > 0 and line[c-1].isdigit()):
                    num, key = get_number(line, c-1, l)
                    gear_res[key] = num
                if (c < len(line) - 1 and line[c+1].isdigit()):
                    num, key = get_number(line, c+1, l)
                    gear_res[key] = num

                if  (l < len(lines) - 1 and lines[l+1][c].isdigit()):
                    num, key = get_number(lines[l+1], c, l+1)
                    gear_res[key] = num

                if ( l < len(lines) - 1 and c < len(line) - 1 and lines[l+1][c+1].isdigit()):
                    num, key = get_number(lines[l+1], c+1, l+1)
                    gear_res[key] = num

                if (l < len(lines) - 1 and c > 0 and lines[l+1][c-1].isdigit()):
                    num, key = get_number(lines[l+1], c-1, l+1)
                    gear_res[key] = num

                if (l > 0 and c > 0 and lines[l-1][c-1].isdigit()):
                    num, key = get_number(lines[l-1], c-1, l-1)
                    gear_res[key] = num

                if (l > 0 and lines[l-1][c].isdigit()):
                    num, key = get_number(lines[l-1], c, l-1)
                    gear_res[key] = num

                if (l > 0 and c < len(line)-1 and lines[l-1][c+1].isdigit()):
                    num, key = get_number(lines[l-1], c+1, l-1)
                    gear_res[key] = num
                
                if len(gear_res) == 2:
                    res += math.prod(map(int, gear_res.values()))

    print(res)

