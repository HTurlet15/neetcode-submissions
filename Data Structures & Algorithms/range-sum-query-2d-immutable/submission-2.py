class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(m):
            for col in range(n):
                self.P[row+1][col+1] = (matrix[row][col] + 
                self.P[row][col+1] + 
                self.P[row+1][col] -
                self.P[row][col])
        print(self.P)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.P[row2+1][col2+1] - self.P[row1][col2+1]
        - self.P[row2+1][col1] + self.P[row1][col1])