class Solution:
    def isValid(self, s: str) -> bool:
        daStack = []
        brackets = {
            ')' : '(', 
            ']' : '[', 
            '}' : '{'
        }

        for char in s:
            if char not in brackets:
                daStack.append(char)

            else:
                if not daStack or daStack[-1] != brackets[char]:
                    return False

                daStack.pop()

        return not daStack
           
    


            
            

        

            