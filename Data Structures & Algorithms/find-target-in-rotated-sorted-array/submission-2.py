class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] < nums[r]:
                # m <= r
                # right is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    # target < nums[m] or target > nums[r]
                    r = m - 1 
            else:
                # left is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
                    



        