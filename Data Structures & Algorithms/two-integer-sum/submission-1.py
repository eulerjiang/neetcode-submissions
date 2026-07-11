class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                return [seen[m], i]
            else:
                seen[n] = i
        
        return [-1, -1]