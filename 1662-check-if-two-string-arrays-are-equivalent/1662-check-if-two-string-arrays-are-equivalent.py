class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(w1 for w1 in word1)
        s2 = "".join(w2 for w2 in word2)
        return True if s1 == s2 else False
        