class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = {}
        for i in range (len(nums)):
            if nums[i] in already_seen:
                return True
            already_seen[nums[i]] = i
        return False
     