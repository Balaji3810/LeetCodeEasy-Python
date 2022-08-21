class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        s1 = " ".join([words[i] for i in range(k)])
        return s1