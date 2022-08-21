class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = "abcdefghijklmnopqrstuvwxyz"
        hashmap = {}
        hashmap = {alpha[i]:morse[i] for i in range(len(alpha))}
        hashset = set()
        for word in words:
            t = ""
            for ch in word:
                t += hashmap[ch]
            hashset.add(t)
        return len(hashset)