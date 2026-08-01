class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        stack = []
        for c in s:
            if c in mapping.values():
                stack.append(c)
                continue
            elif c in mapping.keys() and len(stack) > 0:
                top = stack.pop()
                if top != mapping[c]:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True
