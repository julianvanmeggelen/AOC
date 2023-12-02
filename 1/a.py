if __name__ == "__main__":
    res = 0
    for line in open('input.txt').readlines():
        all_num = [c for c in line if c.isdigit()]
        res += int(all_num[0]+all_num[-1])
    print(res)
