class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0

        while n > 0:
            reminder = n % 2
            if reminder == 1:
                num += 1
            n = n // 2

        return num