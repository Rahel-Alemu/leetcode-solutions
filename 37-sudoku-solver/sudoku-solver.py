class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

        def backtrack(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            box_idx = (i // 3) * 3 + j // 3

            for c in "123456789":
                if c not in rows[i] and c not in cols[j] and c not in boxes[box_idx]:
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[box_idx].add(c)

                    if backtrack(index + 1):
                        return True

                    board[i][j] = '.'
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[box_idx].remove(c)

            return False

        backtrack(0)