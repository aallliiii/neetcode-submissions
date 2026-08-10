class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        countSet = set(nums)
        countNums = dict.fromkeys(countSet, 0)

        for i in range (len(nums)):
            countNums[nums[i]] += 1
        
        result = sorted (countNums, key=countNums.get, reverse=True)[:k]

        return result
       