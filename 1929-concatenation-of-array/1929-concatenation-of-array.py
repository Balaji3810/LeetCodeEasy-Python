class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        l = 0
        while l < 2 * len(nums):
            for i in range(len(nums)):
                ans.append(nums[i])
            l = len(ans)
        return ans