from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def genParens(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                genParens(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                genParens(openN, closeN + 1)
                stack.pop()

        genParens(0, 0)
        return res
