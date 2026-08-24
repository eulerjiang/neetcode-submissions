from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = defaultdict(int)

        for num in nums:
            counters[num] += 1

        if len(counters) <= k:
            return list(counters.keys())

        freq = [[] for i in range(len(nums) + 1)]

        for num, count in counters.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



        

        
