nums = [1,2,3,4,5,6,7,8]
target = 3
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] < target:
        l = m + 1
    elif nums[m] > target:
        r = m - 1
    else:
        print(nums[m])
        break
        
        
        