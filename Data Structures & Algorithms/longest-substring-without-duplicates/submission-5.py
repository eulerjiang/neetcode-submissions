class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        maxLen = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1

            seen[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen


                
