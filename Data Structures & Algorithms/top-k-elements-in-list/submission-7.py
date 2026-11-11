class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        countSet = set(nums)
        numCount = dict.fromkeys(countSet, 0)

        for i in range(len(nums)):
            numCount[nums[i]] += 1
        result = sorted (numCount, key=numCount.get, reverse=True)[:k]
        return result
        