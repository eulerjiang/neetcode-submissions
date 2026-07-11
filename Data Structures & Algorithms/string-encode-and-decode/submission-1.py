SNUM = 2

class Solution:
    def encode(self, strs: List[str]) -> str:
        # key = 2, c -> c+2
        # #len1#<string>#len2#<string2>
        estr = ""

        for s in strs:
            length = len(s)
            prefix = "#{}#".format(length + SNUM)
            es = ""

            for c in s:
                es += chr(ord(c) + SNUM)
            estr += prefix + es
        print(estr)
        return estr + "$"

    def decode(self, s: str) -> List[str]:
        results = []

        i = 0
        length = len(s)
        while i < length:
            if s[i] == '#':
                # find next #
                i += 1
                start = i
                while s[i] != '#':
                    i += 1
                # s[i] == '#'
                slen = int(s[start:i]) - SNUM
                print(slen)
                
                i += 1  # skip end #
                if i >= length:
                    break

                estr = ''
                for k in range(slen):
                    estr += chr(ord(s[i+k]) - SNUM)
                    print(estr)
                results.append(estr)
                i += slen - 1
            elif s[i] == "$":
                break
            else:
                raise Exception("wrong decode string")
            i += 1
            if s[i] == "$":
                break

        return results


