class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ddict = {}
        for i in range (len(nums)):
            if nums[i] in ddict:
                return True
            ddict[nums[i]] = i
        return False