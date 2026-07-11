from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs = defaultdict(int)

        n = len(s)
        for i in range(n):
            freqs[s[i]] += 1
            freqs[t[i]] -= 1

        for c in freqs.values():
            if c != 0:
                return False

        return True




        