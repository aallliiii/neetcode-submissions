class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        maxFrequency = 0
        count = {}

        for r in range (len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFrequency = max (maxFrequency, count[s[r]])

            while (r - left + 1) - maxFrequency> k:
                count[s[left]] -= 1
                left = left + 1
            result = max (result, r-left+1)
        return result
        