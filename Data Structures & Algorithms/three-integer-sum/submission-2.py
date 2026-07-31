class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i, a in enumerate (nums):
            if i>0 and nums[i-1] == a:
                continue
            left = i + 1
            right = len(nums) - 1

            while left<right:
                result = nums[left] + nums[right] + a
                if result < 0:
                    left += 1
                elif result > 0:
                    right -= 1
                else:
                    results.append([a, nums[left], nums[right]])
                    left = left + 1
                    while nums [left] == nums [left-1] and left<right:
                        left += 1
        return results

       