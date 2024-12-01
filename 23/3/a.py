

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

def is_symbol(a):
    return not (a.isalnum() or a.isspace() or a == '.')

if __name__ == "__main__":
    res = {}
    lines = open('input.txt').readlines()
    for l, line in enumerate(lines):
        for c, char in enumerate(line):
            if char.isdigit():
                if (
                    (c > 0 and is_symbol(line[c-1] ))
                    or (c < len(line) - 1 and is_symbol(line[c+1] ))
                    or (l < len(lines) - 1 and is_symbol(lines[l+1][c] ))
                    or ( l < len(lines) - 1 and c < len(line) - 1 and is_symbol(lines[l+1][c+1] ))
                    or (l < len(lines) - 1 and c > 0 and is_symbol(lines[l+1][c-1] ))
                    or (l > 0 and c > 0 and is_symbol(lines[l-1][c-1] ))
                    or (l > 0 and is_symbol(lines[l-1][c] ))
                    or (l > 0 and c < len(line)-1 and is_symbol(lines[l-1][c+1] ))
                ):
                    num, key = get_number(line, c, l)
            
                    if key not in res:
                        print(l, key, num)
                        res[key] = num

    print(res.values())
    print(sum(map(int, res.values())))

