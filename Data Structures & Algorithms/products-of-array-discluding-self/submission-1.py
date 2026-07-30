class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = 1
        postfix = 1
        results = [1] * length
        for i in range (length):
            results[i] = prefix
            prefix *= nums[i]
        for i in range (length-1,-1,-1):
            results[i] *= postfix
            postfix *= nums[i]
        return results
        