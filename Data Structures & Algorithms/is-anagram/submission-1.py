class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        freq = [0]*26
        
        if len(s) != len(t):
            return False

        i = 0
        while i < len(s):
            a = s[i].lower()
            b = t[i].lower()
            freq[ord(a)-ord('a')] += 1
            freq[ord(b)-ord('a')] -= 1
            i += 1

        for val in freq:
            if val != 0:
                return False

        return True
