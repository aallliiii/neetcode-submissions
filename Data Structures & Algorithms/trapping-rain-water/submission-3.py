class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        result = 0

        while left<right:
            if leftMax<rightMax:
                left = left + 1
                leftMax = max(height[left], leftMax)
                result+=leftMax-height[left]
            else:
                right=right-1
                rightMax=max(height[right], rightMax)
                result+=rightMax-height[right]
        return result        