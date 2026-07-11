class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n

        prod = 1

        for i in range(n):
            if i == 0:
                prod = 1
            else:
                prod *= nums[i-1]
            products[i] = prod

        results = [0] * n
        right_product = 1
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right_product = 1
            else:
                right_product *= nums[i + 1]

            results[i] = right_product * products[i]
        
        return results