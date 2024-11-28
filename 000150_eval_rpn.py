# PYTHON 3 SOLUTION


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        eval_values = []
        for token in tokens:
            if token == "+":
                b, a = eval_values.pop(), eval_values.pop()
                eval_values.append(a + b)
            elif token == "-":
                b, a = eval_values.pop(), eval_values.pop()
                eval_values.append(a - b)
            elif token == "*":
                b, a = eval_values.pop(), eval_values.pop()
                eval_values.append(a * b)
            elif token == "/":
                b, a = eval_values.pop(), eval_values.pop()
                eval_values.append(int(a / b))
            else:
                eval_values.append(int(token))

        return eval_values[0]
