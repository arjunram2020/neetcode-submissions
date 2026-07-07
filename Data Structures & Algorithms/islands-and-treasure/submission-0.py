class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #for every tile, perform BFS algorithm.. until a 0 is found
        from collections import deque
        if not grid:
            return None
        boxes = []
        #find all the treasure boxes, and put them into an array of doubles
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        boxes.append([i,j])
        queue = deque(boxes)
        count = 0
        while queue:
            tile = queue.popleft()
            row = tile[0]
            col = tile[1]
            if row+1 < len(grid) and grid[row+1][col] == 2147483647:
                queue.append([row+1, col])
                grid[row+1][col] = grid[row][col] + 1
            if col+1 < len(grid[0]) and grid[row][col+1] == 2147483647:
                queue.append([row, col+1])
                grid[row][col+1] = grid[row][col] + 1
            if row-1 >= 0 and grid[row-1][col] == 2147483647:
                queue.append([row-1, col])
                grid[row-1][col] = grid[row][col] + 1
            if col-1 >= 0 and grid[row][col-1] == 2147483647:
                queue.append([row, col-1])
                grid[row][col-1] = grid[row][col] + 1
            


        

