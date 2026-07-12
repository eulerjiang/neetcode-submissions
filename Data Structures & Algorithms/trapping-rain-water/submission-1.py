class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        max_right = height[-1]

        total = 0

        l, r = 0, len(height) - 1

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                total += max(0, max_left - height[l])
            else:
                r -= 1
                max_right = max(max_right, height[r])
                total += max(0, max_right - height[r])

        return total