class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        if not stones:
            return 0
        while len(stones) > 1:
            x = - (heapq.heappop(stones))
            y = - (heapq.heappop(stones))
            if x == y:
                continue
            if x >= y:
                heapq.heappush(stones, -(x-y))

        if len(stones) == 1:
            return - (stones[0])
        else:
            return 0
