class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            # check boundary 
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == "0" or (i, j) in visited:
                return 

            visited.add((i, j))

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)


        isLands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    isLands += 1
                    dfs(i, j)
        return isLands