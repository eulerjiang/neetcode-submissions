from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            s1 = "".join(sorted(s))
            groups[s1].append(s)

        results = []
        for value in groups.values():
            results.append(value)

        return results
