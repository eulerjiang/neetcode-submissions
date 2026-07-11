class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right ) // 2

            mx = mid // cols
            my = mid % cols

            if matrix[mx][my] == target:
                return True
            elif matrix[mx][my] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False