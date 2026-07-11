class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1, prev2 = 2, 1
        curr = 0

        for i in range(2, n):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr

        return curr
        