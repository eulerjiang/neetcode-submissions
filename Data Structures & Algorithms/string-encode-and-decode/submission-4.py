class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        len(str1)#str1 len(str2)#str2
        """
        results = ""

        for word in strs:
            results += str(len(word)) + "#" + word

        return results

    def decode(self, s: str) -> List[str]:
        results = []

        i = j = 0
        while j < len(s):
            while j < len(s) and s[j] != "#":
                j += 1
            # s[j] == "#"
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            results.append(word)

            i = j + 1 + length
            j = i

        return results





        
