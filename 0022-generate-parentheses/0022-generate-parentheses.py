class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTracking(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)
                return 
            if open_n < n:
                backTracking(open_n + 1, closed_n, path + "(")
            
            if closed_n < open_n:
                backTracking(open_n, closed_n + 1, path + ")")
        backTracking(0, 0, "")
        return res

        