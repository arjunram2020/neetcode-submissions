class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #here we are not searching through the piles array, we are searching through all the possibilities of k...
        #we can implicitly create an array of 1 += all the way to max(piles), for that we do not need to create another array, just use low, high, and mid
        #search through... and see h is feasible for each middle.... if yes, then go left, if not, then go right.... 
        #now when to stop.... is simply just by left<=right

        if not piles:
            return 0
        low = 1
        high = max(piles)
        result = max(piles)
        while low <= high:
            mid = (low + high) // 2
            sums = 0
            for pile in piles:
                sums += -(-pile // mid)
            if sums <= h:
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        return result

            