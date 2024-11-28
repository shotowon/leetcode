class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed = {")": "(", "}": "{", "]": "["}
        expected_parens = []

        for char in s:
            if char in closed:
                if expected_parens and expected_parens[-1] == closed[char]:
                    expected_parens.pop()
                    continue
                return False

            expected_parens.append(char)

        return len(expected_parens) == 0
