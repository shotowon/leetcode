class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cached = {}
        
        for i, num in enumerate(nums):
            if target - num in cached:
                return [cached[target - num], i]
            cached[num] = i
        return []
