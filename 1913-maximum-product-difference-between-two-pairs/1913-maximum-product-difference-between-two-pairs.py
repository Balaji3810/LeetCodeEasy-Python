class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        smallest = nums[0] * nums[1]
        highest = nums[len(nums) - 1] * nums[len(nums) - 2]
        return highest - smallest