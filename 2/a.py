
mx = {
    'red': 12,
    'green': 13,
    'blue': 14
}
if __name__ == "__main__":
    res = set()
    for line in open('input.txt').readlines():
        id_str, game = line.split(':')
        id = int(id_str.strip('Game '))
        possible = True
        for draw in game.split(';'):
            for cube in draw.split(','):
                num, color = cube.split()
                if int(num) > mx[color]:
                    possible = False
                    break
        if possible:
            res.add(id)
    print(sum(res))

