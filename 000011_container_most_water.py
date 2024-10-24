from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, result = 0, len(height) - 1, 0
        
        while l < r:
            minHeight = min(height[l], height[r])
            result = max(result, (r - l) *  minHeight) 
            
            if minHeight == height[l]:
                l += 1
                continue
            r -= 1

        return result
