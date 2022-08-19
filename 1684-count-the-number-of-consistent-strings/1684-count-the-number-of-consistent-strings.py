class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            present = True
            for ch in word:
                if ch not in allowed:
                    present = False
                    break
            if present: count += 1
        return count
        