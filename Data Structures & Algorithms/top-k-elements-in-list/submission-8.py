class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}
        numSet = set(nums)
        numsCount = dict.fromkeys(numSet, 0)

        for i in range (len(nums)):
            numsCount[nums[i]] += 1
        
        result = sorted (numsCount, key=numsCount.get)[-k:]
        return result

     