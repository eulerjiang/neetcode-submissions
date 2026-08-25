class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n

        left = 1
        right = 1
        for i in range(n):
            left_prod[i] = left
            left *= nums[i]

            right_prod[n - 1 - i] = right
            right *= nums[n - 1 - i]

        res = []
        for i in range(n):
            if i == 0:
                res.append(right_prod[i])
            elif i > 0 and i < n - 1:
                res.append(left_prod[i] * right_prod[i])
            else:
                res.append(left_prod[i])

        return res