class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #print(nums,target)
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                #print(threeSum)
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    print(a, nums[l], nums[r])
                    res.append([a, nums[l], nums[r]])
                    #print(res)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res