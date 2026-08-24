from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = defaultdict(int)

        for i in range(0, len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1

        for c, count in counter.items():
            if count != 0:
                return False

        return True

