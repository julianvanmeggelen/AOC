def check_operators(num: int, nums:int, i: int=0):
    if len(nums) == 0 or num < 0:
        return False
    next_num = nums[-1]

    if num == next_num or num == 0:
        return True
    return check_operators(num/next_num, nums[:-1]) or check_operators(num-next_num, nums[:-1])

total: int = 0
for line in open('input.txt'):
    left = int(line.strip().split(':')[0])
    nums = [int(_.strip()) for _ in line.split(':')[1].split()]
    if check_operators(left, nums):
        total += left
print(total)