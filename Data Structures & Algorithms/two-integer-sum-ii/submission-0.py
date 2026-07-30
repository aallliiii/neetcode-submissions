class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i<j:
            res = numbers[i] + numbers[j]
            if res == target:
                results = []
                results.append(i+1)
                results.append(j+1)
                return results
            elif res < target:
                i = i + 1
            elif res > target:
                j = j - 1

        