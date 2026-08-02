import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for w in stones:
            heapq.heappush(heap, -w)

        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                w = abs(x - y)
                heapq.heappush(heap, -w)

        return -heap[0] if heap else 0
