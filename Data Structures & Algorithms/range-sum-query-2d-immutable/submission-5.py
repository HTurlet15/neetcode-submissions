class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS+1) for r in range(ROWS+1)]
        
        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix+=matrix[row][col]
                above = self.sumMat[row][col+1]
                self.sumMat[row+1][col+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1+1, col1+1, row2+1, col2+1
        return (self.sumMat[r2][c2] -
         self.sumMat[r2][c1-1] - 
         self.sumMat[r1-1][c2] + 
         self.sumMat[r1-1][c1-1] )