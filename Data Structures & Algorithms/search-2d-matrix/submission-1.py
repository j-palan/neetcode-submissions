class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in matrix:

            left = 0
            right = len(m) - 1
            while left <= right:
                middle = (left + right) // 2     

                if m[middle] == target:
                    return True

                elif m[middle] < target:
                    left = middle + 1
                
                else:
                    right = middle - 1

        return False

                
