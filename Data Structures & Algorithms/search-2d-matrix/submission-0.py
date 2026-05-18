class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we cannot brute force, that would be O(m*n)
        #we can look at the first elements of each row...
        
        row = -1
        #1st BSA - row recognition
        #start with the middle row
        left = 0
        right = len(matrix)-1
        middle = (left + right) // 2
        while left <= right:
            if target < matrix[middle][0]:
                right = middle - 1
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                row = middle
                break
            middle = (left + right) // 2
        if row == -1:
            return False


        #now we have the row index to start our next binary search algorithm, which is in the specific row
        left = 0
        right = len(matrix[row])-1
        middle = (left + right) // 2
        while left <= right:
            #case if target was found
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            middle = (left + right) // 2
        return False
                
        

