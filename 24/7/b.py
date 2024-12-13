def check_operators(num: int, curr: float, nums:int, i: int=0):
    if curr == num and len(nums) == 0:
        return True
    
    if len(nums) == 0 or curr > num:
        return False
    return ( 
        check_operators(num, curr*nums[0], nums[1:], i+1)
        or check_operators(num, curr+nums[0], nums[1:], i+1) 
        or check_operators(num, int(str(curr)+str(nums[0])), nums[1:], i+1)
    )

   

total: int = 0
for line in open('input.txt'):
    #print("----"*10)
    left = int(line.strip().split(':')[0])
    nums = [int(_.strip()) for _ in line.split(':')[1].split()]
    if check_operators(left, nums[0], nums[1:]):
        total += left
print(total)