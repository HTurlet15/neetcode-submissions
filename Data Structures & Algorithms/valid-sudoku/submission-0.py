class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_grid = {i: set() for i in range(9)}
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        for r_i in range(9) :
            for c_i in range(9):
                val = board[r_i][c_i]
                if val==".":
                    continue
                print(val)
                grid = r_i //3 + c_i//3 *3
                if val in sub_grid[grid]:
                    print(grid, sub_grid)
                    return False
                if val in rows[r_i]:
                    return False
                if val in cols[c_i]:
                    return False
                sub_grid[grid].add(val)
                rows[r_i].add(val)
                cols[c_i].add(val)
        return True
