class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = {}
        for num in nums:
            freqs[num] = freqs.setdefault(num, 0) + 1

        freq_to_nums = {} 
        for num, freq in freqs.items():
            if freq not in freq_to_nums:
                freq_to_nums[freq] = []
            freq_to_nums[freq].append(num)

        return [num for freq in sorted(freq_to_nums.keys(), reverse=True) for num in freq_to_nums[freq]][:k]
