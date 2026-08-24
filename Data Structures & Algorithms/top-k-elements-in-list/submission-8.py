from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = defaultdict(int)

        for num in nums:
            counters[num] += 1

        if len(counters) <= k:
            return list(counters.keys())

        group = sorted(counters.items(), key=lambda item: item[1], reverse=True)
        
        results = []
        for key, val in group[:k]:
            results.append(key)

        return results

        

        
