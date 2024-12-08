lines = open("input.txt").readlines()
edges = [((a := line.strip().split("|"))[0], a[1]) for line in lines if "|" in line]
prec = {
    edge: [el[1] for el in edges if el[0] == edge]
    for edge in set(map(lambda el: el[0], edges))
}
print(
    sum(
        int(line[int(len(line) / 2)])
        for line in [
            line.strip().split(",")
            for line in lines
            if "|" not in line and len(line) > 1
        ]
        if not any(num2 in prec[num] for i, num in enumerate(line) for num2 in line[:i])
    )
)
