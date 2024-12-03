n = 0
for nums in ([int(_) for _ in line.split()] for line in open("input.txt").readlines()):
    def is_safe(a: list[int]):
        diffs = [n1 - n2 for n1, n2 in zip(a[1:], a[:-1])]
        return (all(el < 0 for el in diffs) or all(el > 0 for el in diffs)) and all(
            (abs(el) >= 1 and abs(el) <= 3) for el in diffs
        )
    
    if is_safe(nums):
        n+=1 
        continue

    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[(i+1):]):
            n+=1
            break
print(n)
