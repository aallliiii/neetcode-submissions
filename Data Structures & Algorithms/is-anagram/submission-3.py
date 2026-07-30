class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(list(s)) == sorted(list(t))
        if len(t) != len(s):
            return False
        count_hash_s, count_hash_t = {}, {}

        for i in range (len(s)):
            count_hash_s[s[i]] = 1 + count_hash_s.get(s[i], 0)
            count_hash_t[t[i]] = 1 + count_hash_t.get(t[i], 0)
        for char in count_hash_s:
            if count_hash_s[char] != count_hash_t.get(char, 0):
                return False
        return True
        
        