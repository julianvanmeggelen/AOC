

if __name__ == "__main__":
    res = {}
    lines = open('input.txt').readlines()
    res = 0
    for l, line in enumerate(lines):
        winning, have = line.split('|')
        winning = [int(_) for _ in winning.split(':')[1].strip().split()]
        have = [int(_) for _  in have.strip().split()]
        isct = set(winning).intersection(set(have))
        print(isct)
        res += 2**(len(isct)-1) if len(isct) >0 else 0
    print(res)


     

