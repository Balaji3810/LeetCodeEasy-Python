class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        output = []
        for idx, num in enumerate(nums):
            while q and num > q[-1][1]:
                q.pop()
            q.append([idx, num])
            while (idx - q[0][0] + 1) > k:
                q.popleft()
            if (idx + 1) >= k:
                output.append(q[0][1])
        return output
        