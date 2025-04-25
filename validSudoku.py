import collections
from typing import List

# Approach: Use hash sets to track seen numbers in rows, columns, and boxes
# TC: O(1) - fixed size 9x9 grid
# SC: O(1) - at most 81 values stored across hash sets


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check board dimensions
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False

        # Create hash sets for rows, cols, and 3x3 squares
        ROWS = collections.defaultdict(set)
        COLS = collections.defaultdict(set)
        SQR = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue  # Skip empty cells

                # Check if value already exists in row, col or 3x3 square
                if (
                    val in ROWS[r]
                    or val in COLS[c]
                    or val in SQR[(r // 3) * 3 + (c // 3)]
                ):
                    return False

                # Add value to row, col, and square set
                ROWS[r].add(val)
                COLS[c].add(val)
                SQR[(r // 3) * 3 + (c // 3)].add(val)

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# Create object and print result
sol = Solution()
print("Is the Sudoku board valid?", sol.isValidSudoku(board))
