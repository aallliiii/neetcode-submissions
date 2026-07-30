class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        for i in range (len(nums)):
            temp = target - nums[i]
            if temp in already_seen:
                return [already_seen[temp], i]
            already_seen [nums[i]] = i
        

        