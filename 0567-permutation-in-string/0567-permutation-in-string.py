class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        s1Count = Counter(s1)

        while l <= len(s2):
            if s1Count == collections.Counter(s2[l:r]):
                return True
            l += 1
            r += 1
        return False
