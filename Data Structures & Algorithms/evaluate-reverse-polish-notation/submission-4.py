class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # calculate
                right = stack.pop()
                left = stack.pop()

                num = None
                if token ==  "+":
                    num = left + right
                elif token ==  "-":
                    num = left - right
                elif token ==  "*":
                    num = left * right
                elif token ==  "/":
                    num = int(left / right)
                stack.append(num)
            else:
                stack.append(int(token))

        return stack[0]
