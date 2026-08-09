class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}
        numsSet = set(nums)
        numsCount = dict.fromkeys(numsSet, 0)

        for n in nums:
            numsCount[n] += 1
        result = sorted (numsCount, key=numsCount.get, reverse=True)[:k]
        return result

       
        