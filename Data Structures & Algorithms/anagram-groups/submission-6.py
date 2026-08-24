from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                freq[i] += 1
            group[tuple(freq)].append(word)

        return list(group.values())