from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = defaultdict(int)

        for num in nums:
            counters[num] += 1

        if len(counters) <= k:
            return list(counters.keys())

        heap = []
        
        for num, count in counters.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

        

        
