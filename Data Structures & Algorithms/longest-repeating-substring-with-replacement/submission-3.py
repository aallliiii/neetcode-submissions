class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequencyMax = 0
        countS = {}
        result = 0

        for right in range (len(s)):
            countS[s[right]] = 1 + countS.get(s[right], 0)
            frequencyMax = max (frequencyMax, countS[s[right]])

            while (right-left+1) - frequencyMax > k:
                countS[s[left]] -= 1
                left = left + 1
            
            result = max (result, right-left+1)
        return result

    