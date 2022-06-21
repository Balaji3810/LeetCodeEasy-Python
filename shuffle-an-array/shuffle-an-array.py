class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original 

    def shuffle(self) -> List[int]:
        arr = self.original
        #last_index = len(arr)-1
        #while last_index > 0:
        #    rand_index = random.randint(0, last_index)
        #    temp = arr[last_index]
        #    arr[last_index] = arr[rand_index]
        #    arr[rand_index] = temp
        #    last_index -= 1
        #return arr
        rand_values = [random.random() for i in range(len(arr))]
        rand_indexes = [i for i in range(len(arr))]
        rand_indexes.sort(key=lambda i: rand_values[i])
        arr = [arr[i] for i in rand_indexes]
        return arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()