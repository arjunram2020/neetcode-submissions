class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
            #so that way only the k max numbers remain... 



    def add(self, val: int) -> int:
        import heapq
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


        
