nums = [(int(i/2), int(num)) for i, num in enumerate(open('input.txt').readline())]
begin, x, res = 0,0,0
while True:
    if begin >= len(nums):
        break
    id = nums[begin][0]
    space = nums[begin][1]
    for _ in range(space):
        if begin % 2 == 0:
            res+=id*x
        else:
            if nums[-1][1] == 0:
                nums = nums[:-2]
            nums[-1] = (nums[-1][0], nums[-1][1]-1)
            res += nums[-1][0]*x
        x+=1
    begin+=1

print(res)

