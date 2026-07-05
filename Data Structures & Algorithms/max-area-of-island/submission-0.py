class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #unweighted graphs... again either 0, 1
        visited = set()
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        temp = 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    temp = dfs(i,j)
                    max_area = max(temp, max_area)
        return max_area

