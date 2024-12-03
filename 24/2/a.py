n = 0
for nums in ([int(_) for _ in line.split()] for line in open("input.txt").readlines()):
    diffs = [n1 - n2 for n1, n2 in zip(nums[1:], nums[:-1])]
    n += (all(el < 0 for el in diffs) or all(el > 0 for el in diffs)) and all(
        (abs(el) >= 1 and abs(el) <= 3) for el in diffs
    )
print(n)
