

if __name__ == "__main__":
    res = {}
    lines = open('input.txt').readlines()
    res = 0
    copies = [1 for _ in range(len(lines))]
    for l, line in enumerate(lines):
        winning, have = line.split('|')
        winning = [int(_) for _ in winning.split(':')[1].strip().split()]
        have = [int(_) for _  in have.strip().split()]
        isct = set(winning).intersection(set(have))
        for _ in range(copies[l]):
            for i in range(1, len(isct)+1):
                copies [l+i]+=1
    print(sum(copies))


     

