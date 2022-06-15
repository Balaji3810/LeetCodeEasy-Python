class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))
        
       #for i in range(len(nums)):
       #    for j in range(len(nums)):
       #        if i!=j:
       #            if nums[i] == nums[j]:
       #                return True
       #     return False

        hashset = set()
        
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        