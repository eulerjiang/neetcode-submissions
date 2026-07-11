class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if no zero in list.
        maxProduct = 1
        zeroIndex = []
        for i, num in enumerate(nums):
            if num != 0:
                maxProduct *= num
            else:
                zeroIndex.append(i)

        results = [0] * len(nums)
        if len(zeroIndex) >= 2:
            pass
        elif len(zeroIndex) == 1:
            results = [0] * len(nums)
            results[zeroIndex[0]] = maxProduct
        else:
            # no zero
            for i in range(len(nums)):
                results[i] = maxProduct // nums[i]

        return results

            
        