a = [line.strip() for line in open("input.txt").readlines()]
print(
    sum(
        (
            (a[y - 1][x - 1] == "M" and a[y + 1][x + 1] == "S")
            or (a[y - 1][x - 1] == "S" and a[y + 1][x + 1] == "M")
        )
        and (
            (a[y + 1][x - 1] == "M" and a[y - 1][x + 1] == "S")
            or (a[y + 1][x - 1] == "S" and a[y - 1][x + 1] == "M")
        )
        for y in range(1, len(a) - 1)
        for x in range(1, len(a[0]) - 1)
        if a[y][x] == "A"
    )
)
