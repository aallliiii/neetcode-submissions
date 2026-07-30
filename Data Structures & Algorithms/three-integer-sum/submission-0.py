class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i, a in enumerate (nums):
            if i>0 and nums [i-1] == a:
                continue
            n = i+1
            j = len(nums) - 1
            while n<j:
                sum_result = a + nums[n] + nums[j]
                if sum_result>0:
                    j = j - 1
                elif sum_result<0:
                    n = n + 1
                else:
                    results.append([a, nums[n], nums[j]])
                    n = n + 1
                    while nums[n] == nums[n-1] and n<j:
                        n = n + 1
        return results

        