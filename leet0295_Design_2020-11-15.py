class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        
        # we seperate the first row and column as indicators.
        # check if the first row need to be zero
        first_row_zero = False
        for j in range(len(matrix[0])):
            if not matrix[0][j]:
                first_row_zero = True
                break
        # check if the first column need to be zero
        first_col_zero = False
        for i in range(len(matrix)):
            if not matrix[i][0]:
                first_col_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]== 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0       
        # set first row
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        
                   
                
