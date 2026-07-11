class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)

        l, r = 0, n1
        total_left = (n1 + n2 + 1) // 2

        while l <= r:
            i = (l + r) // 2
            j = total_left - i

            if j < 0:
                r = i - 1
                continue
            elif j > n2:
                l = i + 1
                continue

            n1_left = nums1[i - 1] if i > 0 else float("-inf")
            n1_right = nums1[i] if i < n1 else float("+inf")

            n2_left = nums2[j - 1] if j > 0 else float("-inf")
            n2_right = nums2[j] if j < n2 else float("+inf")

            if n1_left <= n2_right and n2_left <= n1_right:
                if (n1 + n2) % 2 == 1:
                    return max(n1_left, n2_left)
                return (max(n1_left, n2_left) + min(n1_right, n2_right)) / 2

            elif n1_left > n2_right:
                r = i - 1
            else:
                l = i + 1