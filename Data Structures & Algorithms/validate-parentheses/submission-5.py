class Solution:
    def isValid(self, s: str) -> bool:
        daStack = []
        bracks = {
            ')' : '(',
            ']' : '[', 
            '}' : '{'
        }

        for char in s:
            if char not in bracks:
                daStack.append(char)

            else:
                if not daStack or daStack[-1] != bracks[char]:
                    return False

                daStack.pop()

        return not daStack



            
            

        

            