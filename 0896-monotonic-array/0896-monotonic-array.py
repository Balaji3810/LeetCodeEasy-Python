class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decreasing = True
        increasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                decreasing = False
        if decreasing or increasing:
            return True
        else:
            return False
        