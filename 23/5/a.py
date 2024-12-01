

if __name__ == "__main__":
    lines = open('input.txt').readlines()
    mapped = list(map(int, lines.pop(0).strip('seeds: ').split()))
    mapped_set = set()
    for l, line in enumerate(lines):
        if any((c.isdigit()) for c in line):
            dest_start, org_start, length = map(int,line.split())
            for i, el in enumerate(mapped):
                if i not in mapped_set and el >= org_start and el < org_start+length:
                    mapped[i] = dest_start + (el-org_start) 
                    mapped_set.add(i)
        else:
            mapped_set = set()
    print(min(mapped))


     

