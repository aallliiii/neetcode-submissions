class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}
        set_nums = set(nums)
        results = dict.fromkeys(set_nums, 0)
        for i in range (len(nums)):
            results[nums[i]] += 1
        top = sorted(results, key=results.get, reverse=True)[:k]

        return list(top)
        