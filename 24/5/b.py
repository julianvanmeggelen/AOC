from functools import cmp_to_key


lines = open("input.txt").readlines()
edges = [((a := line.strip().split("|"))[0], a[1]) for line in lines if "|" in line]
prec = {
    edge: [el[1] for el in edges if el[0] == edge]
    for edge in set(map(lambda el: el[0], edges))
}
total=0
for line in [
    line.strip().split(",")
        for line in lines
        if "|" not in line and len(line) > 1
    ]:
    if any(num2 in prec[num] for i, num in enumerate(line) for num2 in line[:i]):
        i = 0
        while i < len(line)-1:
            j = i+1
            while j < len(line):
                if line[i] in prec[line[j]]:
                    line.insert(j, line.pop(i))
                    j=i+1
                else:
                    j+=1
            i+=1
        total += int(line[int(len(line) / 2)])
print(total)

