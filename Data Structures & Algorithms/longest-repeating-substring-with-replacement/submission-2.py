class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0 
        left = 0
        maxFrequency = 0
        countS = {}

        for right in range (len(s)):
            countS[s[right]] = 1 + countS.get(s[right], 0)
            maxFrequency = max (maxFrequency, countS.get(s[right]))

            while (right-left+1) - maxFrequency > k:
                countS[s[left]] -= 1
                left = left + 1
            result = max(result, right-left+1)
        return result       