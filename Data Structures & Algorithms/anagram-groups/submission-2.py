from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            alpha = [0] * 26
            for c in word:
                alpha[ord(c) - ord('a')] += 1
                
            groups[tuple(alpha)].append(word)

        return list(groups.values())