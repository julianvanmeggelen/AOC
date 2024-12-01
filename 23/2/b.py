if __name__ == "__main__":
    res = 0
    for line in open('input.txt').readlines():
        id_str, game = line.split(':')
        game_mins = {'red': 0, 'green': 0, 'blue': 0}
        for draw in game.split(';'):
            for cube in draw.split(','):
                num, color = cube.split()
                game_mins[color] = max(game_mins[color] , int(num))
        res += game_mins['red']*game_mins['green']*game_mins['blue']
    print(res)

