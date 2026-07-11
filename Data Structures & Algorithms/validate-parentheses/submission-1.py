class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c in mapping.values():
                # (, {, [, push to stack
                stack.append(c)
            elif c in mapping.keys():
                # pop stack and check pair
                if len(stack) > 0 and stack[-1] == mapping[c]:
                    # pop stack
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True