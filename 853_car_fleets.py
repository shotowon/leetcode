from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        desc_sorted_pairs = sorted([[p, s] for p, s in zip(position, speed)])[::-1]
        
        fleetsStack = []
        for p, s in desc_sorted_pairs:
            fleetsStack.append((target - p) / s)
            if len(fleetsStack) >= 2 and fleetsStack[-1] <= fleetsStack[-2]:
                fleetsStack.pop()
        return len(fleetsStack)

