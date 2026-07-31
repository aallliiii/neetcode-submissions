class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}
        numsSet = set(nums)
        numsCount = dict.fromkeys(numsSet, 0)

        for i in range (len(nums)):
            numsCount[nums[i]] += 1
        
        top = sorted(numsCount, key=numsCount.get, reverse=True)[:k]

        return top

        