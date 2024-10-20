class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        prefix_mul = 1
        for i, num in enumerate(nums):
            result[i] = prefix_mul
            prefix_mul *= num

        postfix_mul = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_mul
            postfix_mul *= nums[i]

        return result
