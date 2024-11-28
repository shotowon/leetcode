class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        boxes = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]

        i = 0
        for r, row in enumerate(board):
            for n, num in enumerate(row):
                if num == ".":
                    continue
                number = int(num)
                box = ((r // 3) * 3) + (n // 3)
                if (
                    number in rows[r]
                    or number in boxes[box]
                    or number in columns[n]
                ):
                    return False
                boxes[box][number] = number
                rows[r][number] = number
                columns[n][number] = number
                i += 1

        return True
