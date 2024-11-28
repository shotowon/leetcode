class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = num

        return False
