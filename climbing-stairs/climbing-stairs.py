class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        i = 0
        while i in range(n-1):
            temp = one
            one = one + two
            two = temp
            i += 1
        return one
        