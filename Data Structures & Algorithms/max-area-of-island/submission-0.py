class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        COLS = len(grid[0])
        ROWS = len(grid)

        area = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                 grid[r][c] == 0):
                 return 0

            grid[r][c] = 0
            n = 1

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                n += dfs(r + dr, c + dc)

            return n

        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))

        return area