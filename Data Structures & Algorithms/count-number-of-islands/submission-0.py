class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= row or c < 0 or c >= col or
                grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count