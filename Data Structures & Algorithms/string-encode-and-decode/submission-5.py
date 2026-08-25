class Solution:

    def encode(self, strs: List[str]) -> str:
        # len1 + '#' + <str1> + len2 + '#' + <str2>
        result = ""

        for word in strs:
            result += str(len(word)) + '#' + word

        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # 1#a, 2#bb
        res = []

        i = 0
        while i < len(s):
            j = s[i:].index('#') + i
            print(s[i:j])
            length = int(s[i:j])

            i = j + 1
            word = s[i:i+length]
            print(word)
            res.append(word)

            i += length

        return res

