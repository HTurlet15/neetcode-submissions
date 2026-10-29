class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_2D = []
        self.prefix_1D = []
        total = 0
        for list_1D in matrix:
            for num in list_1D :
                total+=num
                self.prefix_1D.append(total)
            total = 0
            self.prefix_2D.append(self.prefix_1D)
            self.prefix_1D = []

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = 0
        for row in range(row1,row2+1,1) :
            prefix_left_row = 0
            if col1 > 0 :
                prefix_left_row = self.prefix_2D[row][col1-1]
            prefix_right_row = self.prefix_2D[row][col2]
            total_sum += prefix_right_row - prefix_left_row
        return total_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)