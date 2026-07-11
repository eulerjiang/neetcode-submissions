class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}

        for n in nums:
            if n in numDict:
                numDict[n] += 1
            else:
                numDict[n] = 1
        
        # numDicts with n occur numDict[n] time
        newDict = {}
        for num, freq in numDict.items():
            if freq in newDict:
                newDict[freq].append(num)
            else:
                newDict[freq] = [num]

        results = []
        i = 1
        for freq in reversed(sorted(newDict.keys())):
            j = len(newDict[freq])
            results.extend(newDict[freq])
            if i + j - 1 == k:
                return results
            i += j

        return results


        