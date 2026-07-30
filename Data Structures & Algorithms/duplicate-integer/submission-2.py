class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep_dict = {}
        len_nums = len(nums)
        for i in range (len_nums):
            if nums[i] in rep_dict:
                return True
            rep_dict[nums[i]] = i
        return False