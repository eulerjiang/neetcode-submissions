from collections import defaultdict

def convert(freq: dict) -> str:
    result = []
    for key in sorted(freq.keys()):
        result.append(key + str(freq[key]))

    return "".join(result)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            freq = defaultdict(int)
            for c in word:
                freq[c] += 1
            key = convert(freq)
            group[key].append(word)

        results = []
        for val in group.values():
            results.append(val)

        return results