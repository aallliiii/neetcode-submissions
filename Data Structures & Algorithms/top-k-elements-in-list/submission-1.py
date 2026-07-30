class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        keys = set (nums)
        nums_count = dict.fromkeys(keys, 0)
        for i in range (len(nums)):
            nums_count [nums[i]] += 1
        top = sorted (nums_count, key=nums_count.get)[-k:]
        return list(top)
        