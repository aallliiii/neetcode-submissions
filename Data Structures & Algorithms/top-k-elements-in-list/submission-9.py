class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = {}
        countSet = set(nums)
        countNum = dict.fromkeys(countSet, 0)

        for i in range (len(nums)):
            countNum[nums[i]]+=1
        result = sorted (countNum, key=countNum.get)[-k:]
        return result
        