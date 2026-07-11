import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}

        for n in nums:
            if n in numDict:
                numDict[n] += 1
            else:
                numDict[n] = 1
        
        heap = []
        for num, freq in numDict.items():
            heapq.heappush(heap, (-freq, num))

        results = []
        while len(results) < k:
            item = heapq.heappop(heap)
            print(item)
            results.append(item[1])

        return results


        