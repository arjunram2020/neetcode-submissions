class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #points have an X Y coordiante system.... how to turn into a heap...
        import heapq
        heap = []
        for point in points:
            heap.append((-((point[0])**2+(point[1])**2), (point[0], point[1])))
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        for i in range(len(heap)):
            result.append(heap[i][1])

        return result