def calIndex(s: str) -> str:
    # return string like leter+num format as index
    freq = [0]*26

    for c in s:
        i = ord(c) - ord('a')
        freq[i] += 1

    tmp = []
    for i, c in enumerate(freq):
        l = chr(i + ord('a'))
        tmp.append(str(l) + str(c))
    
    index = "".join(tmp)
    print(index)
    return index

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        seen = {}
        for s in strs:
            index = calIndex(s)
            if index in seen:
                seen[index].append(s)
            else:
                seen[index] = [s]
        
        for val in seen.values():
            results.append(val)

        return results