import copy

class Solution(object):
    def __init__(self):
        self.solutions = []
    def is_safe(self, row, col, board):
        for i in range(len(board)):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
        i = 0
        while row - i >= 0 and col - i >= 0:
            if board[row - i][col - i] == 'Q':
                return False
            i += 1
        i = 0
        while row + i < len(board) and col + i < len(board):
            if board[row + i][col - i] == 'Q':
                return False
            i += 1
        i = 1
        while row + i < len(board) and col - i >= 0:
            if board[row + i][col - i] == 'Q':
                return False
            i += 1
        i = 1
        while row - i >= 0 and col + i < len(board):
            if board[row - i][col + i] == 'Q':
                return False
            i += 1
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        grid = [['.' for _ in range(n)] for _ in range(n)]
        solved = self.helper(n, 0, grid)
        print (len(self.solutions))
        if solved:
            return ["".join(item) for item in grid]
        else:
            return None

    def helper(self, n, row, grid):
        if n == row:

            self.solutions.append(copy.deepcopy(grid))
            return
        for col in range(n):
            if self.is_safe(row, col, grid):
                grid[row][col] = 'Q'
                self.helper(n, row + 1, grid)
                grid[row][col] = '.'



if __name__ == '__main__':
    solution = Solution()
    solution.solveNQueens(int(input()))