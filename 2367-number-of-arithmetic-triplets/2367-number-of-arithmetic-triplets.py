class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for i in range(len(nums)):
            j = nums[i] - diff
            k = diff + nums[i]
            if j in nums and k in nums:
                res += 1
        return res