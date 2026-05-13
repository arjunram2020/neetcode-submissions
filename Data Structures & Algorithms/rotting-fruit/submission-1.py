class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        freshFruit = 0
        rotten = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    rotten.add((i,j))
                if grid[i][j] == 1:
                    freshFruit += 1

        #BFS Alg
        time = 0
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        queue = deque(rotten)
        while queue and freshFruit > 0:
            for i in range(len(queue)):
                fruit = queue.popleft()
                for dr, dc in directions:
                    sr, sc = fruit[0] + dr, fruit[1] + dc
                    if (sr < 0 or sc < 0 or sr >= ROW or sc>= COL or grid[sr][sc] == 0 or grid[sr][sc] == 2):
                        continue
                    queue.append((sr,sc))
                    grid[sr][sc] = 2
                    freshFruit -= 1
            time += 1
        if freshFruit > 0:
            return -1
        else:
            return time
                

