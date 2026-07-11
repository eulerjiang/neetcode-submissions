
class Solution:
    def encode(self, strs: List[str]) -> str:
        # combine string as <len1>#<str1><len2>#<str2>
        results = []

        for word in strs:
            code = str(len(word)) + "#" + word
            results.append(code)

        return "".join(results)


    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        start = 0
        while i < len(s):
            while s[i] != '#':
                i += 1

            # s[i] = '#', start:i is len
            num = int(s[start:i])
            word = s[i+1:i+num+1]

            strs.append(word)

            i += num + 1
            start = i
        
        return strs


