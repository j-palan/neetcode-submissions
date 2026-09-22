class Solution:
    def isValid(self, s: str) -> bool:
        daStack = []
        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            # Opening bracket
            if char not in brackets:
                daStack.append(char)

            # Closing bracket
            else:
                if not daStack or daStack[-1] != brackets[char]:
                    return False

                daStack.pop()

        return not daStack

            
            

        

            