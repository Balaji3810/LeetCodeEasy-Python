class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxW = 0
        for i in range(len(sentences)):
            l = len(sentences[i].split(" "))
            maxW = max(l, maxW)
        return maxW
            
            