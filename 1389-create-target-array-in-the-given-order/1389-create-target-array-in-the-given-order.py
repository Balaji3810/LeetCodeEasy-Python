class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(index)):
            new_nums.insert(index[i],nums[i])
            #print(new_nums)
        return new_nums
        