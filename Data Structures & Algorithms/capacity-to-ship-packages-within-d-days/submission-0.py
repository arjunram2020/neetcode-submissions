class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #what is the array we are trying to search....
        if not weights:
            return 0
        low = max(weights)
        high = sum(weights)
        result = high
        #what is the condition here.... sum up the loop... iterate through, and count the number of days you need BASED ON THE MIDDLE
        #if the number of days <= days, then it is valid and save the middle result as the optimal # of days... go more left
        #otherwise, invalid... look larger towards the right
        while low <= high:
            mid = (low + high) // 2 #holds the current weight capacity
            temp = 0
            sums = 0
            for weight in weights:
                if (weight + temp) > mid:
                    sums += 1
                    temp = 0
                temp += weight
            sums+=1
            if sums <= days:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        

                    


