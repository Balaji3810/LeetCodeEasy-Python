class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mapped = {"type" : 0, "color" : 1, "name" : 2}
        result = 0
        for item in items:
            if (item[mapped[ruleKey]] == ruleValue):
                result += 1
        return result
        