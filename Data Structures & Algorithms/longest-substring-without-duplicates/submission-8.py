class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCounter = {}

        maxLen = 0

        l = 0
        r = 0
        for r in range(len(s)):
            while s[r] in charCounter:
                del charCounter[s[l]]
                l += 1
            
            charCounter[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
                
        return maxLen
