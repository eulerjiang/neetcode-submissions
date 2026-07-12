class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        sign = 1 if x >= 0 else -1
        x = abs(x)

        rev = 0
        while x > 0:
            digit = x % 10
            x //= 10

            if rev > (MAX_INT - digit) // 10:
                return 0

            rev = rev * 10 + digit


        return rev * sign
        