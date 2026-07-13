class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r-l):
                top, buttom = l, r
                # save left top

                left_top = matrix[top][l + i]

                # buttom left to left top
                matrix[top][l + i] = matrix[buttom - i][l]

                # buttom right to butom left
                matrix[buttom - i][l] = matrix[buttom][r - i]

                # top right to buttom right
                matrix[buttom][r - i] = matrix[top + i][r]

                # left top to top right
                matrix[top + i][r] = left_top

            l += 1
            r -= 1

