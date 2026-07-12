class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # Calculate carry
            carry = (a & b) << 1

            # Sum without carry
            a = (a ^ b) & MASK

            # Update carry
            b = carry & MASK

        # Convert to signed integer
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)