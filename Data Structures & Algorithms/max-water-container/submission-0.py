class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        l = 0
        r = len(heights) - 1

        while l < r:
            
            if heights[l] <= heights[r]:
                a = heights[l] * (r-l)
                areas.append(a)
                l += 1
            elif heights[l] > heights[r]:
                a = heights[r] * (r-l)
                areas.append(a)
                r -= 1

        return max(areas)




            

