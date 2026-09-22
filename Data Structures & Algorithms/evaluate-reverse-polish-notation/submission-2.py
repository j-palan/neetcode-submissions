class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        daStack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in ops:
                daStack.append(int(token))
            else:
                right = daStack.pop()
                left = daStack.pop()

                if token == "+":
                    answer = left + right
                elif token == "-":
                    answer = left - right
                elif token == "*":
                    answer = left * right
                else:
                    answer = int(left / right)

                daStack.append(answer)

        return daStack[-1]
        
        