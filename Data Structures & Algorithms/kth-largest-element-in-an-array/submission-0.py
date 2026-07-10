class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #to find kth largest element... take a minheap... and elimiate till you have k items left... those are your k largest element...
        #return the first pop...

        import heapq
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return heapq.heappop(nums)