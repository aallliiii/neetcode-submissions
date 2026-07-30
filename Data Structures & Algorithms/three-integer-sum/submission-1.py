class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate (nums):
            if i > 0 and nums[i-1] == n:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                result = n + nums[left] + nums[right]
                if result > 0:
                    right = right - 1
                elif result < 0:
                    left = left + 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left = left + 1
                    while nums [left] == nums [left-1] and left<right:
                        left = left + 1
        return res
        