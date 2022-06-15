class Solution:
    def twoSum(self,nums:list,target:int) -> List[int]:
        prevMap = {} #val : index
        
        for i, n in enumerate(nums):
            
            diff = target - n
            
            if diff in prevMap:
                return [prevMap[diff],i]
            
            else:
                prevMap[n] = i
        return
      