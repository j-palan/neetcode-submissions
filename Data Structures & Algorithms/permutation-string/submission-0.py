class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorteds1 = "".join(sorted(s1))

        window_size = len(s1)
        left = 0

        # The right pointer expands the window by moving forward
        for right in range(len(s2)):
    
            # Condition: When the distance between pointers equals our window size
            if (right - left + 1) == window_size:
                
                window = s2[left : right + 1]
                sortedwindow = "".join(sorted(window))
                
                if sortedwindow == sorteds1:
                    return True
    
        
                # Shrink the window from the left to slide it forward
                left += 1

        return False