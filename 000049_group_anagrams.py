class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_lists = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in anagram_lists:
                anagram_lists[sorted_str].append(str)
                continue
            anagram_lists[sorted_str] = [str]

        result = []
        for anagram_list in anagram_lists.values():
            result.append(anagram_list)

        return result
