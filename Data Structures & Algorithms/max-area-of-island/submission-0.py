class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(i, j):
            # check boundary
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0 or (i, j) in visited:
                return 0

            visited.add((i, j))
            area = 1
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j-1)
            area += dfs(i, j+1)
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea